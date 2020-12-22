import asyncio
import os
import json
from aiogithubapi import GitHub
from aiogithubapi.helpers import async_call_api
from aiogithubapi.common.const import BASE_API_HEADERS, BASE_API_URL

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
        _headers = BASE_API_HEADERS
        _headers["Authorization"] = f"token {github.client.token}"

        name = event["repository"]["full_name"]
        number = event["pull_request"]["number"]
        msg = f"Hey!\\n\\n{IDENTIFIER}"
        repository = await github.get_repo(name)
        pull = await repository.get_issue(number)
        pull.attributes["id"] = number
        comments = await pull.get_comments()
        for comment in comments:
            if IDENTIFIER in comment.body:
                await async_call_api(github.client.session, "POST", f"{BASE_API_URL}/repos/{name}/issues/{number}/comments/{comment.id}", data={"body": msg}, headers=BASE_API_HEADERS)
                return

        # await async_call_api(github.client.session, "POST", f"{BASE_API_URL}/repos/{name}/issues/{number}/comments", data=json.dumps({"body": msg}), headers={"Accept": "application/vnd.github.v3+json"})
        await github.client.session.post(
            f"{BASE_API_URL}/repos/{name}/issues/{number}/comments",
            data=json.dumps({{"body": msg}}),
            headers=_headers
        )


asyncio.get_event_loop().run_until_complete(post())
