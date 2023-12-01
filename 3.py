import pytest
import aiohttp

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

@pytest.mark.asyncio
async def test_fetch_data(event_loop):
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response_data = await fetch_data(api_url)

    # Проверка, что ответ не пустой
    assert response_data

    # Здесь вы можете добавить дополнительные проверки, в зависимости от структуры ответа API

    # Например, если API возвращает JSON, вы можете проверить, что это действительно JSON
    import json
    json_data = json.loads(response_data)
    assert isinstance(json_data, dict)

    # Также можно проверить какие-то конкретные значения в ответе, например, наличие ключа "userId"
    assert "userId" in json_data

    # Завершение теста
    print("Тест успешно выполнен.")