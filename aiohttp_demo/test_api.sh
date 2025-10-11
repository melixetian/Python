#!/bin/bash

# Скрипт для тестирования API
# Использование: ./test_api.sh

BASE_URL="http://localhost:8080"

echo "=========================================="
echo "🧪 Тестирование aiohttp API"
echo "=========================================="
echo ""

# Цвета для вывода
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 1. Health check
echo -e "${BLUE}1. Health Check${NC}"
curl -s "$BASE_URL/health" | python3 -m json.tool
echo -e "\n"

# 2. Создание задач
echo -e "${BLUE}2. Создание задач${NC}"
echo "Создаем задачу 1..."
curl -s -X POST "$BASE_URL/tasks" \
  -H "Content-Type: application/json" \
  -d '{"title": "Купить молоко", "description": "В магазине на углу"}' | python3 -m json.tool

echo "Создаем задачу 2..."
curl -s -X POST "$BASE_URL/tasks" \
  -H "Content-Type: application/json" \
  -d '{"title": "Написать код", "description": "Доделать фичу"}' | python3 -m json.tool

echo "Создаем задачу 3..."
curl -s -X POST "$BASE_URL/tasks" \
  -H "Content-Type: application/json" \
  -d '{"title": "Сходить в спортзал", "description": "Не забыть форму"}' | python3 -m json.tool
echo -e "\n"

# 3. Получение всех задач
echo -e "${BLUE}3. Получение всех задач${NC}"
curl -s "$BASE_URL/tasks" | python3 -m json.tool
echo -e "\n"

# 4. Получение конкретной задачи
echo -e "${BLUE}4. Получение задачи с ID=1${NC}"
curl -s "$BASE_URL/tasks/1" | python3 -m json.tool
echo -e "\n"

# 5. Обновление задачи
echo -e "${BLUE}5. Обновление задачи (отмечаем как выполненную)${NC}"
curl -s -X PUT "$BASE_URL/tasks/1" \
  -H "Content-Type: application/json" \
  -d '{"completed": true}' | python3 -m json.tool
echo -e "\n"

# 6. Массовое выполнение
echo -e "${BLUE}6. Массовое выполнение задач 2 и 3${NC}"
curl -s -X POST "$BASE_URL/tasks/bulk-complete" \
  -H "Content-Type: application/json" \
  -d '{"task_ids": [2, 3]}' | python3 -m json.tool
echo -e "\n"

# 7. Фильтрация выполненных задач
echo -e "${BLUE}7. Получение только выполненных задач${NC}"
curl -s "$BASE_URL/tasks?completed=true" | python3 -m json.tool
echo -e "\n"

# 8. Статистика
echo -e "${BLUE}8. Статистика${NC}"
curl -s "$BASE_URL/stats" | python3 -m json.tool
echo -e "\n"

# 9. Тест ошибок
echo -e "${BLUE}9. Тест обработки ошибок${NC}"
echo "Попытка создать задачу без title..."
curl -s -X POST "$BASE_URL/tasks" \
  -H "Content-Type: application/json" \
  -d '{"description": "Только описание"}' | python3 -m json.tool

echo "Попытка получить несуществующую задачу..."
curl -s "$BASE_URL/tasks/999" | python3 -m json.tool
echo -e "\n"

# 10. Удаление задачи
echo -e "${BLUE}10. Удаление задачи${NC}"
curl -s -X DELETE "$BASE_URL/tasks/1" | python3 -m json.tool
echo -e "\n"

# 11. Финальное состояние
echo -e "${BLUE}11. Финальное состояние всех задач${NC}"
curl -s "$BASE_URL/tasks" | python3 -m json.tool
echo -e "\n"

# 12. Внешний API
echo -e "${BLUE}12. Демо вызова внешнего API${NC}"
curl -s "$BASE_URL/external" | python3 -m json.tool
echo -e "\n"

echo -e "${GREEN}=========================================="
echo "✅ Тестирование завершено!"
echo "==========================================${NC}"

