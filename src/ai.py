import requests

API_URL = "http://localhost:20128/v1/chat/completions"

def ask_ai(message, encoded_photo):
    data = {
        "model": "my-combo",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": message
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{encoded_photo}"
                        }
                    }
                ]
            }
        ],
        "stream": False
    }

    response = requests.post(
        API_URL,
        json=data
    )

    return response.json()