import os
import discord
from googleapiclient import discovery
from mcstatus import MinecraftServer

client = discord.Client()
TOKEN = os.getenv('DISCORD_TOKEN')
IP = os.getenv('SERVER_IP')
compute = discovery.build('compute', 'v1')
server = MinecraftServer(IP, 25565)
project = 'minecraft-sisters'
zone = 'us-west1-b'
instance = 'minecraft-sisters'


def start_server(compute):
    print('starting VM instance....')
    result = compute.instances().start(
        project=project, zone=zone, instance=instance).execute()
    print('server started')


def stop_server(compute):
    print('stopping server....')
    result = compute.instances().stop(
        project=project, zone=zone, instance=instance).execute()
    print('server stopped.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!mcs start":
        await message.channel.send("starting minecraft server... should take a second")
        start_server(compute=compute)
        await message.channel.send("Server started :)")

    if message.content == "!mcs stop":
        stop_server(compute=compute)
        await message.channel.send(
            "shutting down server... please make sure it shuts down before leaving")

    if message.content == "!mcs status":
        status = server.query()
        await message.channel.send('online rn: {0}'.format(", ".join(status.players.names)))

client.run(TOKEN)
