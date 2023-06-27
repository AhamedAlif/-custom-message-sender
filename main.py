import urllib.parse
import requests

number = input("Enter Number":)  # Replace with the actual mobile number
message = input("Enter Massage")# Replace with the actual message

base_url = "https://shopapp.self-shopping.com/public/smsapi"
params = {
    "mobile": number,
    "msg": message
}
api_url = base_url + "?" + urllib.parse.urlencode(params)

# Make the API request
response = requests.get(api_url)

# Handle the API response
if response.status_code == 200:
    print("SMS sent successfully.")
else:
    print("Failed to send the SMS.")
