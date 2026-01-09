import csv
from pathlib import Path

RAW_DATA_PATH = Path("data/raw/sales.csv")

def read_sales_data(file_path: Path):
    if not file_path.exists():
        raise FileNotFoundError(f"Raw data file not found: {file_path}")

    records = []
    with open(file_path, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            records.append(row)

    return records

if __name__ == "__main__":
    data = read_sales_data(RAW_DATA_PATH)
    print(f"Total records read: {len(data)}")
    for record in data:
        print(record)
