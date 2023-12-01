import asyncio
import threading
import pytest

async def async_function_to_run():
    # Пример асинхронной функции, которую мы будем запускать
    await asyncio.sleep(1)
    return "Async function result"

def run_async_function_in_thread():
    # Функция для запуска асинхронной функции в отдельном потоке
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    result = loop.run_until_complete(async_function_to_run())

    loop.close()
    return result

@pytest.mark.asyncio
async def test_run_async_function_in_thread():
    # Тест проверяет, что результат функции run_async_function_in_thread корректен
    event_loop = asyncio.get_event_loop()

    # Запускаем асинхронную функцию в отдельном потоке
    result_future = event_loop.run_in_executor(None, run_async_function_in_thread)

    # Ждем завершения выполнения асинхронной функции в отдельном потоке
    result = await result_future

    # Проверяем, что результат соответствует ожидаемому
    assert result == "Async function result"

# Если запускаете тесты с помощью pytest, может просто вызвать pytest в консоли:
# pytest test_async_function.py