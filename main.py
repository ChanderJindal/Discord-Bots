import discord # allows to work with discord
import os # for files
import requests # to message on discord
import json # file format
from replit import db # data base
from Keep_it_Alive import keep_online

#Block Chain files
import Transactions as T
import Block as B

# initial Prefix
if "Prefix" not in db.keys():
    db["Prefix"] = "pls"

Transfer = ["give","gives","send","sent","gift","gifted","transfer","transfered"]
Make = ["make","create","generate"]
Yes = ["y","ye","yes","yea","yeah","k","ok","okay","kay"]

client = discord.Client() # to connect to discord

@client.event
async def on_ready():
    print('Ready here {0.user}'.format(client))
    # just to see that it's online

@client.event
async def on_message(message): 
  # reads all messages

  #If commnad from bot it self no reply
  if message.author == client.user: 
      return

  text = message.content.lower().split()
  #set to lower so, doesn't miss-match
  
  if text[0] == "echo":
    # a basic command for testing
    text[0] = ''
    temp = " ".join(text)
    await message.channel.send(temp)
    return

  MyPrefix = str(db["Prefix"])
  #Picked up a prefix

  if text[0] == "prefix":
    # to see the current prefix
    #await message.channel.send("MyPrefix")
    await message.channel.send(MyPrefix)
    return    

  if text[0] != MyPrefix:
    #check if it starts with Prefix
    return

  del text[0]
  # removed the prefix

  if text[0] == "setprefix":
    #await message.channel.send("setprefix")
    #setting new prefix
    MyPrefix = text[1]
    temp = "The New Prefix is " + str(MyPrefix)
    db["Prefix"] = MyPrefix
    await message.channel.send(temp)
    return

  if len(text) > 1:
    if text[1] in Transfer: 
      # Making a Transaction
      temp = "**Invalid Statement**\n> Format is `User1 gives User2 <Amount>`"
      # Format ^
      if len(text) < 4: 
        # to see there are enough elements there
        await message.channel.send(temp)
        return
      amount = 0.0
      try:
        amount = float(text[3]) 
        # number for amount
      except:
        await message.channel.send(temp)
        return
      if amount < 0:
        #No Negatives
        temp = "Invalid Amount!\n*Amount can't be negative.*"
        return
      # Format is correct
      MyTransaction = T.Transaction(text[0],text[2],amount)
      temp = "The Following Transaction has been made :- " +str(MyTransaction)
      #Transaction is made
      await message.channel.send(temp)
      temp = "Save the Transaction? (y/n)"
      await message.channel.send(temp)
      #To save it or not
      new_message = await client.wait_for('message')

      if new_message.content.lower() in Yes:
        #White List use only

        ID = MyTransaction.Store()
        #Got the Transaction ID
        temp = "The Transaction has been Stored.\nThe Transaction ID is `"+str(ID)+"`\n The corresponding Code is:-  **`"
        if ID != 0:
          temp = temp + str(B.GetPrevHash(ID)) + "`**"
        else:
          temp = temp + "!`**"
        #Previous Hash
        
        await new_message.channel.send(temp)
      else:
        temp = "The Transaction has been deleted."
        #Transaction Failed
        await new_message.channel.send(temp)
      del MyTransaction
      #For Space reasons + Not gonna need it
      return

