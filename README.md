# OSRS Cow Farming Bot

A Python-based bot for Old School RuneScape (OSRS) that uses computer vision and confidence factors to automate cow farming tasks. The bot identifies cows on the screen using image recognition and interacts with them using mouse clicks.

## Features

- **Image Recognition**: Uses `pyautogui` to locate cows on the screen based on images in the `photos` folder.
- **Configurable Confidence**: Adjustable confidence level for image matching.
- **Keyboard Controls**:
  - **Start/Stop**: Press `A` to toggle the bot on or off.
  - **Exit**: Press `B` to stop the bot and exit the program.
- **Dynamic Image Loading**: Automatically loads all `.png` images from the `photos` folder.

## Requirements

- Python 3.8 or higher
- Required Python libraries:
  - `pyautogui`
  - `pynput`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/osrs-cow-farming-bot.git
   cd osrs-cow-farming-bot