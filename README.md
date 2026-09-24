# screen.ai

An experimental AI computer assistant that can see, understand, plan, and interact with your screen.

## What it does

screen.ai captures the screen, uses a vision model to understand what is happening, generates a structured plan for a user-provided task, and executes the plan through computer-control actions.

**Screen → Vision → Screen State → Planner → Plan → Act**

## Current Features

* Screen capture
* Vision-based screen understanding
* Structured screen state
* AI task planning
* User-provided tasks
* Global hotkey activation
* Computer interaction
* Multi-step AI-generated action execution
* Keyboard and mouse control

## Current Activation

Press `Alt + [` to activate screen.ai.

The current pipeline:

1. Capture the screen
2. Send the screenshot to the vision model
3. Extract the screen state
4. Ask the planner to create a structured plan
5. Parse the generated plan
6. Execute each action in sequence

## Example

A task such as:

```text
type hello world in a new terminal
```

can produce a plan like:

```json
{
  "goal": "Type hello world in a new terminal",
  "steps": [
    {
      "action": "hotkey",
      "target": "ctrl+shift+`"
    },
    {
      "action": "type",
      "target": "hello world"
    },
    {
      "action": "press_key",
      "target": "enter"
    }
  ]
}
```

screen.ai then executes the steps sequentially.

## Tech Stack

* Python
* MSS — screen capture
* PyAutoGUI — computer interaction
* Keyboard — global hotkey activation
* Requests — API communication
* Vision-language model
* Local OpenAI-compatible API

## Project Structure

```text
screen.ai/
├── src/
│   ├── ai.py
│   ├── act.py
│   ├── capture.py
│   ├── hotkey.py
│   ├── main.py
│   └── planner.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Current Status

Early working prototype.

The perception, planning, and basic computer-interaction pipeline is working. screen.ai can understand the current screen, generate a multi-step plan from a user task, and execute keyboard and mouse actions.

The next major stage is making the agent observe the computer after each action and verify that the expected result occurred.

## Roadmap

* [x] Screen perception
* [x] Structured screen state
* [x] AI task planning
* [x] User-provided tasks
* [x] Computer interaction
* [x] Multi-step action execution
* [ ] Action verification
* [ ] Observe → Plan → Act → Observe loop
* [ ] Error detection and recovery
* [ ] Semantic screen target resolution
* [ ] Memory and context
* [ ] Better screen understanding
* [ ] Explore custom/fine-tuned AI models
