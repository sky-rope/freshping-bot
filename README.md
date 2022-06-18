# freshping-bot
Telegram bot for sending alerts from Freshping

## Usage
1. Create Telegram bot with [BotFather](https://t.me/BotFather), it will return your API token.
2. Create a channel in telegram and name it whatever you like.
3. Invite @BotFather to that channel as admin
4. Type at least one message and get your Chat ID
```
https://api.telegram.org/bot<YOUR API TOKEN FROM ABOVE>/getUpdates

{"ok":true,"result":[{"update_id":642281183,
"channel_post":{"message_id":4,"sender_chat":{"id":<YOUR CHAT ID>,"title":"alerts","type":"channel"},"chat":{"id":<YOUR CHAT ID>,"title":"alerts","type":"channel"},"date":1653577465,"text":"Test"}}]}
```
5. Specify bot token and chat id in application settings as environment variables in docker-compose:
```
    environment:
      TELEGRAM_BOT_TOKEN: "YOUR_BOT_TOKEN"
      TELEGRAM_CHAT_ID: "TELEGRAM_CHAT_ID"
```

6. Expose application on publicly available URL. You can use Nginx as a reverse proxy with basic HTTP authorization.
7. Configure Webhook Integration on the Freshping side, and pass your application URL and auth credentials.