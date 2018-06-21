# !/usr/bin/env python
# _*_ coding:utf-8 _*_

import hashlib as hasher
import datetime as date

# 定义区块链
# 每个块链的索引位置 
# 时间戳 每个块链的数据 
# 上一个块链的哈希值
class Block(object):
	
	def __init__(self, index, timestamp, data, previous_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.hash_block()

	def hash_block(self):
		# 用sha256加密
		sha = hasher.sha256()
		sha.update(str(self.index).encode("utf-8")+str(self.timestamp).encode("utf-8")+str(self.data).encode("utf-8")+str(self.previous_hash).encode("utf-8"))
		# 双重加密 返回一个16进制的加密结果
		return sha.hexdigest()


# 创建一个起源块
def create_genesis_block(object):
	# 手动创建块链 索引为0或者任意先前块链的散列
	return Block(0,date.datetime.now(), 'Genesis', '0')


# 起源块后续块链以何种方式陆续创建
def next_block(last_block):
	this_index = last_block.index + 1
	this_timestamp = date.datetime.now()
	this_data = "hey i'm new Block [ " + str(this_index) + " ] "
	this_hash = last_block.hash
	return Block(this_index, this_timestamp, this_data, this_hash)


# 创建起源块
blockchain = [create_genesis_block(object)]
previous_block = blockchain[0]
# 在起源块之后添加多少块链
num_of_block_to_add = 20
# 添加块到列上
for i in range(0, num_of_block_to_add):
	block_to_add = next_block(previous_block)
	blockchain.append(block_to_add)
	previous_block = block_to_add
	print("Block # {} has been added to blockchain".format(block_to_add.index))
	print("hash :{}\n".format(block_to_add.hash))