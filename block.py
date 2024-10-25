import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.transactions)
        return hashlib.sha256(data.encode()).hexdigest()

    def mine_block_scrypt(self, difficulty):
        nonce = 0
        while self.hash[:difficulty] != '0' * difficulty:
            nonce += 1
            data = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.transactions) + str(nonce)
            self.hash = hashlib.sha256(data.encode()).hexdigest()