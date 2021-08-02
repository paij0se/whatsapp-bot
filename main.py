from twilio.rest import Client
import time
import random
import os
from dotenv import load_dotenv
import requests
import json


def main():
    load_dotenv()
    account_sid = os.getenv("TWILIO_SID")
    auth_token = os.getenv("TWILIO_TOKEN")
    twilio_number = os.getenv("TWILIO_NUMBER")
    whatsapp_number = os.getenv("WHATSAPP_NUMBER")
    client = Client(account_sid, auth_token)

    while True:
        subreddits = ["https://meme-api.herokuapp.com/gimme/MAUU/1",
                      "https://meme-api.herokuapp.com/gimme/DylanteroYT/1",
                      "https://meme-api.herokuapp.com/gimme/linuxmemes/1"]

        url = random.choice(subreddits)
        x = requests.get(url)
        parse_json = json.loads(x.text)
        image = parse_json["memes"][0]["url"]
        message = client.messages.create(
            from_=f'whatsapp:{twilio_number}',
            body=f'{parse_json["memes"][0]["title"]}',
            to=f'whatsapp:{whatsapp_number}',
            media_url=f'{image}'
        )

        print(message.sid)
        # send a image every 1 hour
        time.sleep(3600)


if __name__ == '__main__':
    main()
