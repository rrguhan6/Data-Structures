class node:
    def __init__(self, data=None, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next


class double_linked_list:
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None

    def print(self):
        temp = self.tail
        while(temp.previous != None):
            print(temp.data, end="  ")
            temp = temp.previous
        print(temp.data)

    def print_forward(self):
        temp = self.head
        while(temp.next != None):
            print(temp.data, end="  ")
            temp = temp.next
        print(temp.data)

    def insert_at_first(self, data):
        new_node = node(data)
        new_node.next = self.head
        if(self.head != None):
            if(self.head.next == None):
                self.tail = self.head
            self.head.previous = new_node
        self.head = new_node
        self.length = self.length + 1

    def insert_at_last(self, data):
        temp = self.head
        if(temp == None):
            self.head = node(data)
            self.length = self.length + 1
            return

        while(temp.next != None):
            temp = temp.next
        temp.next = node(data, temp, None)
        self.tail = temp.next
        self.length = self.length + 1

    def insert(self, data=None, n=None):
        if(data == None and n == None):
            return

        if(data == None):
            return

        if(n == None or n >= self.length):
            self.insert_at_last(data)
            return

        i = 0
        temp = self.head
        n = n-1
        while(temp.next != None):
            if(i == n):
                new_node = node(data)
                new_node.next = temp.next
                new_node.previous = temp
                temp.next.previous = new_node
                temp.next = new_node
                break
            temp = temp.next
            i = i+1
        self.length = self.length + 1


l = double_linked_list()
l.insert_at_first(11)
l.insert_at_first(12)
l.insert_at_first(13)
l.insert_at_first(14)


l.print()
l.print_forward()

l.insert(n=7, data=31)
l.insert(n=7, data=32)
l.insert(n=4, data=33)

l.print()
l.print_forward()

l.insert_at_last(21)
l.insert_at_last(22)
l.insert_at_last(23)

l.print()
l.print_forward()
