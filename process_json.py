import json

# Open and load the json file

# Function to safely convert a value to float, removing commas
def safe_float(value):
    if value:  # Check if the value is not None or empty
        try:
            # Remove commas and convert to float
            return float(value.replace(",", ""))
        except ValueError:
            # Return 0.0 if conversion fails
            return 0.0
    return 0.0  # Return 0.0 if the value is None or empty

with open('stock_market_data.json', 'r') as file:
    data = json.load(file)

    # Initialize the list to hold transformed data
    trade_data = []

    for index, item in enumerate(data):
        trade_data.append({
            "model": "Trade.tradedata",
            "pk": index + 1,
            "fields": {
                "date": item["date"],
                "trade_code": item["trade_code"],
                "high": safe_float(item["high"]),
                "low": safe_float(item["low"]),
                "open": safe_float(item["open"]),
                "close": safe_float(item["close"]),
                "volume": safe_float(item["volume"])
            }
        })

# Write the transformed data to a new file or overwrite the existing one
with open("./Trade/fixtures/trade_data.json", "w") as json_file:
    json.dump(trade_data, json_file, indent=4)

print("Data has been transformed and saved.")