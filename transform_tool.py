import yaml
import sys
import re

def transform_to_custom_language(data, indent=0):
    if isinstance(data, dict):
        result = "dict(\n"
        for key, value in data.items():
            result += " " * (indent + 4) + f"{key} = {transform_to_custom_language(value, indent + 4)};\n"
        result += " " * indent + ")"
        return result
    elif isinstance(data, list):
        values = " ".join(transform_to_custom_language(v, indent) for v in data)
        return f"{{ {values} }}"
    elif isinstance(data, str):
        return f"[[{data}]]"
    elif isinstance(data, (int, float)):
        return str(data)
    else:
        raise ValueError(f"Unsupported data type: {type(data)}")

def main():
    # Read the YAML input from standard input
    yaml_input = sys.stdin.read()

    try:
        # First, parse the YAML input
        data = yaml.safe_load(yaml_input)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        return

    try:
        # Transform to custom configuration language
        output = transform_to_custom_language(data)
        print(output)
    except Exception as e:
        print(f"Error transforming data: {e}")

if __name__ == "__main__":
    main()
