from typing import List, Dict

def clean_sales_data(records: List[Dict]) -> List[Dict]:
    cleaned = []

    for record in records:
        cleaned_record = {
            "order_id": int(record["order_id"]),
            "order_date": record["order_date"],
            "customer_id": record["customer_id"],
            "amount": int(record["amount"]),
        }
        cleaned.append(cleaned_record)

    return cleaned
