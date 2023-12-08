import requests

base = input("Enter a base currency: ")
target = input("Enter a target currency: ")

while True:
    try:
        amount = float(input("Enter the amount you want to convert: "))
    except ValueError:
        print("Invalid input. The amount should be float")
        continue

    if amount <= 0:
        print("The amount should be a positive number.")
        continue
    else:
        break

url = f"https://api.apilayer.com/fixer/convert?to={target}&from={base}&amount={amount}"

headers= {
  "apikey": "bBGXiYkmFq1sFHvfY3JQQKc4OBb29Dwc"
}

response = requests.request("GET", url, headers=headers)

status_code = response.status_code
if status_code == 200:
    result = response.json()['result']
    print(f"{amount} {base} = {result} {target}")
else:
    print(f"Error: {status_code}. Unable to fetch conversion rates.")
