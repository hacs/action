import json

with open("./requirements.json") as requirements_file:
  requirements = json.loads(requirements_file.read())

with open("./additional_requirements.json") as requirements_file:
  additional_requirements = json.loads(requirements_file.read())
  for req in additional_requirements["apk"]:
    if req not in requirements["apk"]:
      requirements["apk"].append(req)

with open("./requirements.json", "w") as requirements_file:
  requirements_file.write(json.dumps(requirements))