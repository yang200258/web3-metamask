import asyncio


async def coroutine_example():
    await asyncio.sleep(3)
    print('zhihu ID: Zarten')


async def coroutine_example2():
    await asyncio.sleep(1)
    print('zhihu ID: Zarten22')

# coro = coroutine_example()

loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine_example())
print(222)
loop.run_until_complete(coroutine_example2())
loop.close()