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
        comment_id = None
        name = event["repository"]["full_name"]
        number = event["pull_request"]["number"]
        print(name)
        print(number)
        repository = await github.get_repo(name)
        pull = await repository.get_issue(number)
        comments = await pull.get_comments()
        for comment in comments:
            if IDENTIFIER in comment.body:
                comment_id = comment.id

        if comment_id is None:
            await pull.comment("Hey!\\n\\n{IDENTIFIER}")


asyncio.get_event_loop().run_until_complete(post())
