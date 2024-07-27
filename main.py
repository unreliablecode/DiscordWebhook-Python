import requests
import json

# Define your webhook URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/your_webhook_id/your_webhook_token'

# Define the payload
payload = {
    'username': 'Custom Username',  # Replace with the desired username
    'avatar_url': 'https://example.com/path/to/avatar.png',  # Replace with the desired avatar URL
    'content': 'Hello, this is a test message!'  # Replace with the desired message
}

# Send the POST request
response = requests.post(
    WEBHOOK_URL,
    data=json.dumps(payload),
    headers={'Content-Type': 'application/json'}
)

# Check if the request was successful
if response.status_code == 204:
    print('Message sent successfully!')
else:
    print(f'Failed to send message. Status code: {response.status_code}')
    print(f'Response: {response.text}')
