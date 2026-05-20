import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='0')

    def create_block(self, data=None, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'data': data,
            'previous_hash': previous_hash or self.get_last_block()['hash']
        }

        block['hash'] = self.hash(block)
        self.chain.append(block)
        return block

    def get_last_block(self):
        return self.chain[-1]

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current['previous_hash'] != previous['hash']:
                return False

            if current['hash'] != self.hash(current):
                return False

        return True