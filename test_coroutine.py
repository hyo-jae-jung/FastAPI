import asyncio
import time 

async def coroutine_1():
    print("Coroutine 1 is running")
    await asyncio.sleep(2)
    print("Coroutine 1 is done")

async def coroutine_2():
    print("Coroutine 2 is running")
    await asyncio.sleep(1)
    print("Coroutine 2 is done")

async def main():
    print("Main coroutine is running")
    task1 = asyncio.create_task(coroutine_1())
    task2 = asyncio.create_task(coroutine_2())
    
    await task1
    await task2
    
    print("Main coroutine is done")

start = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
print(time.time() - start)
