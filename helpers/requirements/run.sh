#!/bin/sh

jq -r '.[]' /validate/files.json | python3 /validate