#Making of a Block
  if len(text) > 1:
    if text[1] == "block" and text[0] in Make:
      if len(text) < 4:
        #see if all arguments are there
        temp = "Missing Arguments!\nFormat is :- `Make Block <int-ID> <hex-Code>`"
        await message.channel.send(temp)
        return

      Transaction_ID = 0
      try:
        Transaction_ID = int(text[2])
        # see if Transaction_ID is/can be int
      except:
        temp = "Invalid Format for Transaction_ID!\nFormat is :- `"+ MyPrefix + " Make Block <int-Transaction_ID> <hex-Code>`"
        await message.channel.send(temp)
        return

      OldHash = str(B.GetPrevHash(Transaction_ID))
      if OldHash != text[3]:
        #See that the Hash is correct
        temp = "Incorrect Value of Code"
        await message.channel.send(temp)
        return

      #Format is correct

      MyBlock = B.Block(OldHash,Transaction_ID)
      #made the block
      await message.channel.send(str(MyBlock))
      #sent the message that the block was made
      temp = "Save the Block? (y/n)"
      await message.channel.send(temp)
      #To save it or not
      new_message = await client.wait_for('message')

      if new_message.content.lower() in Yes:
        #green Light to save
        Block_ID = MyBlock.Store()
        Block_Hash = MyBlock.hash
        temp = "Block has been Saved.\nThe Block ID is:- `" + str(Block_ID) + "` and the Block Code **"+str(Block_Hash) + "**"
        await message.channel.send(temp)
      else:
        #Red Light to save
        temp = "The Block has been deleted."
      del MyBlock
      del Block_ID
      del Block_Hash
      return

  if text[0] == "poolsize":
    #no of blocks that can be mined
    temp = "`" + str(B.PoolSize()) + "`"
    await message.channel.send(temp)

#Mine Block

  if text[0] == "mine":
    #for mining the block
    if len(text) < 4:
      #to check if all arguments are there
      temp = "Argument Missing!\nFormat is :- `"+ MyPrefix + " Mine Block <Block_ID-int> <Block-Code>`"
      await message.channel.send(temp)
    
    if text[1] != "mine":
      #format check
      temp = "Invalid Argument!\nFormat is :- `"+ MyPrefix + " Mine Block <Block_ID-int> <Block-Code>`"
      await message.channel.send(temp)

    #Block ID is there
    Block_ID = 0
    try:
      Block_ID = int(Block_ID)
    except:
      temp = "Invalid Argument! Blcok ID invalid\nFormat is :- `"+ MyPrefix + " Mine Block <Block_ID-int> <Block-Code>`"
      await message.channel.send(temp)
      return

    #Code is there
    Block_Hash = B.GetCurrHash(Block_ID)
    if str(Block_Hash) != text[3]:
      temp = "Invalid Code"
      await message.channel.send(temp)
    
    #format is correct
    temp = "Wait! Message is correct, it might take a while to mine..."
    await message.channel.send(temp)
    Mined_Block_ID = B.MineBlock(3,Block_ID)
    Mined_Block = B.GetBlock(Mined_Block_ID)

    temp = "The Block has been Mined at difficulty Level of `3`!\nThe new code to Block is `" + str(Mined_Block.hash) + "`\nNow the Block is " + str(Mined_Block)

    await message.channel.send(temp)

    del Mined_Block
    del Mined_Block_ID
    return

  if text[0] == "totaltransactions":
    temp = T.TotalTransactions()
    await message.channel.send(str(temp))

  if text[0] == "check":
    if len(text) < 3:
      temp = "Missing Arguments!\nFormat :- `" + MyPrefix + " Check Block <Block_ID-int>`"
      await message.channel.send(temp)
      return

    if text[1] != "block":
      temp = "Missing Arguments!\nFormat :- `" + MyPrefix + " Check Block <Block_ID-int>`"
      await message.channel.send(temp)
      return
    
    Block_ID = 0
    try:
      Block_ID = int(text[2])
    except:
      temp = "Invalid Block_ID!\nFormat :- `" + MyPrefix + " Check Block <Block_ID-int>`"
      await message.channel.send(temp)
      return

    if B.CheckBlock(Block_ID,3) == True:
      temp = "Block `" + str(Block_ID) +"` is verified with difficulty level of " + "3"
    else:
      temp = "Block `" + Block_ID +"` is not verified with difficulty level of " + "3"
    await message.channel.send(temp)
    return 
    
    

    
  

    
    
    





    


      


      

      



        
client.run(os.getenv('PASS'))
 