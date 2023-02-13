import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")


class Queue(object):
    def __init__(self):
        self.items = []
        self.front = None
        self.rear = None

    def enqueue(self, item):
        self.items.insert(0, item)
        self.front = item
        self.rear = item if len(self.items) else self.items[-1]

    def dequeue(self):
        if self.items == []:
            return "Ain't no items left"
        else:
            item = self.items.pop()
            self.rear = self.items[-1] if len(self.items) > 0 else None
            return item

    def peek(self):
        if self.is_empty() == False:
            return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def __str__(self):
        myReturnString = ""
        for i in range(0, len(self.items)-1):
            myReturnString = myReturnString + str(self.items[i]) + ", "
        myReturnString = myReturnString + str(self.items[len(self.items)-1])
        return "|" + myReturnString + "|"


print("Queue()")
print(32*"#")
q = Queue()
assert q.isEmpty() == True
q.enqueue("rat")
assert q.front == "rat"
q.enqueue("bag")
assert q.front == "bag"
q.enqueue("rat")
assert q.front == "rat"
assert q.rear == "rat"

rear = q.dequeue()
print("last: ", rear)
print(q)
assert q.isEmpty() == False
assert str(q) == "|rat, bag|"

rear = q.dequeue()
print("rear: ", rear)
rear = q.dequeue()
print("rear: ", rear)
rear = q.dequeue()
print("rear: ", rear)
assert q.isEmpty() == True


# Inefficient pop() method, efficient push()
class StackQ(object):
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, item):
        self.q1.enqueue(item)

    def pop(self):
        while len(self.q1.items) > 1:
            self.q2.enqueue(self.q1.dequeue())
        popVal = self.q1.dequeue()
        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp
        return popVal

    def isEmpty(self):
        return self.q1.isEmpty()

    def peek(self):
        if self.q1.isEmpty() == False:
            return self.q1.items[-1]

    def __str__(self):
        myReturnString = ""
        if self.q1.items == []:
            return "# @"
        else:
            for i in range(0, len(self.q1.items)-1):
                myReturnString = myReturnString + str(self.q1.items[i]) + ", "
            myReturnString = myReturnString + \
                str(self.q1.items[len(self.q1.items)-1])
            return "# " + myReturnString + " @"


print("\nStackQ()")
print(32*"#")

stack = StackQ()
stack.push("rat")
stack.peek()
print("push:", stack)
stack.push("bag")
stack.peek()
print("push:", stack)
stack.push("yellowbeard")
stack.peek()
print("push:", stack)

data = stack.pop()
print("pop :", stack)
data = stack.pop()
print("pop :", stack)
data = stack.pop()
print("pop :", stack)
data = stack.pop()
print(data)


# Inefficient push() method, efficient pop()
class StackQ2(object):
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, item):
        self.q1.enqueue(item)

    def pop(self):
        while len(self.q1.items) > 1:
            self.q2.enqueue(self.q1.dequeue())
        popVal = self.q1.dequeue()
        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp
        return popVal

    def isEmpty(self):
        return self.q1.isEmpty()

    def peek(self):
        if self.q1.isEmpty() == False:
            return self.q1.items[-1]

    def __str__(self):
        myReturnString = ""
        if self.q1.items == []:
            return "# @"
        else:
            for i in range(0, len(self.q1.items)-1):
                myReturnString = myReturnString + str(self.q1.items[i]) + ", "
            myReturnString = myReturnString + \
                str(self.q1.items[len(self.q1.items)-1])
            return "# " + myReturnString + " @"
