import sys
import json

from .validate_requirements import validate_requirements


def main() -> int:
    """Run main function."""
    return 0 if validate() else 1


def validate() -> bool:
    """Do the validation."""
    print("Validating requirements")
    print()
    requirements = []
    with open("/action/validate/files.json", "r") as requirements_file:
        requirements = json.loads(requirements_file.read())
    validated_ok = True
    print("Requirements to validate:", len(requirements))

    requirements_ok = validate_requirements(requirements)
    if requirements_ok:
        print("OK!")
    validated_ok = validated_ok and requirements_ok

    return validated_ok


sys.exit(main())
