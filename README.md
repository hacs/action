# HACS Action

_Repository validation action for HACS_

## Inputs

| Input    | Description                                                                                        |
| -------- | -------------------------------------------------------------------------------------------------- |
| ignore   | A space seperated list of ignored checks                                                           |
| category | The type of repository (integration, plugin, template, theme, appdaemon, python_script) |

## Example

```yaml
name: HACS Action

on:
  push:
  pull_request:
  schedule:
    - cron: "0 0 * * *"

jobs:
  hacs:
    name: HACS Action
    runs-on: "ubuntu-latest"
    steps:
      - name: HACS Action
        uses: "hacs/action@main"
        with:
          category: "CHANGE_ME!"
```

## Ignorable checks

All these checks can be disabled with `with.ignore`. Use a string, and if you ignore multiple ones, seperate them with spaces.

| Check         | More info                | Description                                      |
| ------------- | ------------------------ | ------------------------------------------------ |
| `archived`    | [More info][archived]    | Checks if the repository is archived             |
| `brands`      | [More info][brands]      | Checks if the domain is added to the brands repo |
| `description` | [More info][description] | Checks if the repository has a description       |
| `hacsjson`    | [More info][hacsjson]    | Checks that hacs.json exists                     |
| `images`      | [More info][images]      | Checks that the info file has images             |
| `information` | [More info][information] | Checks that the repo has an information file     |
| `issues`      | [More info][issues]      | Checks that issues are enabled                   |
| `topics`      | [More info][topics]      | Checks that the repository has topics            |

[archived]: https://hacs.xyz/docs/publish/include#check-archived
[brands]: https://hacs.xyz/docs/publish/include#check-brands
[description]: https://hacs.xyz/docs/publish/include#check-repository
[hacsjson]: https://hacs.xyz/docs/publish/include#check-hacs-manifest
[images]: https://hacs.xyz/docs/publish/include#check-images
[information]: https://hacs.xyz/docs/publish/include#check-info
[issues]: https://hacs.xyz/docs/publish/include#check-repository
[topics]: https://hacs.xyz/docs/publish/include#check-repository

## Versions

To use a specific version of this action instead of `main` set the value after `@` in the `uses` definition, like:

```yaml
uses: hacs/action@xx.xx.x
```

If you do this, please enable [dependabot](https://dependabot.com/github-actions/) to help you keep that up to date.
