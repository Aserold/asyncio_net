import asyncio
import datetime

import aiohttp
from more_itertools import chunked

from models import Session, SwapiPeople, engine, init_db

MAX_CHUNK = 10


async def get_person(client, person_id):
    http_response = await client.get(f"https://swapi.py4e.com/api/people/{person_id}/")
    json_result = await http_response.json()
    return json_result


async def insert_to_db(json_list):
    models = [SwapiPeople(json=json_item) for json_item in json_list]
    async with Session() as session:
        session.add_all(models)
        await session.commit()


async def main():
    await init_db()
    client = aiohttp.ClientSession()
    for chunk in chunked(range(1, 101), MAX_CHUNK):
        coros = [get_person(client, person_id) for person_id in chunk]
        result = await asyncio.gather(*coros)
        insert_task = asyncio.create_task(insert_to_db(result))

    task_set = asyncio.all_tasks() - {asyncio.current_task()}
    await asyncio.gather(*task_set)

    await client.close()
    await engine.dispose()


if __name__ == "__main__":
    start = datetime.datetime.now()
    asyncio.run(main())
    print(datetime.datetime.now() - start)
