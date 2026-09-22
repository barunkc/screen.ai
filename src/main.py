import base64
import json

from capture import capture_screen
from ai import ask_ai
from planner import create_plan


def process_screen():
    photo = capture_screen()
    encoded_photo = base64.b64encode(photo).decode("utf-8")

    result = ask_ai(
        """Analyze the screen and return JSON with:
- application
- active_file
- visible_elements
- current_state
Keep each value concise.""",
        encoded_photo
    )

    content = result["choices"][0]["message"]["content"]

    content = content.replace("```json", "").replace("```", "").strip()

    screen_state = json.loads(content)

    print("Application:", screen_state["application"])
    print("Active file:", screen_state["active_file"])
    print("Current state:", screen_state["current_state"])
    print("Visible elements:", screen_state["visible_elements"])

    task = "Fix the error in my Python program"

    plan = create_plan(task, screen_state)

    print("\nGoal:", plan["goal"])

    print("Plan:")
    for step in plan["steps"]:
        print(f"{step['step']}. {step['action']}")