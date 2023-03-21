class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None


class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):  # added this line, takes a value
        newNode = SLNode(val)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        return self

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next 	# set the runner to its neighbor
        return self  # once the loop is done, return self to allow for chaining

    def add_to_back(self, val):
        if self.head == None:  # if the list is empty
            self.add_to_front(val)  # run the add_to_front method
            return self  # let's make sure the rest of this function doesn't happen if we add to the front
        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node  # increment the runner to the next node in the list
        return self  # return self to allow for chaining

    def remove_from_front(self):
        if self.head == None:
            return self
        newHead = self.head.next
        self.head.next = None
        del self.head
        self.head = newHead

    def remove_from_back(self):
        if self.head == None:
            return self
        runner = self.head
        previous = runner
        while (runner.next != None):
            previous = runner
            runner = runner.next
        previous.next = None
        del runner
        return self

    def remove_val(self, val):
        if self.head == None:
            return self
        if self.head.value == val:
            newHead = self.head.next
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
            del runner
        return self

    def insert_at(self, val, n):
        if (self.head == None and n > 0) or n < 0:
            return self
        if n == 0:
            self.add_to_front(val)
            return self
        newNode = SLNode(val)
        runner = self.head
        previous = runner
        while (n != 0 and runner.next != None):
            previous = runner
            runner = runner.next
            n -= 1
        if n == 0:
            previous.next = newNode
            newNode.next = runner
        else:
            print("link list not that long!")
        return self