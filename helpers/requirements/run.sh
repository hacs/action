#!/bin/sh

mkdir -p /action
mv /validate /action/validate
cd /action || exit 1
cat /action/validate/files.json
python3 -m validate