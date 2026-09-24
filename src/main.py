import base64
import json
import time

from capture import capture_screen
from ai import ask_ai
from planner import create_plan
from act import hotkey, move_mouse, click, type_text, press_key


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

    task = input("\nWhat do you want me to do? ")

    plan = create_plan(task, screen_state)

    print("\nRAW PLAN:")
    print(plan)
    print("\nGoal:", plan["goal"])

    print("Plan:")
    for i, step in enumerate(plan["steps"], 1):
        print(f"{i}. {step}")

    for step in plan["steps"]:
        action = step["action"]
        target = step["target"]

        print(f"\nExecuting: {action} → {target}")

        if action == "hotkey":
            keys = target.split(" to ")[0].split("+")
            hotkey(*keys)

        elif action == "move_mouse":
            x, y = map(int, target.split(","))
            move_mouse(x, y)

        elif action == "click":
            click()

        elif action == "type":
            type_text(target)

        elif action == "press_key":
            press_key(target)

        elif action == "ask_user":
            input(f"Please perform the following action: {target}. Press Enter when done.")

        else:
            print(f"Unknown action: {action}")
        time.sleep(1)   