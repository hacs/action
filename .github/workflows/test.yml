name: HACS Action
on:
  pull_request:
  push:
    branches:
      - main

jobs:
  repository:
    runs-on: ubuntu-latest
    name: "${{ matrix.repository.category }}: ${{ matrix.repository.name }}"
    strategy:
      matrix:
        repository:
          - { "name": "hacs/integration", "category": "integration" }
          - {
              "name": "basnijholt/lovelace-ios-dark-mode-theme",
              "category": "theme",
            }
          - {
              "name": "home-assistant-community-themes/template",
              "category": "theme",
            }
          - {
              "name": "ofekashery/vertical-stack-in-card",
              "category": "plugin",
              "ignore": "images topics",
            }
          - {
              "name": "custom-cards/boilerplate-card",
              "category": "plugin",
              "ignore": "images",
            }
          - {
              "name": "hacs/ND-NotifyUpdates",
              "category": "netdaemon",
              "ignore": "topics",
            }
          - {
              "name": "ludeeus/ad-hacs",
              "category": "appdaemon",
              "ignore": "hacsjson",
            }
          - {
              "name": "ludeeus/ps-hacs",
              "category": "python_script",
              "ignore": "hacsjson information",
            }
    steps:
      - name: Checkout the repository
        uses: actions/checkout@v4.1.0

      - name: HACS Action
        uses: ./
        with:
          comment: false
          category: ${{ matrix.repository.category }}
          ignore: ${{ matrix.repository.ignore }}
          repository: ${{ matrix.repository.name }}
