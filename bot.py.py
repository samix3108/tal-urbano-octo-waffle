import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('On-line', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'oi':
            await message.channel.send('Ola :)')

client = MyClient()
client.run('seu token')