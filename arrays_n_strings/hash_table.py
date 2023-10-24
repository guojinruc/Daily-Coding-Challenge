
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_node = None

    def set_next(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.start = None

    def is_empty(self):
        return self.start is None

    def append(self, key, value):
        new_node = Node(key, value)
        if self.start is None:
            self.start = new_node
        else:
            last_node = self.start
            while last_node.next_node is not None:
                last_node = last_node.next_node
            last_node.set_next(new_node)

    def prepend(self, key, value):
        new_node = Node(key, value)
        new_node.set_next(self.start)
        self.start = new_node

    def delete(self, key):
        if self.is_empty():
            return
        if self.start.key == key:
            self.start = self.start.next_node
        else:
            prev_node = self.start
            current_node = self.start.next_node
            while current_node.key != key and current_node is not None:
                prev_node = current_node
                current_node = current_node.next_node
            if current_node.key == key:
                prev_node.set_next(current_node.next_node)

    def display(self):
        if self.is_empty():
            print()
        else:
            s = str(self.start.key) + ': ' + str(self.start.value)
            current_node = self.start.next_node
            while current_node is not None:
                s += ' -> ' + str(current_node.key) + ': ' + str(current_node.value)
                current_node = current_node.next_node
            print(s)

class HashTable:
    """
    Hashtable whose keys are strings.
    """
    size = 1000
    x = 31

    def __init__(self):
        self.table = [None for i in range(self.size)]

    def hash_function(self, key: str) -> int:
        """
        Use polynomial and mod to compute hash function.
        """
        h = 0
        # Horner's rule
        for i, c in enumerate(key):
            h += h*HashTable.x + ord(c)
        return h % HashTable.size
    
    def insert(self, key: str, value):
        h = self.hash_function(key)
        ll = LinkedList() if self.table[h] is None else self.table[h]
        ll.append(key, value)

    def get(self, key: str):
        h = self.hash_function(key)
        ll = self.table[h]
        if ll is not None:
            node = ll.start
            while node is not None:
                if node.key == key:
                    return node.value
                node = node.next_node
        return None

    def delete(self, key: str):
        h = self.hash_function(key)
        ll = self.table[h]
        if ll is not None:
            ll.delete(key)

    def display(self):
        for item in self.table:
            if item is not None:
                item.display()

if __name__ == "__main__":
    ll = LinkedList()
    print("Initial list is empty: ", ll.is_empty())
    ll.append("b", 1)
    ll.prepend("a", 0)
    ll.append("c", 9)
    ll.prepend("aa", 3)
    ll.display()
    ll.delete('b')
    ll.display()
    ll.delete('aa')
    ll.display()