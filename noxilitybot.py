import discord
from discord.ext import commands

TOKEN = 'NTE4ODczMzIxMDg1ODYxOTE4.DuXKKQ.E3PdxHY5V0S5bibs5kqnUkefNbs'

client = commands.Bot(command_prefix = '?')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='www.noxility.com'))
    print('Bot has been Deployed.')

@client.command(pass_context=True)
async def embed(ctx, *, msg):
    embed = discord.Embed(colour=discord.Colour.gold(),description=msg)
    embed.set_author(name='Message by {}'.format(ctx.message.author), icon_url=ctx.message.author.avatar_url),
    await client.delete_message(ctx.message)
    await client.say(embed=embed)

client.run(TOKEN)