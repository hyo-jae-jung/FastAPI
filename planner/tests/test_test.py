import pytest

# 테스트를 위한 비동기 함수
async def async_function():
    return "Hello, Async!"

# 테스트 함수
@pytest.mark.asyncio
async def test_async_function():
    result = await async_function()
    assert result == "Hello, Async!"

# 테스트 실행
if __name__ == "__main__":
    pytest.main()
