from pathlib import Path

from config.load_config import load_pipeline_config
from src.ingestion.read_csv import read_sales_data
from src.transformation.clean_sales_data import clean_sales_data
from src.loading.write_processed_data import write_processed_data

if __name__ == "__main__":
    config = load_pipeline_config()

    raw_data_path = Path(config["raw_data_path"])
    processed_data_path = Path(config["processed_data_path"])

    raw_records = read_sales_data(raw_data_path)
    cleaned_records = clean_sales_data(raw_records)
    write_processed_data(cleaned_records, processed_data_path)

    print(f"Processed data written to {processed_data_path}")
