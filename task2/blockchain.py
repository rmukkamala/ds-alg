

import hashlib
import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
    
    def get_genesis_block(self):
        return Block(datetime.datetime.now(),'0','0')


    def calc_hash():
      sha = hashlib.sha256()
      hash_str = "We are going to encode this string of data!".encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()

    def add_block(self,):

#print(datetime.datetime.now())
#newBlockChain= Block()
# 
block_chain = [Block.get_genesis_block()]

print("The genesis block has been created.")
print("Hash: %s" % block_chain[0].hash)