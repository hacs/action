import os

ignored = [
    "-shield",
    "img.shields.io",
    "buymeacoffee.com"
]

with open(f"{os.getenv('GITHUB_ACTION_PATH')}/data/readme.md", "r") as inputfile:
    for line in inputfile.read().split("\n"):
        if "<img" in line or "![" in line:
            skip = False
            for ignore in ignored:
                if ignore in line:
                    skip = True
            if not skip:
                print(line)
