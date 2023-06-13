import asyncio
from asyncio import sleep
import asyncpg

QUERY = """"INSERT INTO some test table VALUES ($1,$2,$3)"""


async def make_request(db_pool):
    await db_pool.fetch(QUERY, 1, "some striing", 3)
    await sleep(.1)


async def main():
    chunk = 200
    tasks = []
    pended = 0

    db_pool = await asyncpg.create_pool("postgresql://127.0.0.1:5432/postgres")

    for x in range(10_000):
        tasks.append(asyncio.create_task(make_request(db_pool)))
        pended += 1
        if len(tasks) == chunk or pended == 10000:
            await asyncio.gather(*tasks)
            tasks = []
            print(pended)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
