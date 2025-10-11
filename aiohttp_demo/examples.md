# Практические примеры использования API

## 🔧 Инструменты для тестирования

### 1. curl (встроен в систему)
```bash
curl -X POST http://localhost:8080/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Моя задача"}'
```

### 2. httpie (более удобный, установка: `pip install httpie`)
```bash
http POST localhost:8080/tasks title="Моя задача" description="Описание"
```

### 3. Postman или Insomnia (GUI приложения)

### 4. Python requests
```python
import requests

response = requests.post(
    'http://localhost:8080/tasks',
    json={'title': 'Моя задача', 'description': 'Описание'}
)
print(response.json())
```

## 📋 Полный сценарий работы с API

### Шаг 1: Запуск сервера
```bash
python main.py
```

### Шаг 2: Проверка работоспособности
```bash
curl http://localhost:8080/health
```

Ожидаемый ответ:
```json
{
  "status": "ok",
  "timestamp": "2025-10-09T12:00:00.000000",
  "tasks_count": 0
}
```

### Шаг 3: Создание задач

#### Задача 1
```bash
curl -X POST http://localhost:8080/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Изучить aiohttp",
    "description": "Пройти через все примеры"
  }'
```

Ответ:
```json
{
  "id": 1,
  "title": "Изучить aiohttp",
  "description": "Пройти через все примеры",
  "completed": false,
  "created_at": "2025-10-09T12:00:00.000000",
  "updated_at": "2025-10-09T12:00:00.000000"
}
```

#### Задача 2
```bash
curl -X POST http://localhost:8080/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Написать свое API",
    "description": "Применить полученные знания"
  }'
```

#### Задача 3
```bash
curl -X POST http://localhost:8080/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Добавить тесты",
    "description": "Написать unit-тесты для API"
  }'
```

### Шаг 4: Просмотр всех задач
```bash
curl http://localhost:8080/tasks
```

Ответ:
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Изучить aiohttp",
      "description": "Пройти через все примеры",
      "completed": false,
      "created_at": "2025-10-09T12:00:00.000000",
      "updated_at": "2025-10-09T12:00:00.000000"
    },
    {
      "id": 2,
      "title": "Написать свое API",
      "description": "Применить полученные знания",
      "completed": false,
      "created_at": "2025-10-09T12:01:00.000000",
      "updated_at": "2025-10-09T12:01:00.000000"
    },
    {
      "id": 3,
      "title": "Добавить тесты",
      "description": "Написать unit-тесты для API",
      "completed": false,
      "created_at": "2025-10-09T12:02:00.000000",
      "updated_at": "2025-10-09T12:02:00.000000"
    }
  ],
  "count": 3
}
```

### Шаг 5: Просмотр конкретной задачи
```bash
curl http://localhost:8080/tasks/1
```

### Шаг 6: Обновление задачи
```bash
curl -X PUT http://localhost:8080/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Изучить aiohttp ✓",
    "completed": true
  }'
```

### Шаг 7: Фильтрация задач

#### Только невыполненные
```bash
curl http://localhost:8080/tasks?completed=false
```

#### Только выполненные
```bash
curl http://localhost:8080/tasks?completed=true
```

### Шаг 8: Массовое выполнение задач
```bash
curl -X POST http://localhost:8080/tasks/bulk-complete \
  -H "Content-Type: application/json" \
  -d '{
    "task_ids": [2, 3]
  }'
```

Ответ:
```json
{
  "updated": [
    {
      "id": 2,
      "title": "Написать свое API",
      "description": "Применить полученные знания",
      "completed": true,
      "created_at": "2025-10-09T12:01:00.000000",
      "updated_at": "2025-10-09T12:10:00.000000"
    },
    {
      "id": 3,
      "title": "Добавить тесты",
      "description": "Написать unit-тесты для API",
      "completed": true,
      "created_at": "2025-10-09T12:02:00.000000",
      "updated_at": "2025-10-09T12:10:00.000000"
    }
  ],
  "not_found": [],
  "count": 2
}
```

### Шаг 9: Просмотр статистики
```bash
curl http://localhost:8080/stats
```

Ответ:
```json
{
  "total": 3,
  "completed": 3,
  "pending": 0,
  "completion_rate": 100.0
}
```

### Шаг 10: Удаление задачи
```bash
curl -X DELETE http://localhost:8080/tasks/1
```

Ответ:
```json
{
  "message": "Task deleted",
  "task": {
    "id": 1,
    "title": "Изучить aiohttp ✓",
    "description": "Пройти через все примеры",
    "completed": true,
    "created_at": "2025-10-09T12:00:00.000000",
    "updated_at": "2025-10-09T12:09:00.000000"
  }
}
```

## ❌ Примеры обработки ошибок

### Ошибка 400: Пустой title
```bash
curl -X POST http://localhost:8080/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Только описание"
  }'
