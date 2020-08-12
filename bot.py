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
    'pepechain' : '<a:aPES_PoggersChain:619920297750953989>',
    'pepescary' : '<a:PepeScary:731173526102605885>',
    'pepespin' : '<a:aPES_PogSpin:699598474143989830>',
    'mochiheart' : '<a:0MochiHeart:641898366996971520>',
    'peperain' : '<a:aPES_PeepoSadRain:718071523864477726>',
    'ezmoney' : '<a:aPES_MoneyRain:718071523524739074>',
    'pepelaugh' : '<a:aPES_LulLaugh:718071523013034125>',
    'monkawash' : '<a:aPES_FranticWash:690958321733337170>',
    'pepebonk' : '<a:aPES4_PaperBonk:733230501455986769>',
    'kittyplay' : '<a:0KittyPlay:700970912656392204>',
    'sharingan' : '<a:CH_Sharingan1A:730774327007379560> <a:CH_Sharingan1B:730774341339578388> <a:CH_Sharingan1C:730774350789214259> <a:CH_Sharingan1D:730774360704548875> '\
                    '<a:CH_Sharingan2A:730774405231411271> <a:CH_Sharingan2B:730774474340696124> <a:CH_Sharingan2C:730774502895779870> <a:CH_Sharingan2D:730774539335630858>' \
                    '<a:CH_Sharingan3A:730774563192832070> <a:CH_Sharingan3B:730774572252659813> <a:CH_Sharingan3C:730774586035011594> <a:CH_Sharingan3D:730774596667572334>' \
                    '<a:CH_Sharingan4A:730774610571952168> <a:CH_Sharingan4B:730774622169071627> <a:CH_Sharingan4C:730774711088316486> <a:CH_Sharingan4D:730774725688557658>' 

}

webhook_dict = {
    '🤫-secret' : os.environ['SECRET_CHANNEL'],
    '🏛-hidden-link' : os.environ['HIDDEN_LINK'],
    'minecraft-progression' : os.environ['MINECRAFT_PROGRESSION'],
}

client = discord.Client()

def create_help(emoji_dict):
    embed = discord.Embed(title='**Emoji Help**',description='[Github Source Code](https://github.com/jasonlohcy/discord_bot)')
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
        c = '{0.channel}'.format(message)
        if not c in webhook_dict:
            print(f'{message.channel} channel not supported')
        else:
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