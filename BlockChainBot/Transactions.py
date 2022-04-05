from datetime import datetime

'''
make transaction
store transaction
update transaction
str transaction

get transaction
'''

from replit import db # data base

#Storage Units
db['Sender'] = []
db['Receiver'] = []
db['Amount'] = []
db['IndexT'] = 0
db['DataT'] = []
db['DateT'] = []

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

    def Store(self):
      #Storing the Data, objects can't be stored
      db['Sender'].append(self.sender)
      db['Receiver'].append(self.receiver)
      db['Amount'].append(self.amount)
      db['DataT'].append(self.data)
      db['DateT'].append(self.date)

      db['IndexT'] = db['IndexT'] + 1

      #temp = str(db['IndexT']-1) + " " + 
      return db['IndexT']-1
    
    def Update(self,ID):
      db['Sender'][ID] = self.sender
      db['Receiver'][ID] = self.reveiver
      db['Amount'][ID] = self.amount
      db['DataT'][ID] = self.data
      db['DateT'][ID] = self.date

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
    
  return MyTransaction
        


if __name__ == "__main__":
    t1 = Transaction("ABC","XYZ",10.5)
    test = t1.__str__()
    print(test)
    t2 = Transaction("ABC1","XYZ1",-10.5)
    test = t2.__str__()
    print(test)