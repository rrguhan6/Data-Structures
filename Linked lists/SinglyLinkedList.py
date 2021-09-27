class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linked_list:
    def __init__(self, data):
        self.head = node(data)
        self.length = 1

    def print(self):
        temp = self.head
        while temp.next != None:
            print(temp.data, end="  ")
            temp = temp.next
        print(temp.data)

    def insert_at_end(self, data):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = node(data)
        self.length = self.length + 1

    def insert_at_first(self, data):
        temp = node(data)
        temp.next = self.head
        self.head = temp
        self.length = self.length + 1

    def insert(self, data, n=None):
        i = 0
        temp = self.head
        if(n == None):
            self.insert_at_end(data)
            return

        if(n < 0):
            return

        if(n == 0):
            self.insert_at_first(data)
            return

        if(n >= self.length):
            self.insert_at_end(data)
            return

        while(i <= n):
            if(i == n-1):
                _temp = temp.next
                temp.next = node(data)
                temp.next.next = _temp

            else:
                temp = temp.next
            i = i+1

        self.length = self.length + 1

    def delete(self, data):
        temp = self.head
        previous_node = None
        while(temp.next != None):
            if(temp.data == data):
                if(previous_node == None):
                    self.head = self.head.next
                    return
                previous_node.next = temp.next
                return
            previous_node = temp
            temp = temp.next

    def reverse(self):
        prev = None
        temp = self.head
        while(temp != None):
            current_node = temp
            temp = temp.next
            current_node.next = prev
            prev = current_node

        self.head = prev

    def is_sorted(self):
        if(self.head is None):
            return True

        cur = self.head

        while(cur.next):
            if(cur.data > cur.next.data):
                return False

            cur = cur.next

        return True

    def is_cyclic(self):
        runner = self.head
        walker = self.head

        while(runner.next.next and walker.next):
            walker = walker.next
            runner = runner.next.next

            if(runner == walker):
                return True

        return False


l1 = linked_list(1)

l1.insert_at_end(11)
l1.insert_at_end(2)
l1.insert_at_end(3)

l1.insert_at_first(5)
l1.insert_at_end(55)
l1.insert_at_end(555)

l1.print()

l1.insert(77, n=5)

l1.print()

# l1.delete(3)
l1.reverse()
l1.print()

print(l1.is_sorted)
