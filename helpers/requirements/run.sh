#!/bin/sh

mkdir -p /action
mv /validate /action/validate
cd /action || exit 1
python3 -m validate