import os, json
from util.logger import enable_logging

@enable_logging
def read_json_as_dict(file_name: str) -> dict:
    if not os.path.exists(file_name):
        raise ValueError(f"[Error] File not found: {file_name}")
    with open(file_name, "r", encoding="utf-8") as f:
        return json.load(f)
