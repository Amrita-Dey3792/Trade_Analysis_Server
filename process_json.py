import json

def safe_float(value):
    if value:  
        try:
            return float(value.replace(",", ""))
        except ValueError:
        
            return 0.0
    return 0.0  

with open('stock_market_data.json', 'r') as file:
    data = json.load(file)
    
    trade_data = []

    for index, item in enumerate(data):
        trade_data.append({
            "model": "Trade.stock",
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

with open("./Trade/fixtures/stocks.json", "w") as json_file:
    json.dump(trade_data, json_file, indent=4)

print("Data has been transformed and saved.")