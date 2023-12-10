import asyncio
import random, time
async def f(x):
    while True:
        await asyncio.sleep(x*0.5)
        print("  "*x,x)


async def main():
    pass
    tasks = []
    tasks.append( asyncio.create_task( f(1)))
    tasks.append( asyncio.create_task( f(2)))
    tasks.append( asyncio.create_task( f(3)))
    tasks.append( asyncio.create_task( f(4)))
    for i in range(len(tasks)):
        await(tasks[i])

asyncio.run(main())