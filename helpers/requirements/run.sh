#!/bin/sh

mkdir -p /action
mv /validate /action/validate
cd /action || exit 1
cat /action/validate/requirements.json
python3 -m validate