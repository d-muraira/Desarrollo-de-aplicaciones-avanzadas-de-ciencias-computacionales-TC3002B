#David Arturo Martinez Muraira
#A00837830

class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack)==0

class Queue():
    def __init__(self):
        self.queue=[]
    
    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue)==0
    
    def size(self):
        return len(self.queue)


class Dictionary():
    def __init__(self):
        self.items={}

    def put(self,key,value):
        self.items[key]=value
    
    def get(self,key):
        return self.items.get(key)

    def remove(self,key):
        if key in self.items:
            del self.items[key]
    
    def contains(self,key):
        return key in self.items

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items)==0



def main():
    print("=== STACK TESTS ===")
    s = Stack()

    # Test empty
    print("Empty:", s.is_empty())  # True
    print("Pop empty:", s.pop())  # None
    print("Peek empty:", s.peek())  # None

    # Push elements
    s.push(10)
    s.push(20)
    s.push(30)

    print("Empty after push:", s.is_empty())  # False
    print("Peek:", s.peek())  # 30

    # Pop elements (LIFO)
    print("Pop:", s.pop())  # 30
    print("Pop:", s.pop())  # 20
    print("Peek:", s.peek())  # 10

    print("Pop:", s.pop())  # 10
    print("Pop empty again:", s.pop())  # None
    print()

    print("=== QUEUE TESTS ===")
    q = Queue()

    # Test empty
    print("Empty:", q.is_empty())  # True
    print("Dequeue empty:", q.dequeue())  # None
    print("Peek empty:", q.peek())  # None

    # Enqueue elements
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print("Size:", q.size())  # 3
    print("Peek:", q.peek())  # 1

    # Dequeue elements (FIFO)
    print("Dequeue:", q.dequeue())  # 1
    print("Dequeue:", q.dequeue())  # 2
    print("Peek:", q.peek())  # 3

    print("Size:", q.size())  # 1
    print("Dequeue:", q.dequeue())  # 3
    print("Dequeue empty again:", q.dequeue())  # None
    print()

    print("=== DICTIONARY TESTS ===")
    d = Dictionary()

    # Test empty
    print("Empty:", d.is_empty())  # True
    print("Size:", d.size())  # 0
    print("Get missing key:", d.get("x"))  # None

    # Insert elements
    d.put("a", 1)
    d.put("b", 2)
    d.put("c", 3)

    print("Size after inserts:", d.size())  # 3
    print("Get a:", d.get("a"))  # 1
    print("Contains b:", d.contains("b"))  # True

    # Update value
    d.put("a", 100)
    print("Updated a:", d.get("a"))  # 100

    # Remove key
    d.remove("b")
    print("Contains b after remove:", d.contains("b"))  # False
    print("Size after remove:", d.size())  # 2

    # Remove non-existent key (should not crash)
    d.remove("z")

    # Clear remaining
    d.remove("a")
    d.remove("c")

    print("Empty at end:", d.is_empty())  # True
    print()

main()