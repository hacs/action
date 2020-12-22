import asyncio
import os
import json
from aiogithubapi import GitHub

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
        comments = await github.client.get(endpoint=f"/repos/{name}/issues/{number}/comments")
        for comment in comments:
            if IDENTIFIER in comment.body:
                await github.client.post(endpoint=f"/repos/{name}/issues/{number}/comments/{comment.id}", data={"body": msg}, jsondata=True)
                return

        await github.client.post(endpoint=f"/repos/{name}/issues/{number}/comments", data={"body": msg}, jsondata=True)


asyncio.get_event_loop().run_until_complete(post())
