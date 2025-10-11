"""
Демонстрационное приложение на aiohttp
REST API для управления задачами (TODO list)
"""

import json
from datetime import datetime

import aiohttp
from aiohttp import web

# Хранилище данных в памяти
tasks_db: dict[int, dict] = {}
task_id_counter = 1


# ==================== Middleware ====================


@web.middleware
async def logging_middleware(request: web.Request, handler):
    """Middleware для логирования всех запросов"""
    print(f"\n>>> {request.method} {request.path}")
    print(f">>> Query params: {dict(request.query)}")

    try:
        response = await handler(request)
        print(f"<<< Response status: {response.status}")
        return response
    except web.HTTPException as ex:
        print(f"<<< HTTP Exception: {ex.status}")
        raise
    except Exception as ex:
        print(f"<<< Error: {ex}")
        raise


@web.middleware
async def error_handling_middleware(request: web.Request, handler):
    """Middleware для обработки ошибок"""
    try:
        return await handler(request)
    except json.JSONDecodeError:
        return web.json_response({"error": "Invalid JSON"}, status=400)
    except web.HTTPException:
        raise
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        return web.json_response({"error": "Internal server error", "details": str(ex)}, status=500)


# ==================== Handlers ====================


async def health_check(request: web.Request) -> web.Response:
    """Проверка здоровья сервиса"""
    return web.json_response({"status": "ok", "timestamp": datetime.now().isoformat(), "tasks_count": len(tasks_db)})


async def get_all_tasks(request: web.Request) -> web.Response:
    """
    GET /tasks - Получить все задачи
    Query params:
        - completed: true/false - фильтр по статусу выполнения
    """
    # Фильтрация по статусу
    completed_filter = request.query.get("completed")

    tasks = list(tasks_db.values())

    if completed_filter is not None:
        is_completed = completed_filter.lower() == "true"
        tasks = [t for t in tasks if t["completed"] == is_completed]

    return web.json_response({"tasks": tasks, "count": len(tasks)})


async def get_task(request: web.Request) -> web.Response:
    """GET /tasks/{id} - Получить задачу по ID"""
    task_id = int(request.match_info["id"])

    task = tasks_db.get(task_id)
    if not task:
        raise web.HTTPNotFound(text=json.dumps({"error": f"Task {task_id} not found"}), content_type="application/json")

    return web.json_response(task)


async def create_task(request: web.Request) -> web.Response:
    """
    POST /tasks - Создать новую задачу
    Body: {"title": "...", "description": "..."}
    """
    global task_id_counter

    data = await request.json()

    # Валидация
    if "title" not in data or not data["title"].strip():
        raise web.HTTPBadRequest(text=json.dumps({"error": "Title is required"}), content_type="application/json")

    task = {
        "id": task_id_counter,
        "title": data["title"].strip(),
        "description": data.get("description", "").strip(),
        "completed": False,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
    }

    tasks_db[task_id_counter] = task
    task_id_counter += 1

    return web.json_response(task, status=201)


async def update_task(request: web.Request) -> web.Response:
    """
    PUT /tasks/{id} - Обновить задачу
    Body: {"title": "...", "description": "...", "completed": true/false}
    """
    task_id = int(request.match_info["id"])

    task = tasks_db.get(task_id)
    if not task:
        raise web.HTTPNotFound(text=json.dumps({"error": f"Task {task_id} not found"}), content_type="application/json")

    data = await request.json()

    # Обновляем поля
    if "title" in data:
        if not data["title"].strip():
            raise web.HTTPBadRequest(
                text=json.dumps({"error": "Title cannot be empty"}), content_type="application/json"
            )
        task["title"] = data["title"].strip()

    if "description" in data:
        task["description"] = data["description"].strip()

    if "completed" in data:
        task["completed"] = bool(data["completed"])

    task["updated_at"] = datetime.now().isoformat()

    return web.json_response(task)


