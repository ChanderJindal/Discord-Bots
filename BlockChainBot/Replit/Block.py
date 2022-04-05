import Transactions as T
import hashlib
from datetime import datetime

'''
Make Block
Store Block
Update Block
make Str of Block 
Print Block

Get Block
Mine Block 
Check Block
'''

from replit import db # data base
if 'PreviousHash' not in db.keys():
  db['PreviousHash'] = []
if 'TID' not in db.keys():
  db['TID'] = []
if 'DateB' not in db.keys():
  db['DateB'] = []
if 'Hash' not in db.keys():
  db['Hash'] = []
if 'Nonse' not in db.keys():
  db['Nonse'] = []
if 'IndexB' not in db.keys():
  db['IndexB'] = 0 # <- ID for Block
if 'IndexChain' not in db.keys():
  db['IndexChain'] = 0

def TotalBlocks():
  return db['IndexB']

class Block:
    def __init__(self,prev,tid) -> None:
        self.prev = prev 
        self.transaction = tid
        self.date = str(datetime.now())
        self.nonse = 0
        self.hash = hashlib.sha256(str(self).encode()).hexdigest()


    def Store(self):
      #Storing the data
      db['PreviousHash'].append(self.prev)
      db['TID'].append(self.transaction)
      db['DateB'].append(self.date)
      db['Hash'].append(self.hash)
      db['Nonse'].append(self.nonse)

      db['IndexB'] = db['IndexB'] + 1
      return db['IndexB'] - 1, hashlib.sha256(str(self).encode() ).hexdigest()


    def UpdateBlock(self,ID):
      ID = int(ID)
      if ID < db['IndexB']:
        db['PreviousHash'][ID] = self.prev
        db['TID'][ID] = self.tid
        db['DateB'] [ID] = self.date
        db['Hash'][ID] = self.hash
        db['Nonse'][ID] = self.nonse


    def __str__(self):
      return "#" + str(db['IndexB']) +" with ID " + str(self.transaction)  + " and Code " + str(self.prev) + " is made on " + str(self.date) + " with special value of " + str(self.nonse)
    

    def printer(self):
      print(T.GetObject(self.transaction))        
      print("The Previous Hash is: ",self.prev,'\n',"The Current Hash is: ", self.hash,'\n',"The ",self.index," Block was gotten on Date: ", self.date,sep="",end="\n\n")



def GetBlock(ID):
  ID = int(ID)
  MyBlock = Block("!",0)
  if ID < db['IndexB'] or ID == 0:
    #Block ID too large
    MyBlock.prev = db['PreviousHash'][ID]
    MyBlock.tid = db['TID'][ID]
    MyBlock.date = db['DateB'] [ID]
    MyBlock.hash = db['Hash'][ID]
    MyBlock.nonse = db['Nonse'][ID]
  return MyBlock
'''
def GetPrevHash(ID):
  try:
    ID = int(ID)
  except:
    return -1
  if ID == 0:
    return "!"
  if ID > 0:
    return db['PreviousHash'][ID]
  return -1
'''
def PoolSize():
  return db['IndexB'] - db['IndexChain']

def GetCurrHash(ID):
  if ID > -1 and ID < db['IndexB']:
    return db['Hash'][ID]
  return -1


def MineBlock(difficulty,ID):

  ID = int(ID)
  if ID >= db['IndexB']:
    return "This Block doesn't exist in the Pool of Blocks." #no block in pool

  if ID < db['IndexChain']:
    return "This Block is already Mined." #Block is already mined


  if ID != 0 and CheckBlock(ID-1,difficulty) is False:
    return "There are previous Unmined Boxes!"
  

  #Mining the Block
  MyBlock = GetBlock(ID)
  Prefix = "0"*difficulty
  while str(MyBlock.hash)[:difficulty] != Prefix:
    #may need to add a limit here, if takes too long
    MyBlock.nonse = MyBlock.nonse + 1
    MyBlock.hash = hashlib.sha256(str(MyBlock).encode() ).hexdigest()
    
  #either got it, or it failed
  db['Nonse'][ID] = MyBlock.nonse
  db['Hash'][ID] = MyBlock.hash
  if str(MyBlock.hash).startswith("0"*difficulty):
    db['IndexChain'] = db['IndexChain'] + 1
    return db['IndexChain'] - 1
  return "Mining Failed"



def CheckBlock(ID,difficulty):
  ID = int(ID)

  MyBlock = GetBlock(ID) #get Block

  if ID == 0:
    if MyBlock.prev != "!": #for 1st Block only
      return False
  else: #not 1st block
    if MyBlock.prev != db['Hash'][ID-1]: #Prev hash didn't matched
      return False

  if MyBlock.hash != hashlib.sha256(str(MyBlock).encode()).hexdigest(): #current Hash Check
    return False

  if str(MyBlock.hash).startswith("0"*difficulty):
     #First difficulty numbers are Zero
    return True
  return False

def Vodka_reset():
  db['PreviousHash'] = []
  db['TID'] = []
  db['DateB'] = []
  db['Hash'] = []
  db['Nonse'] = []
  db['IndexB'] = 0 
  db['IndexChain'] = 0

      
if __name__ == "__main__":
    B1 = Block("None",0)
    B1.printer()
    print(B1.__str__())