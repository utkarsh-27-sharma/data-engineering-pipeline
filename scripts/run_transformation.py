from src.ingestion.read_csv import read_sales_data, RAW_DATA_PATH
from src.transformation.clean_sales_data import clean_sales_data
from src.loading.write_processed_data import write_processed_data, PROCESSED_DATA_PATH

if __name__ == "__main__":
    raw_records = read_sales_data(RAW_DATA_PATH)
    cleaned_records = clean_sales_data(raw_records)
    write_processed_data(cleaned_records, PROCESSED_DATA_PATH)

    print(f"Processed data written to {PROCESSED_DATA_PATH}")
