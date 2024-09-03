> WARNING
> 
> Deta Space is shutting down
>
> https://deta.space/sunset
> 

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
7. Return to Develop - Overview tab and click on `Open Builder Instance` button. There will be information about your bot's webhook, if it is set up correctly.
8. Send `/start` to your bot and check that it responds

## Features

### Logging of errors and events to Deta Base

To enable logging of errors and events, set `ENABLE_ERRORS_LOGS` and `ENABLE_EVENTS_LOGS` environment variables to `True` in Develop - Configuration tab. Logs will be stored in `logs` tables. 
Additionally, you can set `ERROR_LOGS_EXPIRE_AFTER` and `EVENTS_LOGS_EXPIRE_AFTER` environment variables to set expiration time for logs in seconds. By default, logs will be stored forever.

### Preset CallbackAnswer middleware

CallbackAnswer middleware is used to automatically answer on all callback queries, so you don't need to do it manually. 

### Automatic webhook setup

The bot automatically sets webhook on startup.

### Page with webhook info

You can find webhook info on `/info` page. Root page redirects to `/info` page.

## Notes

You can find version tuned for my personal purposes in `personal-tuned` branch. I may have some additional features 
