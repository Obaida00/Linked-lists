class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linked_list(object):
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node

    def display(self):
        elems = []
        curr = self.head
        while curr.next != None:
            curr = curr.next
            elems.append(curr.data)
        print(elems)

    def length(self):
        lgth = 0
        curr = self.head
        while curr.next != None:
            lgth += 1
            curr = curr.next
        return lgth

    def extract(self, index):
        if index >= self.length():
            print("ERROR!! 'extract' Index out of range")
            return
        curr_index = 0
        curr_node = self.head
        while True:
            curr_node = curr_node.next
            if curr_index == index: return curr_node.data
            curr_index += 1

    def remove(self, index):
        if index >= self.length():
            print("ERROR!! 'remove' Index out of range")
            return
        curr_index = 0
        curr_node = self.head
        while True:
            last_node = curr_node
            curr_node = curr_node.next
            if curr_index == index:
                last_node.next = curr_node.next
                return
            curr_index += 1


l = Linked_list()

# Appending/adding elements
l.append(21)
l.append(56)
l.append(39)
l.append(28)
l.append(12)
l.append(31)

# Displaying the list
print('the linked list..')
l.display()

# Getting the length of the list
print('\nthe length of the l-list is', l.length())

# Extracting elements
print('\nelement at index 0:', l.extract(0))
print('element at index 1:', l.extract(1))
print('element at index 2:', l.extract(2))
print('element at index 3:', l.extract(3))
print('element at index 4:', l.extract(4))
print('element at index 5:', l.extract(5))

# Removing elements
l.remove(2)
print('\nafter removing index 2')
l.display()

l.remove(3)
print('after removing index 3')
l.display()

l.remove(3)
print('after removing index 3')
l.display()

l.remove(1)
print('after removing index 1')
l.display()

l.remove(1)
print('after removing index 1')
l.display()

l.remove(0)
print('after removing index 0')
l.display()
