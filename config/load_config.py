import json
from pathlib import Path

CONFIG_PATH = Path("config/pipeline_config.json")

def load_pipeline_config():
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Config file not found: {CONFIG_PATH}")

    with open(CONFIG_PATH, "r") as file:
        return json.load(file)
