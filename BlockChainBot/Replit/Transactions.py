from datetime import datetime
from replit import db # data base
import hashlib

'''
make transaction
store transaction
update transaction
str transaction

get transaction
'''

#Storage Units
if 'Sender' not in db.keys():
  db['Sender'] = []
if 'Receiver' not in db.keys():
  db['Receiver'] = []
if 'Amount' not in db.keys():
  db['Amount'] = []
if 'IndexT' not in db.keys():
  db['IndexT'] = 0
if 'DataT' not in db.keys():
  db['DataT'] = []
if 'DateT' not in db.keys():
  db['DateT'] = []
if 'HashT' not in db.keys():
  db['HashT'] = []

def TotalTransactions():
  return db['IndexT']

class Transaction:
    def __init__(self,sender,receiver,amount):
      amount = float(amount)
      # print(type(amount))
      # print(amount < 0.0)
      if amount < 0.0:
          self.sender = receiver
          self.receiver = sender
          self.amount = -amount
      else:
          self.sender = sender
          self.receiver = receiver
          self.amount = amount
      self.data = str(self.sender) + " -> " +str(self.amount) + " -> " + str(self.receiver) 
      self.date = str(datetime.now())
      self.hash = hashlib.sha256(str(self).encode()).hexdigest()

    def Store(self):
      #Storing the Data, objects can't be stored
      db['Sender'].append(self.sender)
      db['Receiver'].append(self.receiver)
      db['Amount'].append(self.amount)
      db['DataT'].append(self.data)
      db['DateT'].append(self.date)
      #return item
      t = (db['IndexT'] ,hashlib.sha256(str(self).encode()).hexdigest())
      
      db['HashT'].append(t[1])

      db['IndexT'] = db['IndexT'] + 1

      #temp = str(db['IndexT']-1) + " " + 
      return t
    
    def Update(self,ID):
      db['Sender'][ID] = self.sender
      db['Receiver'][ID] = self.reveiver
      db['Amount'][ID] = self.amount
      db['DataT'][ID] = self.data
      db['DateT'][ID] = self.date
      db['HashT'][ID] = hashlib.sha256(str(self).encode()).hexdigest()

    def __str__(self):
        return "The transaction of ***" + self.data + "*** took place on " + str(self.date);

def GetTransaction(ID):
  MyTransaction = Transaction("Kaito","Kid",1412)
  if isinstance(ID,int) and ID < db['IndexT']:
    MyTransaction.sender = db['SenderT'][ID]
    MyTransaction.reveiver = db['ReveiverT'][ID]
    MyTransaction.amount = db['AmountT'][ID]
    MyTransaction.index = db['IndexT'][ID]
    MyTransaction.data = db['DataT'][ID]
    MyTransaction.date = db['DateT'][ID]
    MyTransaction.hash = db['HashT'][ID]
    
  return MyTransaction

def Vodka_Reset():
  db['Sender'] = []
  db['Receiver'] = []
  db['Amount'] = []
  db['IndexT'] = 0
  db['DataT'] = []
  db['DateT'] = []

def DeleteTransaction(ID):
  if ID >= db['IndexT']:
    return
  del db['Sender'][ID]
  del db['Receiver'][ID] 
  del db['Amount'][ID]
  del db['DataT'][ID]
  del db['DateT'][ID]
  db['IndexT'] = db['IndexT'] -1



if __name__ == "__main__":
    t1 = Transaction("ABC","XYZ",10.5)
    test = t1.__str__()
    print(test)
    t2 = Transaction("ABC1","XYZ1",-10.5)
    test = t2.__str__()
    print(test)