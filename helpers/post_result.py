import asyncio
import os
from aiogithubapi import GitHub

def get_token():
    with open(f"{os.getenv('GITHUB_ACTION_PATH')}/data/token", "r") as token:
        return token.read()

def get_event():
    with open(os.getenv('GITHUB_EVENT_PATH'), "r") as event:
        print(event.read())


async def post():
    get_event()
    async with GitHub(get_token()) as github:
        repository = await github.get_repo("ludeeus/aiogithubapi")
        print("Repository description:", repository.full_name)
        print("Repository description:", repository.description)


asyncio.get_event_loop().run_until_complete(post())