#!/bin/sh

mkdir -p /action
mv /validate /action/validate
cd /action || exit 1
cat ./requirements.json
python3 -m validate