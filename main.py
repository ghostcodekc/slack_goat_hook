import json
import random
from slack_sdk.webhook import WebhookClient
import sys
# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)
# Verify it works
# from slack_sdk import WebClient
# client = WebClient()
# api_response = client.api_test()


f = open("wordlist.json")
data = json.load(f)
fact = random.choice(data)
print(fact)
# url = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"
# webhook = WebhookClient(url)
# response = webhook.send(
#     text="fallback",
#     blocks=[
#         {
#             "type": "section",
#             "text": {
#                 "type": "mrkdwn",
#                 "text": fact
#             }
#         }
#     ]
# )
f.close()