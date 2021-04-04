import argparse
 
class node:
    def __init__(self, value):
        self.value = value
        self.next = None
 
class linkedlist:
    def __init__(self):
        self.num_element = 0
        self.root = None
    def insert(self, k):
        if self.num_element == 0:
            self.root = node(k)
        else:
            Node = node(k)
            current = self.root
            Node.next = current
            self.root = Node
        self.num_element = self.num_element + 1
    def search(self, k):
        current = self.root
        while current != None:
            if current.value == k:
                s = 'Yes\n'
                break
            else:
                current = current.next
        if current == None:
            s = 'No\n'
        return s
    def delete(self, k, output):
        if self.num_element == 0:
            output.write('Error\n')
        else:
            current = self.root
            while current != None and current.value != k:
                previous = current
                current = current.next
            if current == None:
                output.write('Error\n')
            elif current == self.root:
                self.root = current.next
            else:
                previous.next = current.next
            self.num_element = self.num_element - 1
def findnum(n):
    n = n.lower()
    a = 0
    for i in range(len(n)):
        a += (ord(n[i])-96)*27**(len(n)-i-1)
    return a
class hash_table:
    def __init__(self):
        self.numslot = 1001
        self.slot = []
        for i in range(self.numslot):
            self.slot.append(linkedlist())
    # TODO
    def insert(self, n):
        a = findnum(n)
        a = a % self.numslot
        self.slot[a].insert(n)
    def look(self, k, output):
        k = int(k)
        if self.slot[k].num_element == 0:
            s = 'NULL\n'
        else:
            current = self.slot[k].root
            s = ''
            while current != None:
                s += current.value
                s += ' '
                current = current.next
            s = s[:-1] + '\n'
        output.write(s)
    def delete(self, n, output):
        a = findnum(n)
        a = a % self.numslot
        self.slot[a].delete(n, output)
    def search(self, n, output):
        a = findnum(n)
        a = a % self.numslot
        output.write(self.slot[a].search(n))
def main(input_path, output_path):
    table = hash_table()
    output = open(output_path, 'w')
    # TODO
    with open(input_path) as f:
        for line in f.readlines():
            line = line.strip()
            if line.lower() == 'end':
                break
            else:
                operation = line.split(' ')[0]
                key = line.split(' ')[1]
                if operation.lower() == 'insert':
                    table.insert(key)
                elif operation.lower() == 'look':
                    table.look(key, output)
                elif operation.lower() == 'delete':
                    table.delete(key, output)
                elif operation.lower() == 'search':
                    table.search(key, output)
    output.close()
    print(5)
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