# Демонстрационное приложение на aiohttp

Простое REST API для управления задачами (TODO list), созданное для изучения фреймворка aiohttp.

## 🎯 Что демонстрирует это приложение

### 1. Основы aiohttp
- Создание web-приложения
- Настройка маршрутов (routes)
- Обработчики запросов (handlers)
- Запуск сервера

### 2. HTTP методы
- **GET** - получение данных
- **POST** - создание данных
- **PUT** - обновление данных
- **DELETE** - удаление данных

### 3. Middleware
- Логирование запросов
- Обработка ошибок
- Цепочка обработки запросов

### 4. Работа с данными
- Parsing JSON из request body
- Возврат JSON responses
- Query parameters
- Path parameters

### 5. Обработка ошибок
- Валидация входных данных
- HTTP исключения (404, 400, 500)
- Кастомные сообщения об ошибках

### 6. Асинхронность
- async/await синтаксис
- Асинхронные HTTP клиенты (вызов внешних API)

## 🚀 Установка и запуск

### 1. Установите зависимости
```bash
pip install -r requirements.txt
```

### 2. Запустите сервер
```bash
python main.py
```

Сервер будет доступен на `http://localhost:8080`

## 📡 API Endpoints

### Health Check
```bash
# Проверка работоспособности сервиса
curl http://localhost:8080/health
```

### Создание задачи
```bash
# POST /tasks
curl -X POST http://localhost:8080/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Купить молоко", "description": "В магазине на углу"}'
```

### Получение всех задач
```bash
# GET /tasks
curl http://localhost:8080/tasks

# С фильтром по статусу
curl http://localhost:8080/tasks?completed=false
```

### Получение конкретной задачи
```bash
# GET /tasks/{id}
curl http://localhost:8080/tasks/1
```

### Обновление задачи
```bash
# PUT /tasks/{id}
curl -X PUT http://localhost:8080/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Купить молоко и хлеб", "completed": true}'
```

### Удаление задачи
```bash
# DELETE /tasks/{id}
curl -X DELETE http://localhost:8080/tasks/1
```

### Массовое выполнение задач
```bash
# POST /tasks/bulk-complete
curl -X POST http://localhost:8080/tasks/bulk-complete \
  -H "Content-Type: application/json" \
  -d '{"task_ids": [1, 2, 3]}'
```

### Статистика
```bash
# GET /stats
curl http://localhost:8080/stats
```

### Демо внешнего API
```bash
# GET /external
curl http://localhost:8080/external
```

## 🔍 Примеры использования

### Сценарий 1: Создание и управление задачами
```bash
# 1. Создаем несколько задач
curl -X POST http://localhost:8080/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Задача 1", "description": "Описание 1"}'

curl -X POST http://localhost:8080/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Задача 2", "description": "Описание 2"}'

curl -X POST http://localhost:8080/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Задача 3", "description": "Описание 3"}'

# 2. Получаем список всех задач
curl http://localhost:8080/tasks

# 3. Отмечаем задачу как выполненную
curl -X PUT http://localhost:8080/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'

# 4. Проверяем статистику
curl http://localhost:8080/stats

# 5. Получаем только невыполненные задачи
curl http://localhost:8080/tasks?completed=false
```

### Сценарий 2: Обработка ошибок
```bash
# Попытка создать задачу без title (ошибка 400)
curl -X POST http://localhost:8080/tasks \
  -H "Content-Type: application/json" \
  -d '{"description": "Только описание"}'

# Попытка получить несуществующую задачу (ошибка 404)
curl http://localhost:8080/tasks/999

# Отправка невалидного JSON (ошибка 400)
curl -X POST http://localhost:8080/tasks \
  -H "Content-Type: application/json" \
  -d '{invalid json}'
```

## 📚 Ключевые концепции aiohttp

### 1. Application
```python
app = web.Application()
```
Основной объект приложения, который содержит маршруты, middleware и настройки.

### 2. Request
```python
async def handler(request: web.Request) -> web.Response:
    # Получение данных из запроса
    data = await request.json()          # JSON body
    param = request.query.get('param')   # Query parameter
    path_id = request.match_info['id']   # Path parameter
```

### 3. Response
```python
# JSON response
return web.json_response({'key': 'value'})

# HTTP исключения
raise web.HTTPNotFound()
raise web.HTTPBadRequest()
```

### 4. Middleware
```python
@web.middleware
async def my_middleware(request, handler):
    # Код до обработки запроса
    response = await handler(request)
    # Код после обработки запроса
    return response
```

### 5. Routes
```python
app.router.add_get('/path', handler)
app.router.add_post('/path', handler)
app.router.add_put('/path/{id}', handler)
app.router.add_delete('/path/{id}', handler)
```

## 🎓 Что изучить дальше

После освоения этого примера, рекомендую изучить:

1. **Интеграция с базами данных**
   - aiopg (PostgreSQL)
   - motor (MongoDB)
   - aiosqlite (SQLite)

2. **Валидация данных**
   - pydantic
   - marshmallow

3. **Аутентификация и авторизация**
   - aiohttp-security
   - JWT tokens

4. **WebSockets**
   - Встроенная поддержка WebSocket в aiohttp

5. **Тестирование**
   - pytest-aiohttp
   - Unit и integration тесты

6. **Deployment**
   - Docker
   - systemd
   - nginx as reverse proxy

## 💡 Советы

1. **Логирование**: В production используйте полноценную библиотеку логирования (logging)
2. **База данных**: Для реальных приложений используйте полноценную БД вместо словаря в памяти
3. **Валидация**: Используйте библиотеки типа pydantic для строгой валидации данных
4. **CORS**: При разработке frontend может понадобиться aiohttp-cors
5. **Environment variables**: Для настроек используйте переменные окружения

## 🐛 Отладка

Приложение выводит логи всех запросов в консоль благодаря middleware. Вы увидите:
- HTTP метод и путь
- Query параметры
- Статус ответа
- Ошибки если они возникли

## 📝 Структура кода

- **Middleware** - функции, которые вызываются для каждого запроса
- **Handlers** - обработчики конкретных endpoints
- **Валидация** - проверка входных данных
- **Хранилище** - простая БД в памяти (словарь)
- **Application Setup** - конфигурация приложения и маршрутов

Enjoy learning aiohttp! 🚀

