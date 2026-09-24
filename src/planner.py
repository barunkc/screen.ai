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

Each step must contain:
- action
- target

The action must be one of:
- move_mouse
- click
- type
- press_key
- hotkey
- ask_user

The target must contain only the value needed to execute the action.
Do not include explanations or descriptions in the target.

Examples:
- hotkey → "ctrl+shift+`"
- press_key → "enter"
- type → "hello world"
- click → "Start button"
- move_mouse → "500,300"

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

    print("Parsed plan:")
    print(content)

    return json.loads(content)