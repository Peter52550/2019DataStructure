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
        if self.currentSize == 0:            
            self.currentSize += 1
            self.heapList.append(node)
        else:
            self.currentSize += 1
            print('aa')
            self.heapList.append(node)
            swap = self.currentSize
            while swap != 1:
                if self.heapList[swap].value < self.heapList[swap//2].value:
                    self.heapList[swap].value, self.heapList[swap//2].value = self.heapList[swap//2].value, self.heapList[swap].value
                    swap = swap//2
                else:
                    break
            return self.heapList
    def delMin(self):
        #TODO
        if self.currentSize == 1:
            root = self.heapList.pop()
            self.currentSize = 0
        else:
            root = self.heapList.pop(1)
            self.heapList.insert(1, self.heapList.pop())
            self.currentSize -= 1
            index = 1
            while self.currentSize != 0 or math.floor(math.log(index,2)) < math.floor(math.log(self.currentSize, 2)):
                if 2*index+1 <= self.currentSize:
                    mini = min(self.heapList[2*index], self.heapList[2*index+1])
                    num = self.heapList.index(mini)
                    self.heapList[index].value, self.heapList[num].value = self.heapList[num].value, self.heapList[index].value
                    index = num
                elif 2*index <= self.currentSize:
                    if self.heapList[index].value > self.heapList[2*index].value:
                        self.heapList[index].value, self.heapList[2*index].value = self.heapList[2*index].value, self.heapList[index].value
                        index = 2*index
                    else:
                        break
                else:
                    break
        return root
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


