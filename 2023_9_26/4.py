class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def getsize(self):
        return self.size

    def empty(self):
        return self.size == 0

    def add(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1

    def append(self, value):
        node = Node(value)
        if self.empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
        self.size += 1

    def insert(self, pos, value):
        if pos <= 0:
            self.add(value)
        elif pos > self.size:
            self.append(value)
        else:
            node = Node(value)
            count = 0
            pre = self.head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node
            self.size += 1

    def remove(self, value):
        cur = self.head
        pre = None
        is_find = False
        while cur is not None:
            if cur.value == value:
                if not pre:
                    self.head = cur.next
                else:
                    pre.next = cur.next
                self.size -= 1
                is_find = True
                break
            else:
                pre = cur
                cur = cur.next
        return is_find

    def search(self, value):
        cur = self.head
        while cur is not None:
            if cur.value == value:
                return True
            cur = cur.next
        return False
