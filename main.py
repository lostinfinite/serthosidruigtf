import discord
from discord.ext import commands

intents = discord.Intents.default()
client = commands.Bot(command_prefix='', intents=intents)

# Add the guild ids in which the slash command will appear.
# If it should be in all, remove the argument, but note that
# it will take some time (up to an hour) to register the
# command if it's for all guilds.
@client.command(
    name="commandname",
    description="My first application Command",
)
async def first_command(ctx):
    await ctx.send("Hello!")

# Sync your commands to discord once the client is ready.
@client.event
async def on_ready():
    await client.sync_commands
    print("Ready!")

# Run your client.
client.run('MTE5MDM2MjUxODgyNTIyMjE5Ng.Gsv8Cx.q7cy0qQMGxGpG3XbAcbO3fjK3AHHLUzY0LMfBw')
