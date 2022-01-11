import discord # allows to work with discord
import os # for files
import requests # to message on discord
import json # file format
from replit import db # data base
from Keep_it_Alive import keep_online

#Block Chain files
from Transactions import Transaction as T
from Block import Block as B
from ChainBlock import Block_Chain as BC

# Starter 
Tra = []
T1 = (T("Kaito","Kid",1412))
Tra.append(T1)
db["Transactions"] = Tra
Blo = []
B1 = B("!",db["Transactions"][0])
Blo.append(B1)
db["Blocks"] = Blo

MyBlockChain = BC()
BC.chain.append(db["Blocks"][0])
#First make it
db["BlockChain"] = MyBlockChain
#then add it

#Making Indexing for sequence and all
db["TransactionIndex"] = 1
db["BlockIndex"] = 1

#Transaction Part
def MakeTransaction(User1,User2,Ammount):
  MyTransaction = T(User1,User2,Ammount); # made transaction
  MyTransaction.index = db["TransactionIndex"] #indexed it
  db["TransactionIndex"] = db["TransactionIndex"] + 1 #increment
  db["Transactions"].append(MyTransaction) # added to list
  return MyTransaction.index #returned the ID

#Not Sure if needed
def DeleteTransaction(ID):
  ID = int(ID)
  del db["Transactions"][ID]
  return

#Just a Check
def ShowTransaction(ID):
  MyTransaction = db["Transactions"][ID]
  return MyTransaction.data

#Block part
def MakeBlock(Previous_Block,Transaction_ID,Block_Index):
  if Transaction_ID < db["TransactionIndex"]:# if it's possible
    MyBlock = B(Previous_Block,db["Transactions"]) #made the block[Transaction_ID],db["BlockIndex"])
    MyBlock.index = db["BlockIndex"] #indexed it
    MyBlock.info = str(MyBlock.index) + MyBlock.info
    db["BlockIndex"] = db["BlockIndex"] + 1 #increment 
    db["Blocks"].append(MyBlock)#added to list
    return MyBlock.index #return ID
  return "Invalid Transaction ID" #incorrect Transaction ID

#Still not sure if del can be used
def DeleteBlock(ID):
  ID = int(ID)
  if ID < db["BlockIndex"]:
    del db["Blocks"][ID]
  return

#check
def ShowBlock(ID):
  ID = int(ID)
  if ID < db["BlockIndex"]:
    MyBlock = db["Blocks"][ID]
    return MyBlock.info
  return "Invalid Block ID"
    
#Making Chain

def AddBlockToChain(ID):
  MyBlockChain = db["BlockChain"] 
  MyBlockChain.addBlock(db["Blocks"][ID])
  #MyBlockChain.append(db["Blocks"][ID])


  

#client = discord.Client() # to connect to bot

