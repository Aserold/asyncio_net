import asyncio

import datetime

import requests


async def get_person(person_id):
    return 21


async def main():
    coro_person_1 = get_person(1)
    coro_person_2 = get_person(2)
    coro_person_3 = get_person(3)
    coro_person_4 = get_person(4)
    person_1 = await coro_person_1
    person_2 = await coro_person_2
    person_3 = await coro_person_3
    person_4 = await coro_person_4

    print(person_1, person_2, person_3, person_4)


if __name__ == '__main__':
    start = datetime.datetime.now()
    main()
    print(datetime.datetime.now() - start)