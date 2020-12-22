import asyncio
import os
import json
from aiogithubapi import GitHub
from aiogithubapi.helpers import async_call_api

IDENTIFIER = "<!-- HACS action comment -->"


def get_token():
    with open(f"{os.getenv('GITHUB_ACTION_PATH')}/data/token", "r") as token:
        return token.read()


def get_event():
    with open(os.getenv('GITHUB_EVENT_PATH'), "r") as event:
        return event.read()


async def post():
    event = json.loads(get_event())
    print(json.dumps(event))
    if not event.get('pull_request'):
        return

    async with GitHub(get_token()) as github:
        name = event["repository"]["full_name"]
        number = event["pull_request"]["number"]
        msg = f"Hey!\\n\\n{IDENTIFIER}"
        print(name)
        print(number)
        print(msg)
        repository = await github.get_repo(name)
        pull = await repository.get_issue(number)
        pull.attributes["id"] = number
        comments = await pull.get_comments()
        for comment in comments:
            if IDENTIFIER in comment.body:
                await comment.update(msg)
                return

        await async_call_api(github.client.session, "POST", f"/repos/{name}/issues/{number}/comments", data={"body": msg})


asyncio.get_event_loop().run_until_complete(post())
