import discord, random, os, requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(name='bot')
async def _bot(ctx):
    await ctx.send('Yes, the bot is coool.')


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    if img_name == "mem4.jpg":
        if random.randint(0, 1) == 0:
            await ctx.send('destroyed')
            img_name = "mem6.png"
    with open(f'images/{img_name}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

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

@bot.command("duck")
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("")
