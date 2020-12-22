import os

with open(f"{os.getenv('GITHUB_ACTION_PATH')}/data/readme.md", "r") as inputfile:
    for line in inputfile.read().split("\n"):
        if "<img" in line or "![" in line and not "img.shields.io" in line:
            print(line)
