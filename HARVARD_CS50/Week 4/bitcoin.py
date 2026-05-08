import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    amount = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    # Fetch data
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response.raise_for_status()

    # Parse JSON
    data = response.json()

    # Extract price - THIS IS USUALLY THE CRASH POINT
    # Ensure keys are: "bpi" (lowercase) -> "USD" (uppercase) -> "rate_float" (underscore)
    price = data["bpi"]["USD"]["rate_float"]

    total = amount * price
    print(f"${total:,.4f}")

except requests.RequestException:
    sys.exit("Request error")
except KeyError:
    sys.exit("JSON structure error")
