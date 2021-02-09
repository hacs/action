
#!/bin/sh

cat /validate/files.json | jq -r '.[]' | python3 /validate