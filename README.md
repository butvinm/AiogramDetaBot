Telegram Bot template with [aiogram](https://github.com/aiogram/aiogram) for deployment on [Deta Space](https://deta.space/)

## Getting Started

### Prerequisites

- Python 3.9 or higher
- A [Deta Space](https://deta.space/) account
- A Telegram Bot token from [@BotFather](https://t.me/BotFather)
  
### Installation

1. Clone the repository
2. Install [Space CLI](https://deta.space/docs/en/basics/cli)
3. Run `space new` to link code with a new Space project
4. Run `space deploy` to deploy the code to Deta Space
5. Go to [Builder](https://deta.space/builder) and open builder instance of your project 
6. Set up environment variables in Configuration section
7. Click on `Open Builder Instance` button in Overview section and copy the URL of the builder instance
8. Set telegram webhook 

```bash
curl -X POST https://api.telegram.org/bot<BOT_TOKEN>/setWebhook 
    -H "Content-Type: application/json" 
    -d '{"url": "https://<builder instance url>/webhook", "secret_token": "<WEBHOOK_SECRET>"}'
```

9. Send `/start` to your bot and check that it responds


## Features

- Logging of errors and events to Deta Base (Can be disabled using `ENABLE_ERRORS_LOGS` and `ENABLE_EVENTS_LOGS` environment variables)
- Preset CallbackAnswer middleware
- CallbackMessageMiddleware that inject `message` object into callback handler data 