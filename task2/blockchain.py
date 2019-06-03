####Block Chain###

import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
      self.index= index
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      
    def calc_hash(self):
      sha = hashlib.sha256()
      hash_str = (str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()

##To crete the next block
def create_next_block(lastblock,data):
  index=lastblock.index + 1
  prev_hash=lastblock.hash
  return Block(index,datetime.datetime.now(),data,prev_hash)
  
##To display/visualize the exisiting Block chain 
def display_blockchain(blockchain=None):
  if blockchain is None:
    print("Missing parameter: Please enter the blockchain object param !")
    return None
  if len(blockchain)==0:
    print("The block chain given is empty. There is no genesis/head block !")
    return None
  for i in range(0, len(blockchain)):
    text=[ "Block: " + str(blockchain[i].index), str(blockchain[i].timestamp), str(blockchain[i].data), str(blockchain[i].hash)]
    maxlen=max( len(s) for s in text)
    colwidth= maxlen + 2
    print('+' + '-'*colwidth + '+')
    for s in text:
      print('| %-*.*s |' % (maxlen,maxlen,s))
    print('+' + '-'*colwidth + '+')
    print('            |')

#To initialize/create the first/genesis block
def create_genesis_block():
  return Block(0,datetime.datetime.now(),'This is Genesis Block','0')


#creating list of all the chained blocks
##Test Case 1
block_chain = [ create_genesis_block() ]

block_chain.append(create_next_block(block_chain[-1],'This is awesome'))
block_chain.append(create_next_block(block_chain[-1],'This is bad'))
block_chain.append(create_next_block(block_chain[-1],'This is great'))
block_chain.append(create_next_block(block_chain[-1],'This is superb'))
block_chain.append(create_next_block(block_chain[-1],'This is the best'))
##display
display_blockchain(block_chain)


##Test Case 2
print("#########Test Case 2 #############")
block_chain2 = [ ]
##display
display_blockchain(block_chain2)


##Test Case 3
print("#########Test Case 3 #############")
block_chain3 = [ create_genesis_block() ]
# block_chain2.append(create_next_block(block_chain[-1],'This is awesome'))
# block_chain2.append(create_next_block(block_chain[-1],'This is bad'))
##display
display_blockchain()

##Test Case4
##check if the previous hash of a block is equal to the hash of the block behind it
print("#########Test Case 4 #############")
if block_chain[-1].previous_hash==block_chain[-2].hash:  #refering to the data in first test case
  print("Test Passed ! Previous hash of a block is equal to the hash of the block behind it")
  print(f"Preveious hash of the current block is: {block_chain[-1].previous_hash}")
  print(f"Hash of the previous block is: {block_chain[-2].hash}")
else:
  print("Test Fail !")