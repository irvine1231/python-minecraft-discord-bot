import discord
import os
from dotenv import load_dotenv
from mcipc.query import Client

load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.content.startswith('!ip'):
            await message.channel.send('The IP is `' + os.getenv("MINECRAFT_HOST") + '`')

        if message.content.startswith('!state'):
            try:
                with Client(os.getenv("MINECRAFT_HOST"), int(os.getenv("MINECRAFT_PORT")), timeout=1.5) as client:
                    basic_stats = client.basic_stats
                    await message.channel.send(basic_stats.motd + ' is online! With ' + str(basic_stats.num_players) + ' out of ' + str(basic_stats.max_players) + ' players.')

            except:
                await message.channel.send('Server is offline!')

        if message.content.startswith('!list'):
            try:
                with Client(os.getenv("MINECRAFT_HOST"), int(os.getenv("MINECRAFT_PORT")), timeout=1.5) as client:
                    full_stats = client.full_stats
                    player_list_message = "Player list: \n"
                    for player_name in full_stats.players:
                        player_list_message = player_list_message + "- " + player_name + "\n"

                    await message.channel.send(player_list_message)

            except e:
                print(e)
                await message.channel.send('Server is offline!')


client = MyClient()
client.run(os.getenv("DISCORD_TOKEN"))
