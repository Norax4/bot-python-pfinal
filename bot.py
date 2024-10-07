import discord
import random
import requests
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

enlacesCC = ["https://www.un.org/es/climatechange/what-is-climate-change", "https://www.un.org/es/climatechange/science/causes-effects-climate-change", "https://www.enelgreenpower.com/es/learning-hub/transicion-energetica/cambio-climatico-causas-consecuencias", ]
enlacesIE = ["https://forodiplomatico.com/cinco-avances-tecnologicos-medioambiente/", "" ]
CCquestions = []
funfacts = []


@bot.event
async def on_ready():
    print (f" Se inició el bot {bot.user}")

@bot.command()
async def climatechange(ctx):
    await ctx.send(random.choice(enlacesCC))

@bot.command() 
async def electricinnovation(ctx):
    await ctx.send(random.choice(enlacesIE))

@bot.command()
async def funfacts(ctx):
    await ctx.send(random.choice(funfacts))

@bot.command()
async def questionaire(ctx):
    await ctx.send(random.choice(CCquestions))

    def check(m: discord.Message):  # m = discord.Message.
        return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id
    
    try:
        #              event = on_message without on_
        msg = await bot.wait_for('message', check = check, timeout = 60.0)
        # msg = discord.Message
    except asyncio.TimeoutError: 
        # at this point, the check didn't become True, let's handle it.
        await ctx.send(f"**{ctx.author}**, you didn't send any message that meets the check in this channel for 60 seconds..")
        return
    else:
        # at this point, the check has become True and the wait_for has done its work, now we can do ours.
        # we could also do things based on the message content here, like so
        # if msg.content == "this is cool":
        #    return await ctx.send("wait_for is indeed a cool method")
        
        await ctx.send(f"**{ctx.author}**, you responded with {msg.content}!")
        return

    


bot.run("token")