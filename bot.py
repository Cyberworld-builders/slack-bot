import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# if environment variable is not set, read .env file
if os.environ.get("SLACK_BOT_TOKEN") is None:
    from dotenv import load_dotenv
    load_dotenv()

# Initialize the Slack app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# Handle the 'app_mention' event (when the bot is mentioned)
@app.event("app_mention")
def handle_mention(event, say):
    # Check if the message contains "hello"
    if "hello" in event["text"].lower():
        # Respond in the same channel
        say(f"Hello <@{event['user']}>! How can I assist you today?")

# Start the bot
if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN"))
    handler.start()