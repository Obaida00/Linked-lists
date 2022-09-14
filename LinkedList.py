class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list(object):
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
            curr=curr.next
        return lgth




l = linked_list()

l.append(21)
l.append(56)
l.append(39)
l.append(28)
l.append(12)
l.append(31)

l.display()
print(l.length())