import pytest

async def async_function():
    # Эта функция просто отклоняет промис с исключением.
    raise ValueError("Expected error")

@pytest.mark.asyncio
async def test_async_function_raises_expected_error(event_loop):
    # Вызываем асинхронную функцию в пределах фикстуры event_loop.
    with pytest.raises(ValueError, match="Expected error"):
        await async_function()