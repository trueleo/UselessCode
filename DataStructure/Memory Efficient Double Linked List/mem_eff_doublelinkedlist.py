import ctypes

class Dlinkedlist:
    def __init__(self):
        self._head = None
        self._tail = None
        self._nodes = None

    def get_index(self, index):
        current = self._head
        for _ in range(0, index):
            current = current.next_node
        return current

    def append(self, data=None):
        if data == None:
            node = Node()
        else:
            node = Node(data)
        if self._head == None:
            self._head = node
            self._tail = node
        else:
            tail = self._tail
            tail_prev = tail.previous_node
            tail.next_node = node
            tail_next = tail.next_node
            tail._set_ptrdiff(tail_prev, tail_next)
            tail_next._set_ptrdiff(tail, node.next_node)
            self._tail = tail_next

    def __len__(self):
        if self._head == None:
            return 0
        current = self._head
        count = 1
        while current.next_node != None:
            current = current._next_node
            count += 1
        return count

class Node:
    def __init__(self, _data=0):
        self._data = _data
        self._next_node = 0
        self._ptrdiff = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, node):
        self._next_node = node

    @property
    def previous_node(self):
        node_id = self._ptrdiff ^ id(self.next_node)
        return ctypes.cast(node_id, ctypes.py_object).value

    def _set_ptrdiff(self, prev_node, next_node):
        self._ptrdiff = id(prev_node) ^ id(next_node)

if __name__ == "__main__":
    l = Dlinkedlist()

    for i in range(10,20):
        l.append(i)

    print("Node at index 0 (1st node):  ", l.get_index(0))
    print("node before 2nd node (1st node using previous_node method):  ", l.get_index(1).previous_node )

    print("\n traversing in reverse")
    curr = l._tail
    while curr != 0:
        print(curr.data, end=" ")
        curr = curr.previous_node
    print('')


