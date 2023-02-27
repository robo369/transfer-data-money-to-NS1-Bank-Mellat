
import requests

url = "https://sadad.shaparak.ir/vpg/api/v0/Advice/Advice"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}
payload = {
    "Amount": 10000,
    "CellNumber": "09123456789",
    "MerchantId": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
    "OrderId": "123456789",
    "TerminalId": "XXXXXXX",
    "TransactionDate": "2023/02/24 14:35:30",
    "TransactionReferenceId": "123456789",
    "UserName": "XXXXXXXXXX",
    "UserPassword": "XXXXXXXXXX"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    print("Money transferred successfully!")
else:
    print("Error occurred: " + response.json()["ResDescription"])
