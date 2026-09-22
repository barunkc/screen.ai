from urllib import response

import requests
import json

API_URL = "http://localhost:20128/v1/chat/completions"


def create_plan(task, screen_state):
    data = {
        "model": "my-combo",
        "messages": [
            {
                "role": "user",
                "content": f"""
You are a computer task planner.

User task:
{task}

Current screen state:
{json.dumps(screen_state)}

Create a simple step-by-step plan to accomplish the user's task.

Return JSON with:
- goal
- steps

Each step should be a short action or reasoning step.
Do not perform any actions.
"""
            }
        ],
        "stream": False
    }

    response = requests.post(API_URL, json=data)

    result = response.json()

    content = result["choices"][0]["message"]["content"]

    content = content.replace("```json", "").replace("```", "").strip()

    start = content.find("{")
    end = content.rfind("}") + 1

    content = content[start:end]


    return json.loads(content)


if __name__ == "__main__":
    screen_state = {
        "application": "VS Code",
        "active_file": "main.py",
        "current_state": "Python script has an error",
        "visible_elements": ["Python editor", "terminal"]
    }

    result = create_plan(
        "Fix the error in my Python program",
        screen_state
    )

    print(result)