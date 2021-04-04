import argparse
import math
class node:
	def __init__(self, value):
		self.value = value
		self.right = self
		self.left = self

	def __repr__(self):
		return 'Node{}'.format(self.value).strip()

class link:
	def __init__(self):
		self.num_element = 0
		self.root = node(None)
    
	def pop(self,node):
		flag = False
		node_test = self.root.right
		while node_test != self.root:
			if node_test.value == node.value:
				flag = True
				node = node_test
				break
			else:
				flag = False
				node_test = node_test.right
		if flag == False:
			return 'Error'
		elif self.num_element == 0:
			raise ValueError('Can not execute delete() on an empty link')
		else:
			if self.num_element == 1:
				self.root.left = self.root
				self.root.right = self.root
				self.num_element -= 1
			else:        
				temp = node.right
				node.left.right = temp
				temp.left = node.left
				self.num_element -= 1
				return flag
	def push(self, node):
		if self.num_element == 0:
			self.root.right = node
			node.left = self.root
			node.right = self.root
			self.root.left = node
			self.num_element += 1
		else:
			temp = self.root.right
			node.left = self.root
			node.right = temp
			temp.left = node
			self.root.right = node
			self.num_element += 1
	def search(self, node):
		flag = False
		node_test = self.root.right
		while node_test != self.root:
			if node_test.value == node.value:
				flag = True
				break
			else:
				flag = False
				node_test = node_test.right
		if flag == True:
			return 'Yes'
		else:
			return 'No'
	def __repr__(self):
		ret = ''
		node = self.root.right
		if self.num_element == 0:
			return 'None'
		while node != self.root:
			ret  = ret + '>>' + str(node)
			node = node.right
		return ret
class hash_table():
	# TODO
	def __init__(self):
		self.hashList = []
		for i in range(1001):
			ff = link()
			self.hashList.append(ff)
	def hash(self,n):
		key = 0
		length = len(n)
		for letter in n:
			string = letter.lower()
			number = ord(string) - 96
			key += math.pow(27, length - 1) * number
			length -= 1
			key = int(key % 1001)
		return key
	def insert(self, n, key):
		node_test = node(n)
		a = self.hashList[key]
		a.push(node_test)

	def look(self, key):
		a = self.hashList[key]
		if a.num_element == 0:
			return 'Null'
		else:
			return key
	def delete(self, n, key):
		node_test = node(n)
		a = self.hashList[key]
		flag = a.pop(node_test)
		if flag == 'Error':
			return flag
	def search(self, n, key):
		node_test = node(n)
		a = self.hashList[key]
		flag = a.search(node_test)
		return flag
	def end(self, output):
		output.close()
def main(input_path, output_path):
	table = hash_table()
	output = open(output_path, 'w')
	# TODO
	with open(input_path) as f:
		for line in f.readlines():
			line = line.split()
			command = line[0]
			if len(line) == 2:
				string = line[1]
				key = table.hash(string)
				if command[0] == 'I':
					table.insert(line[1], key)
					a = table.hashList[key]
				elif command[0] == 'D':
					flag = table.delete(line[1], key)
					if flag == 'Error':
						output.write(flag)
						output.write('\n') 
				elif command[0] == 'L':
					a = table.look(int(line[1]))
					if a == 'Null':
						output.write(a + '\n')
					else:
						b = table.hashList[int(line[1])]
						node_out = b.root.right
						while node_out != b.root:
							output.write(node_out.value)
							node_out = node_out.right
							if node_out != b.root:
								output.write(' ')
							else:
								output.write('\n')
				elif command[0] == 'S':
					flag = table.search(line[1], key)
					output.write(flag) 
					output.write('\n')    
				else:
					raise NotImplementedError
			elif command[0] == 'E':
				break
			else:
				raise NotImplementedError
	output.close()
if __name__ == '__main__':
	# DO NOT MODIFY CODES HERE
	# DO NOT MODIFY CODES HERE
	# DO NOT MODIFY CODES HERE
	# It's important and repeat three times
	parser = argparse.ArgumentParser()
	parser.add_argument('--input', default='./input')
	parser.add_argument('--output', default='./output')
	args = parser.parse_args()

	main(args.input, args.output)
