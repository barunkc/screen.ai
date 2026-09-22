# screen.ai

An experimental AI computer assistant that can see, understand, and eventually interact with your screen.

## What it does

screen.ai captures the screen, uses a vision model to understand what is happening, and generates a structured plan based on the current screen and a task.

Screen → Vision → Screen State → Planner → Plan

## Current Features

- Screen capture
- Vision-based screen understanding
- Structured screen state
- AI task planning
- Global hotkey activation

## Current Activation

Press `Alt + [` to activate screen.ai.

The current pipeline:

1. Capture the screen
2. Send the screenshot to the vision model
3. Extract the screen state
4. Pass the screen state and task to the planner
5. Generate a structured plan

## Tech Stack

- Python
- MSS — screen capture
- Requests — API communication
- Vision-language model
- Local OpenAI-compatible API

## Project Structure

screen.ai/
├── src/
│   ├── ai.py
│   ├── capture.py
│   ├── hotkey.py
│   ├── main.py
│   └── planner.py
├── requirements.txt
├── README.md
└── .gitignore

## Current Status

Early working prototype.

The perception and planning pipeline is working. The project currently focuses on building the AI's ability to observe and reason about a computer screen before adding the ability to interact with it.

## Roadmap

- [x] Screen perception
- [x] Structured screen state
- [x] AI task planning
- [ ] User-provided tasks
- [ ] Computer interaction
- [ ] Observe → Plan → Act → Observe loop
- [ ] Memory and context
- [ ] Better screen understanding
- [ ] Explore custom/fine-tuned AI models