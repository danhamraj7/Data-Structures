"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next == self.next
        if self.next:
            self.next.previous == self.prev


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        pass

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        pass

    """
    Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        # create instance of ListNode with value
        new_node = ListNode(value, None, None)
# increment the DLL length attribute
        self.length += 1
# if DLL is empty
# set head and tail to the new node instance
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
# if DLL is not empty
# set new node's prev to current tail
        else:
            new_node.prev = self.tail
# set tail's next to new node
# set tail to the new node
            self.tail.next = new_node
            self.tail = new_node

    """
    Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        # store the value of the tail
        value = self.tail.value
    # call the delete fun to delete tail from dll
        self.delete(self.tail)
     # return the value
        return value

    """
    Removes the input node from its current spot in the
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        pass

    """
    Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the
    order of the other elements of the List.
    """

    def delete(self, node):
        # check if dll is empty there is nothing to delete. just ret
        # no in dll is 0
        if not self.head and self.tail:
            return

        # decrement the length of dll
        # once we pass the return we know a node will be deleted
        # so we decrement the length.
        self.length -= 1
        # if the dll has just 1 item remove it by setting
        # head and tail pointers to none
        # no in dll is 1
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # if the node to be deleted is the head
        # set the head pointer of the next.node
        # delete node connection
        # no. in dll could be > 2
        elif self.head == node:
            self.head = node.next
            node.delete()
        # if the node to be deleted is the tail
        # set the tail pointer of the prev.node
        # delete node connection
        # no. in dll could be > 2
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        # not head or tail
        # no. in dll has to be at least 3
        # delete the connection
        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        pass
