import discord
import commands as C
from discord.ext import commands
import helper_commands as hp

Yeah = ["y","ye","yes","Okay","k","kay","true","t","true",'enable', 'on']
Nah = ["n","no","f","false",'disable', 'off']

bot = commands.Bot(command_prefix='$', case_insensitive=True)
#This is to check prefix, yes prefix can be changed using file system

@bot.event
async def on_ready():
    print('We can begin the Crafting as {0.user}'.format(bot))
    #this is what is shows when the bot is online

    bot.DelMsg = True

@bot.event#ping reply
async def on_message(message):#Only on_message can take in Messages
  if message.author.bot == bot.user: #it's not from this bot itself
    return
  if message.channel.id == 829814770453839895 and message.author == 'MEE6#4876': #Tweet Translate
    #Check that it's in Twitter Channel then, it's from MEE6
    embeds = message.embeds #rest is same as {getmsg}
    for e in embeds:
      var = e.to_dict()#make embed to dict
      try:#these 3 had text in jp in them, so if they are there then translate them
        var["footer"]["text"] = hp.Translate(var["footer"]["text"])
      except:pass
      try:
        var["author"]["name"] = hp.Translate(var["author"]["name"])
      except:pass
      try:
        var["description"] = hp.Translate(var["description"])
      except:pass
      await message.channel.send(embed=discord.Embed.from_dict(var))#change back dict to embed, and send it
  else:
    await bot.process_commands(message)#if none of above carry commands below

'''
@bot.event#ping reply
async def on_message(message):
  if message.author.bot == False and bot.user.mentioned_in(message) and len(message.content) == len(bot.user.mention)+1:
    await message.channel.send(f'Hello! I am the {bot.user.mention}!\nMy Prefix is $')
  await bot.process_commands(message)
'''
@bot.command()
async def prefix(ctx):
  if bot.DelMsg:await ctx.message.delete()
  await ctx.send('$')

@bot.command(name='hello',aliases=['hey','hola','hi'])
async def hello(ctx):
  if bot.DelMsg:await ctx.message.delete()
  await ctx.send(f'Hello!  {ctx.author.mention}')
  #reply to the {Prefix}Hello

@bot.command()
async def echo(ctx, *, arg):
  if bot.DelMsg:await ctx.message.delete()
  await ctx.send(arg)

@bot.command(name='anime',aliases=['A'])
async def anime(ctx):
  if bot.DelMsg:await ctx.message.delete()
  await ctx.send(embed = C.EpisodeUpdate())

@bot.command(name='manga',aliases=['M'])
async def manga(ctx):
  if bot.DelMsg:await ctx.message.delete()
  await ctx.send(embed = C.MangaUpdate())

@bot.command(name = 'autodelmessage',aliases = ['ADM'] )
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

@bot.command() #It takes in an embed message and translates it into english then returns it
async def getmsg(ctx, channel: discord.TextChannel, msgID: int):
  #you need to specify the channel from where the message is picked <#Channel.id> format then, message ID, 
  #PS:- The channel must be present in server
  msg = await channel.fetch_message(msgID)#got the message
  embeds = msg.embeds #embeded part
  for e in embeds:
    var = e.to_dict()# made it into a dict()

    try:var["footer"]["text"] = hp.Translate(var["footer"]["text"])
    except:pass
    try:var["author"]["name"] = hp.Translate(var["author"]["name"])
    except:pass
    try:var["description"] = hp.Translate(var["description"])
    except:pass
    await ctx.send(embed=discord.Embed.from_dict(var))

@bot.command()#just for testing
#this is same as {getmsg} but it only gives the dict() to see the stuff in message 
async def getmsgdict(ctx, channel: discord.TextChannel, msgID: int):
  msg = await channel.fetch_message(msgID)
  embeds = msg.embeds 
  for e in embeds:
    await ctx.send(e.to_dict())

@bot.command()#just for testing
#this is same as {getmsg} but it only gives the dict() to see the stuff in message 
async def chkauth(ctx, channel: discord.TextChannel, msgID: int):
  msg = await channel.fetch_message(msgID)
  await ctx.send(msg.author)

import os

tk = 'OTM4NDg3NDExODE2NjkzODQz.YfrAgw.Jic9wLLoiyzP1cQy0yBgKPPyZcI'#os.environ['TOKEN']

bot.run(tk)
