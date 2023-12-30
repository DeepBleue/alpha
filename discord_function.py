import discord

async def send_discord_message(message,href,client,CHANNEL_ID):
    await client.wait_until_ready()  # Wait until the client is ready
    channel = client.get_channel(CHANNEL_ID)  # Replace with your channel ID
    if channel:
        try:
            await channel.send(message)
            await channel.send(href)
        except discord.DiscordException as e:
            print(f"An error occurred while sending a message: {e}")

    else:
        print("Channel not found or bot does not have access.")
