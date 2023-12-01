import pytest
import asyncio

# Асинхронная функция
async def async_function():
    # Некоторый асинхронный код
    await asyncio.sleep(1)
    return "Hello, World!"

# Асинхронный тест
@pytest.mark.asyncio
async def test_async_function():
    expected_result = "Hello, World!"

    # Используем event_loop для создания цикла событий
    async with asyncio.get_event_loop() as loop:
        # Вызываем асинхронную функцию и ожидаем результат
        result = await async_function()

        # Проверяем, что результат соответствует ожидаемому значению
        assert result == expected_result