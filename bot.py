import discord
from discord import Webhook, RequestsWebhookAdapter
import os

TOKEN = os.environ['TOKEN']  
PREFIX = '.'

emoji_dict = {
    'shoot_tnt' : '<a:KaguyaPew_01s:697513110759800843> <a:KaguyaPew_02s:697513110206152744> '\
                    '<a:KaguyaPew_03s:697513110709469274> <a:KaguyaPew_04s:697513110118072422> <a:TNT_ignite:697513136357376002>',
    'grass_bounce' : '<a:grass_bounce:587505418406723584>',
    'fast_parrot' : '<a:fast_parrot:393622342581878785>',
    'PepeLazer' : '<a:0PepeLazerRee:701750592271417385>',
    'hype' : '<a:hype:726261952216825886>',
    'poggerschain' : '<a:aPES_PoggersChain:619920297750953989>',
    'pepescary' : '<a:PepeScary:731173526102605885>',
    'pogspin' : '<a:aPES_PogSpin:699598474143989830>',
}

webhook_dict = {
    '🤫-secret' : os.environ['SECRET_CHANNEL'],
    '🏛-hidden-link' : os.environ['HIDDEN_LINK'],
    'minecraft-progression' : os.environ['MINECRAFT_PROGRESSION'],
}

client = discord.Client()

def create_help(emoji_dict):
    embed = discord.Embed(title='**Emoji Help**')
    for key, value in emoji_dict.items():
        #emoji , command , inline=true
        embed.add_field(name=value,value=f'`{PREFIX}{key}`')
    return embed

def send_emoji(emoji, message):
    emote = emoji_dict[emoji]
    c = '{0.channel}'.format(message)
    if not c in webhook_dict:
        print(f'{message.channel} channel not supported')
        return
    else:
        webhook = Webhook.from_url(webhook_dict[c],adapter=RequestsWebhookAdapter())
        webhook.send(content=emote,username=message.author.display_name, avatar_url=message.author.avatar_url)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #could use discord.py ext command
    if not message.content.startswith(PREFIX):
        return

    if message.content.startswith(PREFIX + 'test'):
        print('author.name {0.author.name}, author.avatar_url {0.author.avatar_url}'.format(message))
        await message.channel.send('Hello!')
        c = '{0.channel}'.format(message)
        print(c)
    
    if message.content.startswith(PREFIX + 'help'):
        embed = create_help(emoji_dict)
        if not c in webhook_dict:
            print(f'{message.channel} channel not supported')
        else:
            c = '{0.channel}'.format(message)
            webhook = Webhook.from_url(webhook_dict[c],adapter=RequestsWebhookAdapter())
            webhook.send(embed=embed)
            return

    if message.content[1:] in emoji_dict:
        await message.delete()
        send_emoji(message.content[1:],message) 
        return

    if message.content.lower() ==  PREFIX+'logout':
        await client.close()


client.run(TOKEN)