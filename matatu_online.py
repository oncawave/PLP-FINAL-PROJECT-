import random
import time
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth

# --- M-PESA CONFIG ---
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
shortcode = 'YOUR_SHORTCODE'
passkey = 'YOUR_PASSKEY'
callback_url = "https://yourdomain.com/callback"

def get_access_token():
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    return response.json()['access_token']

def send_stk_push(phone_number, amount):
    access_token = get_access_token()
    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode((shortcode + passkey + timestamp).encode()).decode()

    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {
        "BusinessShortCode": shortcode,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": shortcode,
        "PhoneNumber": phone_number,
        "CallBackURL": callback_url,
        "AccountReference": "MatatuOnline",
        "TransactionDesc": "Matatu fare payment"
    }

    response = requests.post(url, json=payload, headers=headers)
    print("\n📤 MPesa STK Push Sent:")
    print(response.json())

# --- TRANSPORT SYSTEM LOGIC ---
class User:
    def __init__(self, name, phone, user_type):
        self.name = name
        self.phone = phone
        self.user_type = user_type  # passenger or driver
        self.location = random.choice(["CBD", "Westlands", "Langata", "Thika", "Karen", "Kasarani"])

class Matatu:
    def __init__(self, driver):
        self.driver = driver
        self.available = True

class Ride:
    def __init__(self, passenger, matatu, destination):
        self.passenger = passenger
        self.matatu = matatu
        self.destination = destination
        self.fare = random.randint(100, 300)

    def confirm_payment(self):
        print(f"\n💳 Estimated Fare: KES {self.fare}")
        send_stk_push(self.passenger.phone, self.fare)
        input("📲 Confirm payment on your phone and press Enter to proceed...")

    def start_ride(self):
        print(f"\n🚐 Ride started from {self.passenger.location} to {self.destination}")
        self.matatu.available = False
        time.sleep(2)
        print("🛬 Ride completed!")
        self.matatu.available = True

# --- SAMPLE RUN ---
print("🚖 Welcome to Matatu Online 🚖")
name = input("Enter your name: ")
phone = input("Enter your phone number (e.g., 254712345678): ")
user_type = input("Are you a passenger or driver? ").lower()

user = User(name, phone, user_type)

if user.user_type == "passenger":
    driver = User("Mwangi", "254798112233", "driver")
    matatu = Matatu(driver)
    destination = input("Where are you headed? ")

    ride = Ride(user, matatu, destination)
    ride.confirm_payment()
    ride.start_ride()

else:
    print(f"\n🧑‍✈️ Welcome {user.name}, you're now registered as a Matatu driver!")

