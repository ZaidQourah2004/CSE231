from typing import TypeVar  # For use in type hinting

# Type declarations
T = TypeVar('T')        # generic type
SLL = TypeVar('SLL')    # forward declared Singly Linked List type
Node = TypeVar('Node')  # forward declared Node type


class SLLNode:
    """
    Node implementation
    Do not modify
    """

    __slots__ = ['data', 'next']

    def __init__(self, data: T, next: Node = None) -> None:
        """
        Initialize an SLL Node
        :param data: data value held by the node
        :param next: reference to the next node in the SLL
        :return: None
        """
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """
        Overloads `str()` method, casts SLL nodes to strings
        :return: string representation of node
        """
        return '(Node: ' + str(self.data) + ' )'

    def __repr__(self) -> str:
        """
        Overloads `repr()` method for use in debugging
        :return: string representation of node
        """
        return '(Node: ' + str(self.data) + ' )'

    def __eq__(self, other: Node) -> bool:
        """
        Overloads `==` operator to compare nodes
        :param other: right operand of `==`
        :return: True if the nodes are ==, else False
        """
        return self is other if other is not None else False


class SinglyLinkedList:
    """
    SLL implementation
    """

    __slot__ = ['head', 'tail']

    def __init__(self) -> None:
        """
        Initializes an SLL
        return: None
        DO NOT MODIFY THIS FUNCTION
        """
        self.head = None
        self.tail = None

    def __repr__(self) -> str:
        """
        Represents an SLL as a string
        DO NOT MODIFY THIS FUNCTION
        :return: string representation of SLL
        """
        return self.to_string()

    def __eq__(self, other: SLL) -> bool:
        """
        Overloads `==` operator to compare SLLs
        :param other: right operand of `==`
        :return: True if equal, else False
        DO NOT MODIFY THIS FUNCTION
        """
        comp = lambda n1, n2: n1 == n2 and (comp(n1.next, n2.next) if (n1 and n2) else True)
        return comp(self.head, other.head)

    # ========== Modify below ========== #

    def append(self, data: T) -> None:
        """
        Append an SLLNode to the end of the SLL
        :param data: data to append
        :return: None
        """
        # create new node
        # insert new element
        # have new node point to null
        # have old node point to new node
        # update tail to point to new node
        new_node = SLLNode(data)  # Create a new SLLNode with the provided data
        if self.head is None:  # If the linked list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # Set the 'next' reference of the current tail to the new node
            self.tail = new_node  # Update the tail to be the new node

    def to_string(self) -> str:
        """
        Converts an SLL to a string
        :return: string representation of SLL
        """
        stringz = ""
        if self.head is None:
            return "None"
        current = self.head
        while current:
            stringz += str(current.data)
            if current.next:
                stringz += " --> "
            current = current.next
        current = self.tail

        return stringz

    def length(self) -> int:
        """
        Determines number of nodes in the list
        :return: number of nodes in list
        """
        iterations = 0
        current = self.head
        while current:
            iterations+=1
            current = current.next
        return iterations

    def total(self) -> T:
        """
        Sums up the values in the list
        :return: total sum of values in the list
        """
        if self.head is None:
            return None
        try:
          summation = self.head.data - self.head.data
        except:
          summation = ""
        current = self.head
        while current:
            summation += current.data
            current = current.next
        return summation

    def delete(self, data):
        """
        Deletes the first node containing `data` from the SLL
        :param data: data to remove
        :return: True if a node was removed, else False
        """
        if self.head is None:
            return False

        if self.head.data == data:
          if self.head == self.tail:
            self.tail = None
          self.head = self.head.next
          return True

        current = self.head
        previous = None
        while current:
          if current.data == data:
              if current == self.tail:
                  self.tail = previous
              if previous:
                  previous.next = current.next
              else:
                  self.head = current.next
              return True
          previous = current
          current = current.next

        return False

    def delete_all(self, data):
        """
        Deletes all instances of a node containing `data` from the SLL
        :param data: data to remove
        :return: True if any nodes were removed, else False
        """
        if self.head is None:
            return False
        counter = 0
        if self.head.data == data:
          if self.head == self.tail:
            self.tail = None
          self.head = self.head.next
          counter += 1

        current = self.head
        previous = None
        while current:
          if current.data == data:
              if current == self.tail:
                  self.tail = previous
              if previous:
                  previous.next = current.next
              else:
                  self.head = current.next
              counter += 1
          previous = current
          current = current.next

        return bool(counter)

    def find(self, data: T) -> bool:
        """
        Looks through the SLL for a node containing `data`
        :param data: data to search for
        :return: True if found, else False
        """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def find_sum(self, data: T) -> int:
        """
        Returns the number of occurrences of `data` in this list
        :param data: data to find and sum up
        :return: number of times the data occurred
        """
        counter = 0
        current = self.head
        while current:
            if current.data == data:
                counter +=1
            current = current.next
        return counter


def help_mario(roster: SLL, ally: str) -> bool:
    """
    Updates the roster of racers to put Mario's ally at the front
    Preserves relative order of racers around ally
    :param roster: initial order of racers
    :param ally: the racer that needs to go first
    :return: True if the roster was changed, else False
    """
    if not roster.find(ally):
        return False

    if roster.head.data == ally:
        return False

    roster_copy = SinglyLinkedList()

    current = roster.head
    while current:
        if current.data == ally:
            break
        current = current.next

    while current:
        roster_copy.append(current.data)
        current = current.next

    new_current = roster.head

    while new_current.data != ally:
        roster_copy.append(new_current.data)
        new_current = new_current.next

    roster.head = roster_copy.head
    roster.tail = roster_copy.tail
    return True