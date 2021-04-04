class node:
    # this class infor testing
    # Do Not Modify
    def __init__(self, value):
        self.value = value
        self.right = self
        self.left = self
        
    def __repr__(self):
        return 'Node{}'.format(self.value).strip()

class stack:
    def __init__(self):
        self.num_element = 0
        self.root = node(None)
    
    def pop(self):
        if self.num_element == 0:
            raise ValueError('Can not execute pop() on an empty stack')
        else:
        # TODO:
        # Connect the second last element >> root
        # Connect root >> the second last element 
            if self.num_element == 1:
                self.root.left = self.root
                self.root.right = self.root
            else:
                temp = self.root.left.left         
                temp.right = self.root
                self.root.left = temp
            self.num_element -= 1
    def push(self, node):
        # TODO:
        # Connect the last element >> inserted node
        # Connect the inserted node >> root
        if self.num_element == 0:
            self.root.right = node
            node.left = self.root
            node.right = self.root
            self.root.left = node
        else:
            temp = self.root.left
            node.left = temp
            temp.right = node
            node.right = self.root
            self.root.left = node
        self.num_element += 1

    def __repr__(self):
        ret = ''
        node = self.root.right
        while node != self.root:
            ret  = ret + '>>' + str(node)
            node = node.right
        return ret

class queue:
    def __init__(self):
        self.num_element = 0
        self.root = node(None)

    def pop(self):
        if self.num_element == 0:
            raise ValueError('Can not execute pop() on an empty queue')
        else:
            # TODO:
            # Connect the second element >> root
            # Connect root >> the second element 
            if self.num_element == 1:
                self.root.left = self.root
                self.root.right = self.root
            else:
                temp = self.root.right.right         
                temp.left = self.root
                self.root.right = temp
            self.num_element -= 1


    def push(self, node):       
        # TODO:
        # Connect the root >> inserted node
        # Connect the inserted node >> first element
        if self.num_element == 0:
            self.root.right = node
            node.left = self.root
            node.right = self.root
            self.root.left = node
        else:
            temp = self.root.left
            temp.right = node
            node.left = temp
            self.root.left = node
            node.right = self.root
        self.num_element += 1
    def __repr__(self):
        ret = ''
        node = self.root.right
        while node != self.root:
            ret  = ret + '>>' + str(node)
            node = node.right
        return ret


