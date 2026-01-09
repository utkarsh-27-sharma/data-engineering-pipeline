import csv
from pathlib import Path
from typing import List, Dict

PROCESSED_DATA_PATH = Path("data/processed/sales_processed.csv")

def write_processed_data(records: List[Dict], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not records:
        raise ValueError("No records to write")

    with open(output_path, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)

if __name__ == "__main__":
    print("This module is intended to be imported, not run directly.")
