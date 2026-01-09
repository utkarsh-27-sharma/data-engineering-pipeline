from src.ingestion.read_csv import read_sales_data, RAW_DATA_PATH
from src.transformation.clean_sales_data import clean_sales_data

if __name__ == "__main__":
    raw_records = read_sales_data(RAW_DATA_PATH)
    cleaned_records = clean_sales_data(raw_records)

    for record in cleaned_records:
        print(record)
