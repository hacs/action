import asyncio
import os
import json
from aiogithubapi import GitHub
from aiogithubapi.common.const import BASE_API_HEADERS, BASE_API_URL

IDENTIFIER = "<!-- HACS action comment -->"


def get_token():
    with open(f"{os.getenv('GITHUB_ACTION_PATH')}/data/token", "r") as token:
        return token.read().replace("\n", "")


def get_event():
    with open(os.getenv('GITHUB_EVENT_PATH'), "r") as event:
        return event.read()


async def post():
    event = json.loads(get_event())
    if not event.get('pull_request'):
        return

    async with GitHub(get_token()) as github:
        name = event["repository"]["full_name"]
        number = event["pull_request"]["number"]
        msg = f"Hey!\\n\\n{IDENTIFIER}"

        _headers = BASE_API_HEADERS
        _headers["Authorization"] = f"token {github.client.token}"
        _endpoint = f"{BASE_API_URL}/repos/{name}/issues/{number}/comments"

        request = await github.client.session.get(_endpoint, headers=_headers)
        comments = await request.json()
        for comment in comments:
            if IDENTIFIER in comment["body"]:
                _endpoint = f"{BASE_API_URL}/repos/{name}/issues/{number}/comments/{comment['id']}"
                break

        result = await github.client.session.post(_endpoint, json={"body": msg}, headers=_headers)
        if result.status != 200:
            print(result.reason)
            exit(1)


asyncio.get_event_loop().run_until_complete(post())
