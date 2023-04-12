Telegram Bot template with [aiogram](https://github.com/aiogram/aiogram) for deployment on [Deta Space](https://deta.space/).

The bot has several useful features, including logging of errors and events to Deta Base, preset CallbackAnswer middleware and automatic webhook setup.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- A [Deta Space](https://deta.space/) account
- [Space CLI](https://deta.space/docs/en/basics/cli)
- A Telegram Bot token from [@BotFather](https://t.me/BotFather)
  
### Installation

1. Clone the repository: `git clone https://github.com/mamsdeveloper/AiogramDetaBot.git`
2. Go to cloned repo's folder
3. Run `space new` to create a new Space project
4. Run `space push` to deploy the code to Deta Space
5. Go to [Builder](https://deta.space/builder) and open builder instance of your project 
6. Set up your Telegram Bot token in Develop - Configuration tab
7. Return to Develop - Overview tab and click on `Open Builder Instance` button
8. Send `/start` to your bot and check that it responds

## Features

- Logging of errors and events to Deta Base (Can be disabled using `ENABLE_ERRORS_LOGS` and `ENABLE_EVENTS_LOGS` environment variables)
- Preset CallbackAnswer middleware
- Automatic webhook setup

## Notes

You can find version tuned for my personal purposes in `personal-tuned` branch. I may have some additional features 
