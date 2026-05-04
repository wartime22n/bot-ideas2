import discord, random, os, requests
from discord.ext import commands
import emoji

liste = {
    "cam": 4000,
    "strafor": 5000,
    "sise": 400,
    "pil": 300,
    "sakiz": 50,
    "kagit": 5
}
@bot.command()
async def rastgele(ctx):
    her = random.choice(list(liste))
    await ctx.send(f'{her} nin sogrulma suresi {liste[her]} yildir')
    img_name2 = random.choice(os.listdir('recyle'))
    with open(f'recyle/{img_name2}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send('Did this help you?')
    @bot.command()
    async def no(ctx):
        await ctx.send(emoji.emojize('i am sad hear that :disappointed_face:'))
    @bot.command()
    async def yes(ctx):
        await ctx.send(emoji.emojize('i am glad to hear that! :smiling_face_with_smiling_eyes:'))