async def delete_task(request: web.Request) -> web.Response:
    """DELETE /tasks/{id} - Удалить задачу"""
    task_id = int(request.match_info["id"])

    task = tasks_db.pop(task_id, None)
    if not task:
        raise web.HTTPNotFound(text=json.dumps({"error": f"Task {task_id} not found"}), content_type="application/json")

    return web.json_response({"message": "Task deleted", "task": task})


async def bulk_complete(request: web.Request) -> web.Response:
    """
    POST /tasks/bulk-complete - Пометить несколько задач как выполненные
    Body: {"task_ids": [1, 2, 3]}
    """
    data = await request.json()
    task_ids = data.get("task_ids", [])

    if not isinstance(task_ids, list):
        raise web.HTTPBadRequest(
            text=json.dumps({"error": "task_ids must be an array"}), content_type="application/json"
        )

    updated_tasks = []
    not_found = []

    for task_id in task_ids:
        task = tasks_db.get(task_id)
        if task:
            task["completed"] = True
            task["updated_at"] = datetime.now().isoformat()
            updated_tasks.append(task)
        else:
            not_found.append(task_id)

    return web.json_response({"updated": updated_tasks, "not_found": not_found, "count": len(updated_tasks)})


async def stats(request: web.Request) -> web.Response:
    """GET /stats - Статистика по задачам"""
    total = len(tasks_db)
    completed = sum(1 for t in tasks_db.values() if t["completed"])
    pending = total - completed

    return web.json_response(
        {
            "total": total,
            "completed": completed,
            "pending": pending,
            "completion_rate": round(completed / total * 100, 2) if total > 0 else 0,
        }
    )


async def external_api_demo(request: web.Request) -> web.Response:
    """
    GET /external - Демонстрация вызова внешнего API
    Получает случайный факт из внешнего API
    """
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get("https://uselessfacts.jsph.pl/random.json?language=en") as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return web.json_response(
                        {"source": "uselessfacts.jsph.pl", "fact": data.get("text", "No fact available")}
                    )
                else:
                    return web.json_response({"error": "Failed to fetch external data"}, status=502)
        except Exception as e:
            return web.json_response({"error": "External API unavailable", "details": str(e)}, status=503)


# ==================== Application Setup ====================


def create_app() -> web.Application:
    """Создание и конфигурация приложения"""
    app = web.Application(
        middlewares=[
            logging_middleware,
            error_handling_middleware,
        ]
    )

    # Маршруты
    app.router.add_get("/health", health_check)
    app.router.add_get("/stats", stats)
    app.router.add_get("/external", external_api_demo)

    # CRUD для задач
    app.router.add_get("/tasks", get_all_tasks)
    app.router.add_get("/tasks/{id}", get_task)
    app.router.add_post("/tasks", create_task)
    app.router.add_put("/tasks/{id}", update_task)
    app.router.add_delete("/tasks/{id}", delete_task)

    # Дополнительные операции
    app.router.add_post("/tasks/bulk-complete", bulk_complete)

    return app


def main():
    """Запуск сервера"""
    app = create_app()

    print("=" * 60)
    print("🚀 Starting aiohttp demo server")
    print("=" * 60)
    print("Available endpoints:")
    print("  GET    /health              - Health check")
    print("  GET    /stats               - Task statistics")
    print("  GET    /external            - External API demo")
    print("  GET    /tasks               - Get all tasks")
    print("  GET    /tasks/{id}          - Get task by ID")
    print("  POST   /tasks               - Create new task")
    print("  PUT    /tasks/{id}          - Update task")
    print("  DELETE /tasks/{id}          - Delete task")
    print("  POST   /tasks/bulk-complete - Mark multiple tasks as completed")
    print("=" * 60)
    print("Server running on http://localhost:8080")
    print("=" * 60)

    web.run_app(app, host="localhost", port=8080)


if __name__ == "__main__":
    main()
