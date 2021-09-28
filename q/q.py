class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class q:
    def __init__(self):
        self.head = None
        self.rear = None

    def print(self):
        cur = self.head

        if cur:

            while (cur):
                print(cur.data)
                cur = cur.next

    def insert(self, data):
        if self.head is None:
            self.head = node(data)
            self.rear = self.head
            return True

        self.rear.next = node(data)
        self.rear = self.rear.next

    def peek(self):
        if self.head:
            return self.head.data
        else:
            return

    def is_empty(self):
        return self.head is None

    def delete_head(self):
        if self.head:
            self.head = self.head.next

    def delete_rear(self):
        if self.head:
            cur = self.head
            if cur.next:
                while cur.next.next is not None:
                    cur = cur.next
                self.rear = cur
                self.rear.next = None

            else:
                self.head = self.rear


x = q()

x.insert(1)
x.insert(3)
x.insert(5)
x.insert(7)
x.insert(8)
x.insert(12)
x.insert(11)
x.insert(11)

# x.print()
x.delete_head()
print(x.peek())
x.delete_rear()
x.print()
