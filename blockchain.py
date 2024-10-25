from transaction import Transaction
import time
from block import Block

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.reward = 50
        self.halving_interval = 1000000
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), [])

    def add_block(self, new_block):
        new_block.previous_hash = self.get_previous_hash()
        self.chain.append(new_block)
        self.check_halving()

    def mine_block_scrypt(self):
        batch_size = 10
        transactions = []
        for i in range(batch_size):
            transaction = Transaction("sender", "recipient", 10)
            transactions.append(transaction)
        self.mine_block_scrypt_batch(transactions)

    def mine_block_scrypt_batch(self, transactions):
        new_block = Block(len(self.chain), self.get_previous_hash(), int(time.time()), transactions)
        new_block.mine_block_scrypt(self.difficulty)
        self.add_block(new_block)

    def get_previous_hash(self):
        return self.chain[-1].hash

    def check_halving(self):
        if len(self.chain) % self.halving_interval == 0:
            self.halve_reward()

    def halve_reward(self):
        self.reward /= 2