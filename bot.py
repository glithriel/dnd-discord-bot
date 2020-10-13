# bot.py
from discord.ext import commands
import os
import random
from dotenv import load_dotenv

# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()

# GRAB THE API TOKEN FROM THE .ENV FILE.
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

def roll(n, sides, bonus):
    rolls = []
    try:
        for _ in range(1, n+1):
            rolls.append(random.randint(1, sides) + int(bonus))
        maximum = (n * sides) + (n * bonus)
        return rolls, maximum
    except:
        return "Error"

@bot.command(name='mm')
async def magic_missle(ctx):
    """Cast Magic Missle"""
    damage, maximum = roll(3, 4, 1)
    total = sum(damage)
    message = (
    f'{ctx.author.display_name} casts Magic Missle at the darkness! \n'
    f'Your missles hit for {damage} causing {total} damage! \n'
    )
    if total == maximum:
        message = message + (f'{ctx.author.display_name} murdered the darkness!')
    await ctx.send(message)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}. (ID {bot.user.id})')
    print('------')

@bot.event
async def on_voice_state_update(member, before, after):
    """Greeting for members joining the voice channel"""
    greetings = [
    f"Yo! It's {member.display_name}!",
    f"{member.display_name} joins the fray!",
    f"{member.display_name} stands ready!",
    f"{member.display_name} is up in this bitch!"
    ]
    greeting = random.choice(greetings)
    if before.channel is None and after.channel is not None:
        for channel in member.guild.text_channels:
            if channel.name == 'general':
                await member.send(greeting)
    
bot.run(TOKEN)

