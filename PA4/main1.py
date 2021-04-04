import argparse
import math

class Heap_Node():
    def __init__(self, key):
        self.value = key

    def __repr__(self):
        return 'Heap_Node({})'.format(str(self.value))

    def __gt__(self, other):
        if self.value > other.value:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.value > other.value:
            return False
        else:
            return True

class MinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def __repr__(self):
        return str(self.heapList)

    def insert(self, node):
        #TODO
        store = []
        for i in self.heapList:
            num = ''
            if i == 0:
                store.append(0)
                continue
            else:
                for j in i:
                    if j.isdigit():
                        num += j
            store.append(int(num))
        if self.currentSize == 0:            
            store.append(node.value)
            self.currentSize += 1
            self.heapList.append('Heap_Node(' + str(node.value) + ')')
        else:
            store.append(node.value)
            self.currentSize += 1
            swap = self.currentSize
            while swap != 1:
                if store[swap] < store[swap//2]:
                    store[swap], store[swap//2] = store[swap//2], store[swap]
                    swap = swap//2
                else:
                    break
            self.heapList.clear()
            self.heapList.append(0)
            for i in range(1, len(store)):
                self.heapList.append('Heap_Node(' + str(store[i]) + ')')
            self.heapList = store

    def delMin(self):
        #TODO
        store = []
        for i in self.heapList:
            num = ''
            if i == 0:
                store.append(0)
                continue
            for j in i:
                if j.isdigit():
                    num += j
            store.append(int(num))
        if self.currentSize == 1:
            root = store.pop()
            self.currentSize = 0
        else:
            root = store.pop(1)
            store.insert(1, store.pop())
            self.currentSize -= 1
            index = 1
            while self.currentSize != 0 or math.floor(math.log(index,2)) < math.floor(math.log(self.currentSize, 2)):
                if 2*index <= self.currentSize:
                    if store[index] > store[2*index]:
                        store[index], store[2*index] = store[2*index], store[index]
                        index = 2*index
                    else:
                        break
                elif 2*index+1 <= self.currentSize:
                    if store[index] > store[2*index+1]:
                        store[index], store[2*index+1] = store[2*index+1], store[index]
                        index = 2*index+1
                    else:
                        break
                else:
                    break
        self.heapList.clear()
        self.heapList.append(0)
        for i in range(1, len(store)):
            self.heapList.append('Heap_Node(' + str(store[i]) + ')')
        return 'Heap_Node(' + str(root) + ')'
def main(input_path, output_path):
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    minheap = MinHeap()
    output = open(output_path, 'w')
    with open(input_path) as f:
        for line in f.readlines():
            line = line.strip()
            if line.lower() == 'print':
                print(minheap, file=output)
            else:
                operation = line.split(' ')[0]
                if operation.lower() == 'insert':
                    key = int(line.split(' ')[1])
                    minheap.insert(Heap_Node(key))
                elif operation.lower() == 'delmin':
                    print(minheap.delMin(), file=output)
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