```

Ответ:
```json
{
  "error": "Title is required"
}
```

### Ошибка 400: Невалидный JSON
```bash
curl -X POST http://localhost:8080/tasks \
  -H "Content-Type: application/json" \
  -d 'invalid json'
```

Ответ:
```json
{
  "error": "Invalid JSON"
}
```

### Ошибка 404: Задача не найдена
```bash
curl http://localhost:8080/tasks/999
```

Ответ:
```json
{
  "error": "Task 999 not found"
}
```

### Ошибка 400: Пустой title при обновлении
```bash
curl -X PUT http://localhost:8080/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": ""
  }'
```

Ответ:
```json
{
  "error": "Title cannot be empty"
}
```

## 🌐 Демо внешнего API

```bash
curl http://localhost:8080/external
```

Этот endpoint демонстрирует, как делать HTTP запросы к внешним API из вашего aiohttp приложения.

Ответ:
```json
{
  "source": "uselessfacts.jsph.pl",
  "fact": "Some random interesting fact..."
}
```

## 🧪 Автоматическое тестирование

Запустите готовый скрипт тестирования:
```bash
./test_api.sh
```

Этот скрипт автоматически выполнит все основные операции и покажет результаты.

## 🐍 Использование из Python

```python
import requests
import json

BASE_URL = "http://localhost:8080"

# Создание задачи
def create_task(title, description=""):
    response = requests.post(
        f"{BASE_URL}/tasks",
        json={"title": title, "description": description}
    )
    return response.json()

# Получение всех задач
def get_all_tasks(completed=None):
    params = {}
    if completed is not None:
        params['completed'] = 'true' if completed else 'false'
    
    response = requests.get(f"{BASE_URL}/tasks", params=params)
    return response.json()

# Обновление задачи
def update_task(task_id, **kwargs):
    response = requests.put(
        f"{BASE_URL}/tasks/{task_id}",
        json=kwargs
    )
    return response.json()

# Удаление задачи
def delete_task(task_id):
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    return response.json()

# Пример использования
if __name__ == "__main__":
    # Создаем задачи
    task1 = create_task("Задача из Python", "Создана программно")
    print(f"Создана задача: {task1['id']}")
    
    # Получаем все задачи
    all_tasks = get_all_tasks()
    print(f"Всего задач: {all_tasks['count']}")
    
    # Отмечаем как выполненную
    updated = update_task(task1['id'], completed=True)
    print(f"Задача обновлена: {updated['completed']}")
    
    # Удаляем
    deleted = delete_task(task1['id'])
    print(f"Задача удалена: {deleted['message']}")
```

## 📊 Наблюдение за логами

При запущенном сервере вы увидите в консоли логи всех запросов:

```
>>> POST /tasks
>>> Query params: {}
<<< Response status: 201

>>> GET /tasks
>>> Query params: {'completed': 'false'}
<<< Response status: 200

>>> PUT /tasks/1
>>> Query params: {}
<<< Response status: 200
```

Это помогает отладке и пониманию того, что происходит в приложении.

## 💡 Советы по использованию

1. **Держите сервер запущенным** - откройте один терминал для сервера, другой для тестирования
2. **Используйте json.tool** - для красивого вывода: `curl ... | python3 -m json.tool`
3. **Сохраняйте ID** - после создания задачи сохраните её ID для дальнейших операций
4. **Проверяйте статистику** - endpoint `/stats` полезен для быстрой проверки состояния
5. **Читайте логи** - в консоли сервера видны все запросы и ошибки

## 🎯 Задания для самостоятельной работы

1. Добавьте поле `priority` (низкий, средний, высокий) к задачам
2. Реализуйте фильтрацию по дате создания
3. Добавьте endpoint для поиска задач по ключевым словам
4. Реализуйте пагинацию для списка задач
5. Добавьте возможность добавлять теги к задачам
6. Реализуйте сортировку задач по разным полям

Удачи в изучении aiohttp! 🚀

