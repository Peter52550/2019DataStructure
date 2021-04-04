import argparse

class BSTree_Node():
    def __init__(self, key):
        self.value = key
        self.left_child = None
        self.right_child = None
    def __repr__(self):
        return str(self.value)

class BSTree():
    def __init__(self):
        self.root = None

    def insert(self, key):
        # TODO
        if self.root == None:
            new = BSTree_Node(key)
            self.root = new
        else:
            temp = self.root
            while True:
                if key < temp.value:
                    if temp.left_child == None:
                        new = BSTree_Node(key)
                        temp.left_child = new
                        break
                    else:
                        temp = temp.left_child
                elif key == temp.value:
                    return
                else:
                    if temp.right_child == None:
                        new = BSTree_Node(key)
                        temp.right_child = new
                        break
                    else:
                        temp = temp.right_child

    def delete(self, key):
        # TODO
        temp = self.root
        current = self.root
        while key != temp.value:
            if key < temp.value:
                if temp.left_child == None:
                    return
                else:
                    current = temp
                    temp = temp.left_child
            else:
                if temp.right_child == None:
                    return
                else:
                    current = temp
                    temp = temp.right_child
        if temp.left_child == None and temp.right_child == None:
            if temp.value > current.value:
                current.right_child = None
                return
            else:
                current.left_child = None
                return
        elif temp.left_child != None and temp.right_child != None:
            if temp == self.root:
                if temp.right_child.left_child == None:
                    temp.right_child.left_child = temp.left_child
                    self.root = temp.right_child
                    return
                elif temp.right_child.left_child != None:
                    minimum = temp.right_child
                    top = minimum
                    while minimum.left_child != None:
                        top = minimum
                        minimum = minimum.left_child
                    if minimum.right_child == None:
                        minimum.left_child = temp.left_child
                        minimum.right_child = temp.right_child
                        top.left_child = None
                    else:
                        minimum.left_child = temp.left_child
                        top.left_child = minimum.right_child
                        minimum.right_child = temp.right_child  
                    self.root = minimum
                    return
            elif temp.value < current.value:
                if temp.right_child.left_child == None:
                    temp.right_child.left_child = temp.left_child
                    current.left_child = temp.right_child
                elif temp.right_child.left_child != None:
                    minimum = temp.right_child
                    top = minimum
                    while minimum.left_child != None:
                        top = minimum
                        minimum = minimum.left_child
                    if minimum.right_child == None:
                        minimum.left_child = temp.left_child
                        minimum.right_child = temp.right_child
                        top.left_child = None
                    else:
                        minimum.left_child = temp.left_child
                        top.left_child = minimum.right_child
                        minimum.right_child = temp.right_child
                    current.left_child = minimum
            else:
                if temp.right_child.left_child == None:
                    temp.right_child.left_child = temp.left_child
                    current.right_child = temp.right_child
                elif temp.right_child.left_child != None:
                    minimum = temp.right_child
                    top = minimum
                    while minimum.left_child != None:
                        top = minimum
                        minimum = minimum.left_child
                    if minimum.right_child == None:
                        minimum.left_child = temp.left_child
                        minimum.right_child = temp.right_child
                        top.left_child = None
                    else:
                        minimum.left_child = temp.left_child
                        minimum.right_child = temp.right_child
                        top.left_child = minimum.right_child
                    current.right_child = minimum
        else:
            if temp.value > current.value:
                if temp.left_child == None and temp.right_child != None:
                    current.right_child = temp.right_child
                    return
                elif temp.left_child != None and temp.right_child == None:
                    current.right_child = temp.left_child
                    return
            else:
                if temp.left_child == None and temp.right_child != None:
                    current.left_child = temp.right_child
                    return
                elif temp.left_child != None and temp.right_child == None:
                    current.left_child = temp.left_child
                    return
        

    def inorder(self, output):
        # TODO
        node_list = []
        temp = self.root
        while True:
            while temp != None:
                node_list.append(temp)
                temp = temp.left_child
            if node_list == []:
                output.write("\n")
                return
            order = node_list.pop()
            output.write(str(order.value))
            output.write(' ')
            temp = order.right_child

    def preorder(self, output):
        # TODO
        node_list = []
        temp = self.root
        node_list.append(temp)
        while True:
            order = node_list.pop()
            output.write(str(order.value))
            output.write(' ')
            if order.right_child != None:
                node_list.append(order.right_child)
            if order.left_child != None:
                node_list.append(order.left_child)
            if node_list == []:
                output.write('\n')
                return
def main(input_path, output_path):
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # DO NOT MODIFY CODES HERE
    # It's important and repeat three times
    bstree = BSTree()
    output = open(output_path, 'w')
    with open(input_path) as f:
        for line in f.readlines():
            line = line.strip()
            if line.lower() == 'inorder':
                bstree.inorder(output)
            elif line.lower() == 'preorder':
                bstree.preorder(output)
            else:
                operation = line.split(' ')[0]
                key = int(line.split(' ')[1])
                if operation.lower() == 'insert':
                    bstree.insert(key)
                elif operation.lower() == 'delete':
                    bstree.delete(key)
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

