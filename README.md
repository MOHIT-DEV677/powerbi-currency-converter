# Currency Converter Dashboard (Power BI + Python)

This project is a **Currency Converter Dashboard** built using **Power BI** and enhanced with **Python integration** to fetch **real-time exchange rates** from the **Open Exchange Rates API**.

---

## Features

- Real-time exchange rate conversion using live API data.
- Converts from base currency **USD** to popular currencies: `INR`, `EUR`, `GBP`, `JPY`, `CAD`.
- Python script runs inside Power BI to fetch and format the data.
- Dynamic visuals for converted rates, base currency, and last updated time.
- Lightweight and fast-refreshing dashboard.

---

## Project Structure

currency-converter-project
├── currency_converter.pbix # Power BI dashboard file
├── fetch_currency_rates.py # Python script for API integration
└── README.md # Project documentation

## How to Use

1. Install **Power BI Desktop** (if not already installed).
2. Clone or download this repository.
3. Open the file `currency_converter.pbix` in Power BI Desktop.
4. Make sure **Python is installed** on your machine.
   - Recommended: Python 3.8+ and libraries `requests`, `pandas`
5. Configure Python in Power BI:
   - Go to `File → Options and settings → Options → Python scripting`
   - Set your local Python path
6. Click `Refresh` to pull live exchange rate data.
7. Interact with the dashboard to see conversions and rate information.

---

## API Details

- **API URL**: [`https://open.er-api.com/v6/latest/USD`](https://open.er-api.com)
- **Base Currency**: USD
- **Target Currencies**: INR, EUR, GBP, JPY, CAD
- **Update Frequency**: As per API refresh interval (usually every hour)

---

## Python Script

The data is fetched using the Python script [`fetch_currency_rates.py`](fetch_currency_rates.py), which is embedded in Power BI using the **"Run Python script"** option in Power Query.

### Required Python Libraries

Install these before refreshing the dashboard:

```bash
pip install requests pandas
