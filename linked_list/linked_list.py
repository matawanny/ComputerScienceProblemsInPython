class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data}"


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append_val(self, x):
        if not isinstance(x, Node):
            x = Node(x)
        if self.head is None:
            self.head = x
        else:
            self.tail.next = x
        self.tail = x

    def __str__(self):
        to_print = ""
        curr = self.head
        while curr is not None:
            to_print += str(curr.data) + "->"
            curr = curr.next
        if to_print:
            return "[" + to_print[:-2] + "]"
        else:
            return "[]"

    def add_to_start(self, x):
        if not isinstance(x, Node):
            x = Node(x)
        x.next = self.head
        self.head = x

    def search_val(self, x):
        '''return indices where x wash found'''
        i = 0
        curr = self.head
        found = False
        while curr:
            if curr.data == x:
                found = True
                break
            curr = curr.next
            i += 1
        if found:
            return i
        else:
            return None


    def remove_val_by_index(self, x):
        prev = None
        curr = self.head
        while curr:
            if curr.data == x:
                if prev:
                    prev.next = curr.next
                    if curr.next is None:
                        self.tail = prev
                else:
                    self.head = curr.next

                return True

            prev = curr
            curr = curr.next
        return False

    def length(self):
        i = 0
        curr = self.head
        while curr:
            i += 1
            curr = curr.next
        return i

    def reverse_list_recur(self, curretn, pervious):
        pass


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    my_list = LinkedList()
    print(my_list)
    my_list.append_val(node1)
    my_list.append_val(node2)
    my_list.append_val(node3)
    my_list.append_val(node4)
    my_list.append_val(5)
    my_list.add_to_start(0)
    my_list.remove_val_by_index(4)

    print(my_list)
    print(my_list.search_val(2))
    print(my_list.length())
