import requests
import pandas as pd

base_currency = "USD"
url = f"https://open.er-api.com/v6/latest/{base_currency}"

response = requests.get(url, timeout=10)
data = response.json()

if data["result"] == "success":
    target_currencies = ["INR", "EUR", "GBP", "JPY", "CAD"]
    rates = data["rates"]
    filtered = {k: v for k, v in rates.items() if k in target_currencies}
    df = pd.DataFrame(list(filtered.items()), columns=["Currency", "Rate"])
    df["BaseCurrency"] = base_currency
    df["Date"] = data["time_last_update_utc"]
else:
    df = pd.DataFrame({"Error": [data.get("error-type", "Unknown error")]})

print(df) 
