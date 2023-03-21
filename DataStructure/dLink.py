class DLNode:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None


class DList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, val):  # added this line, takes a value
        newNode = DLNode(val)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            if self.tail == None:
                self.tail = self.head
                self.tail.prev = newNode
            self.head = newNode
        return self

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next 	# set the runner to its neighbor
        return self  # once the loop is done, return self to allow for chaining

    def reverse(self):
        runner = self.head
        while runner.next != None:
            runner.prev, runner.next = runner.next, runner.prev
            runner = runner.prev
        self.tail.prev, self.tail.next = self.tail.next, self.tail.prev
        self.head, self.tail = self.tail, self.head
        return self

    def add_to_back(self, val):
        if self.head == None:  # if the list is empty
            self.add_to_front(val)  # run the add_to_front method
            return self  # let's make sure the rest of this function doesn't happen if we add to the front
        new_node = DLNode(val)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        return self  # return self to allow for chaining

    def remove_from_front(self):
        if self.head == None:
            return self
        newHead = self.head.next
        self.head.next = None
        del self.head
        self.head = newHead

    def remove_from_back(self):
        if self.tail == None:
            return self
        newTail = self.tail.prev
        newTail.next = None
        del self.tail
        self.tail = newTail
        return self

    def remove_val(self, val):
        if self.head == None:
            return self
        if self.head.value == val:
            newHead = self.head.next
            newHead.prev = None
            self.head.next = None
            del self.head
            self.head = newHead
        else:
            runner = self.head
            previous = runner
            while (runner.value != val and runner.next != None):
                previous = runner
                runner = runner.next
            previous.next = runner.next
            runner.next.prev = previous
            del runner
        return self

    def insert_at(self, val, n):
        if (self.head == None and n > 0) or n < 0:
            return self
        if n == 0:
            self.add_to_front(val)
            return self
        newNode = DLNode(val)
        runner = self.head
        previous = runner
        while (n != 0 and runner.next != None):
            previous = runner
            runner = runner.next
            n -= 1
        if n == 0:
            previous.next = newNode
            newNode.prev = previous
            newNode.next = runner
            runner.prev = newNode
        else:
            print("link list not that long!")
        return self