from flask import Blueprint
from twilio.rest import Client
import os
from dotenv import load_dotenv
from disaster_management.models import create_mongo_client, init_database, init_collection
import requests

load_dotenv()

req_coll = ["end_user"]
dbs = {name: init_collection(init_database(create_mongo_client(), "Disaster-ManagementDB"), name) for name in req_coll}

end_user = Blueprint('end_user', __name__)

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

# Admin phone number
admin_number = os.environ.get("TWILIO_ADMIN_NUMBER")

# Initialize Twilio Client
client = Client(account_sid, auth_token)

def process_messages():
    # Retrieve messages sent to the admin number
    messages = client.messages.list(
        to=admin_number,
        limit=10  # You can adjust the limit as per your requirement
    )

    # Store only the numbers starting with "+91" and with the body "HELP"
    sender_numbers_perm = [message.from_ for message in messages if message.from_.startswith("+91") and message.body.strip().upper() == "HELP"]
    return sender_numbers_perm

def sending_template_messages(sender_numbers):
    # Define your template message
    template_message = (
        "Hello! Thank you for contacting us. To better assist you, please provide the following details:\n"
        "Name:\n"
        "City:\n"
        "Pincode:\n"
        "Address:\n"
        "\n"
        "Confirm us that you are in trouble by sending us these details"
        "Once you provide these details, we'll get back to you as soon as possible. Thank you!"
    )

    # Send the template message to the numbers stored in sender_numbers
    for number in sender_numbers:
        try:
            message = client.messages.create(
                body=template_message,
                from_=admin_number,
                to=number
            )
            print(f"Template message sent to {number} successfully. SID: {message.sid}")
        except Exception as e:
            print(f"Failed to send template message to {number}: {str(e)}")

@end_user.route('/')
def process_and_send_messages():
    # Process incoming messages and send template messages
    sender_numbers_perm = process_messages()
    print(sender_numbers_perm)
    sending_template_messages(sender_numbers_perm)
    
    return "Messages processed and template messages sent successfully!"

def get_lat_lng(pincode):
    url = f'https://nominatim.openstreetmap.org/search?postalcode={pincode}&format=json'
    response = requests.get(url)
    data = response.json()
    if data:
        lat = float(data[0]['lat'])
        lon = float(data[0]['lon'])
        return lat, lon
    else:
        print("No data found for the given pincode.")
        return None, None

@end_user.route("/store_messages", methods=["GET", "POST"])
def store_messages():
    sender_numbers_perm = process_messages()
    for number in sender_numbers_perm:
        messages = client.messages.list(
            from_=number,
            limit=1
        )
        for message in messages:
            # Split the message body by newline character
            message_parts = message.body.split('\n')

            # Check if the message body has enough lines and starts with "Name:"
            if len(message_parts) >= 4 and message_parts[0].startswith("Name:"):
                # Extract name, city, pincode, and address
                name = message_parts[0].split(': ')[1]
                city = message_parts[1].split(': ')[1]
                pincode = message_parts[2].split(': ')[1]
                address = message_parts[3].split(': ')[1]

                # Convert PIN code to latitude and longitude
                latitude, longitude = get_lat_lng(pincode)

                if latitude and longitude:
                    # Check if a document with the same details already exists
                    existing_document = dbs["end_user"].find_one({
                        'Name': name,
                        'City': city,
                        'Pincode': pincode,
                        'Address': address
                    })

                    if existing_document:
                        print("Data already available in the database:", existing_document)
                    else:
                        # Store message details along with latitude and longitude in a dictionary
                        message_data = {
                            'Name': name,
                            'City': city,
                            'Pincode': pincode,
                            'Address': address,
                            'Latitude': latitude,
                            'Longitude': longitude
                        }

                        # Insert message details into MongoDB collection
                        dbs["end_user"].insert_one(message_data)
                        print("Message inserted into the database")
                else:
                    print("Failed to convert pincode to latitude and longitude.")
            else:
                print("Message format is incorrect, skipping...")

    return "Messages stored successfully!"