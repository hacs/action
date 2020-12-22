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
        print(event.read())


async def post():
    event = json.loads(get_event())
    if not event.get('pull_request'):
        return

    async with GitHub(get_token()) as github:
        comment_id = None
        repository = await github.get_repo(event["repository"]["full_name"])
        pull = await repository.get_issue(event["number"])
        comments = await pull.get_comments()
        for comment in comments:
            if IDENTIFIER in comment.body:
                comment_id = comment.id

        if not comment_id:
            await pull.comment(f"Hey!\n\n{IDENTIFIER}")


asyncio.get_event_loop().run_until_complete(post())
