import json
from dotenv import load_dotenv
import os
import time
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")


def text_to_speech(text='Привет Ириша!'):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = "https://api.edenai.run/v2/audio/text_to_speech"
    payload = {"providers": "google",
               "language": "ru-RU",
               "option": "FEMALE",
               "google - studio": "ru-RU-Standard-C",
               "text": f"{text}"}

    response = requests.post(url, json=payload, headers=headers)

    result = json.loads(response.text)
    unx_time = int(time.time())

    with open(f"{unx_time}.json", "w") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    audio_url = result.get('google').get('audio_resource_url')
    r = requests.get(audio_url)

    with open(f'{unx_time}.mp3', "wb") as f:
        f.write(r.content)


def main():
    text_to_speech(text=input('Введите текст...'))


if __name__ == '__main__':
    main()
