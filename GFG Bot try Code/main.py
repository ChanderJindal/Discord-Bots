from discord.ext import commands
import asyncio
import discord
from deep_translator import GoogleTranslator
bot = commands.Bot(command_prefix='!', case_insensitive=True)
Yeah = ["y","ye","yes","Okay","k","kay","true","t","true",'enable', 'on']
Nah = ["n","no","f","false",'disable', 'off']
def Translate(msg,to_lang = 'hi'):
  return GoogleTranslator(source='auto', target=to_lang).translate(msg)
@bot.event
async def on_ready():
  
    print('We can begin the Crafting as {0.user}'.format(bot))

    bot.DelMsg = True
    #Auto Delete Messages field added

@bot.event
async def on_message(message):
  
  await bot.process_commands(message)

@bot.command()
async def Hey(ctx):
  if bot.DelMsg: #If Auto Delete Message is enabled it will delete the Trigger message
    await ctx.message.delete()
    await ctx.send("The Trigger Message has been deleted")
  await ctx.send("Hey there! I am GFG Bot!")

@bot.command()   
async def say(ctx,arg1,arg2):
  if bot.DelMsg: 
    await ctx.message.delete()
    await ctx.send("The Trigger Message has been deleted")
  arg = arg1 + " " + arg2
  await ctx.send(arg)

@bot.command()   
async def echo(ctx,*,arg):
  if bot.DelMsg: 
    await ctx.message.delete()
    await ctx.send("The Trigger Message has been deleted")
  await ctx.send(arg)
    
@bot.command()
async def autodelmessage(ctx,arg):
  arg = arg.lower()
  msg = "Invaild Input!\n`$autodelmessage <True/False>`"
  #temp = bot.DelMsg
  if arg in Yeah:
    bot.DelMsg = True
    msg = "Auto Delete Command Message is On"
  elif arg in Nah:
    bot.DelMsg = False
    msg = "Auto Delete Command Message is Off"

  if bot.DelMsg == True:
    await ctx.message.delete()
  #bot.DelMsg = temp
  await ctx.send(msg)

@bot.command()
async def Reminder(ctx , time, *, reminder):
  if bot.DelMsg:
    await ctx.message.delete()
    await ctx.send("The Trigger Message has been deleted")
    seconds = 0
    if time.lower().endswith("d"):
        seconds += int(time[:-1]) * 60 * 60 * 24
        counter = f"{seconds // 60 // 60 // 24} days"
    if time.lower().endswith("h"):
        seconds += int(time[:-1]) * 60 * 60
        counter = f"{seconds // 60 // 60} hours"
    elif time.lower().endswith("m"):
        seconds += int(time[:-1]) * 60
        counter = f"{seconds // 60} minutes"
    elif time.lower().endswith("s"):
        seconds += int(time[:-1])
        counter = f"{seconds} seconds"
    if seconds == 0:
      await ctx.send("Hey {ctx.author.mention} this is the Reminder about `{reminder}`")
      return 
    else:
        await ctx.send(f"Reminder about {reminder} set in {counter}.")
        await asyncio.sleep(seconds)
        await ctx.send(f"Hi {ctx.author.mention}, you asked me to remind you about {reminder} {counter} ago.")
        return

import os
bot.run(os.getenv('TOKEN'))
