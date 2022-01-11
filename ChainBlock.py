from Block import Block as B
import Transactions as T
import hashlib

class Block_Chain:

    def __init__(self):
        self.chain = []

    def LastBlock(self):
        return self.chain[-1]

    def addBlock(self,block):
        self.prev = self.LastBlock().hash
        self.chain.append(block)
        self.size += 1

    def Simple_Check(self): # a bit like proof of work 
        assert(self.chain[0].prev == "!")
        for i in range(1,len(self.chain)):
            if self.chain[i-1].hash != self.chain[i].prev or self.chain[i].hash != hashlib.sha256(  self.chain[i].data.encode() ).hexdigest() :
                return False
        return True
    
    def printer(self):
        for i in self.chain:
            i.printer()

def Block_Chain_Maker(Sender,Receiver,Amt,chain):
    chain.addBlock(B(chain.LastBlock().hash,T.Transaction(Sender,Receiver,Amt),chain.size)) 
    
if __name__ == "__main__":
    BC = Block_Chain()
    Block_Chain_Maker("ABC","BCD",234,BC)
    Block_Chain_Maker("CDE","DEF",3,BC)
    Block_Chain_Maker("EFG","FGH",43,BC)
    Block_Chain_Maker("GHI","HIJ",67,BC)
    print(BC.Simple_Check())
    BC.printer()