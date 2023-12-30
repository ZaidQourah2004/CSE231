"""
Project 2
CSE 331 F23 (Onsay)
Authored By: Hank Murdock
Originally Authored By: Andrew McDonald & Alex Woodring & Andrew Haas & Matt Kight & Lukas Richters & Sai Ramesh
solution.py
"""

from typing import TypeVar, List

# for more information on type hinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")  # represents generic type
Node = TypeVar("Node")  # represents a Node object (forward-declare to use in Node __init__)


# pro tip: PyCharm auto-renders docstrings (the multiline strings under each function definition)
# in its "Documentation" view when written in the format we use here. Open the "Documentation"
# view to quickly see what a function does by placing your cursor on it and using CTRL + Q.
# https://www.jetbrains.com/help/pycharm/documentation-tool-window.html


class Node:
    """
    Implementation of a doubly linked list node.
    Do not modify.
    """
    __slots__ = ["value", "next", "prev", "child"]

    def __init__(self, value: T, next: Node = None, prev: Node = None, child: Node = None) -> None:
        """
        Construct a doubly linked list node.

        :param value: value held by the Node.
        :param next: reference to the next Node in the linked list.
        :param prev: reference to the previous Node in the linked list.
        :return: None.
        """
        self.next = next
        self.prev = prev
        self.value = value

        # The child attribute is only used for the application problem
        self.child = child

    def __repr__(self) -> str:
        """
        Represents the Node as a string.

        :return: string representation of the Node.
        """
        return f"Node({str(self.value)})"

    __str__ = __repr__


class DLL:
    """
    Implementation of a doubly linked list without padding nodes.
    Modify only below indicated line.
    """
    __slots__ = ["head", "tail", "size"]

    def __init__(self) -> None:
        """
        Construct an empty doubly linked list.

        :return: None.
        """
        self.head = self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        result = []
        node = self.head
        while node is not None:
            result.append(str(node))
            node = node.next
        return " <-> ".join(result)

    def __str__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        return repr(self)

    # MODIFY BELOW #

    def empty(self) -> bool:
        """
        Check if the doubly linked list is empty.

        :return: True if the DLL is empty, False otherwise.
        """
        return(self.head == None and self.tail == None)

    def push(self, val: T, back: bool = True) -> None:
        """
        Insert a new node with the given value into the DLL.

        :param val: The value to be inserted.
        :param back: If True, insert at the back of the DLL; otherwise, insert at the front.
        :return: None.
        """
        new_node = Node(val)

        if self.empty():
            self.head = self.tail = new_node
        elif back:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1


    def pop(self, back: bool = True) -> None:
        """
        Remove a node from the DLL.

        :param back: If True, remove from the back of the DLL; otherwise, remove from the front.
        :return: None.
        """
        if self.empty():
            return

        if back:
            if self.size == 1:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        else:
            if self.size == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

        self.size -= 1

    def list_to_dll(self, source: List[T]) -> None:
        """
        Convert a list into a doubly linked list.

        :param source: List to convert into a DLL.
        :return: None.
        """
        self.head = self.tail = None
        self.size = 0

        for item in source:
          self.push(item, back=True)

    def dll_to_list(self) -> List[T]:
        """
        Convert the doubly linked list into a list.

        :return: A list containing the elements of the DLL.
        """
        new_list = []
        current = self.head
        while current:
          new_list.append(current.value)
          current = current.next
        return new_list

    def _find_nodes(self, val: T, find_first: bool = False) -> List[Node]:
        """
        Find nodes with a specific value in the doubly linked list.

        :param val: The value to search for in the nodes.
        :param find_first: If True, stop searching after finding the first occurrence.
        :return: A list of Nodes containing the specified value or an empty list if none found.
        """
        result = []
        current = self.head

        while current:
            if current.value == val:
                result.append(current)
                if find_first:
                    break
            current = current.next

        return result

    def find(self, val: T) -> Node:
        """
        Find the first occurrence of a value in the DLL.

        :param val: The value to search for.
        :return: The first Node containing the value, or None if not found.
        """
        if self.empty():
            return None
        nodes = self._find_nodes(val)
        if nodes:
          return nodes[0]  # Return the first matching Node
        else:
          return None  # No matching Node found, return None

    def find_all(self, val: T) -> List[Node]:
        """
        Find all occurrences of a value in the DLL.

        :param val: The value to search for.
        :return: A list of Nodes containing the value, or an empty list if not found.
        """
        if self.empty():
            return []
        nodes = self._find_nodes(val)
        if nodes:
          return nodes  # Return the list of matching Node
        else:
          return []  # No matching Node found, return empty list

    def _remove_node(self, to_remove: Node) -> None:
        """
        Remove a specific node from the doubly linked list.

        :param to_remove: The node to be removed.
        :return: None.
        """
        if to_remove is None:
            return  # Nothing to remove

        if to_remove.prev is not None:
            to_remove.prev.next = to_remove.next  # Update the next reference of the previous node
        else:
            # If the node to remove is the head, update the head
            self.head = to_remove.next

        if to_remove.next is not None:
            to_remove.next.prev = to_remove.prev  # Update the previous reference of the next node
        else:
            # If the node to remove is the tail, update the tail
            self.tail = to_remove.prev

        # Set the references of the node to remove to None to disconnect it from the DLL
        to_remove.prev = None
        to_remove.next = None

        # Decrement the size of the DLL
        self.size -= 1


    def remove(self, val: T) -> bool:
        """
        Remove the first occurrence of a value from the DLL.

        :param val: The value to remove.
        :return: True if a value was removed, False if the value was not found.
        """
        current = self.head
        while current:
            if current.value == val:
                self._remove_node(current)
                return True
            current = current.next
        return False

    def remove_all(self, val: T) -> int:
        """
        Remove all occurrences of a value from the DLL.

        :param val: The value to remove.
        :return: The number of occurrences removed.
        """
        nodes = self.find_all(val)  # Find all occurrences of val
        count = len(nodes)  # Get the count of nodes to be removed

        for node in nodes:
            self._remove_node(node)  # Remove each node

        return count  # Return the count of removed nodes


    def reverse(self) -> None:
        """
        Reverse the order of elements in the doubly linked list.

        :return: None.
        """
        if self.head == self.tail:
            return 

        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self.head, self.tail = self.tail, self.head

class BrowserHistory:

    def __init__(self, homepage: str):
        """
        Initialize a browser history object with a homepage.

        :param homepage: The URL of the homepage.
        :return: None.
        """
        
        self.head = Node(homepage)
        self.tail = self.head
        self.current_page = self.head
        

    def get_current_url(self) -> str:
        """
        Get the URL of the current page.

        :return: The URL of the current page.
        """
        return self.current_page.value

    def visit(self, url: str) -> None:
        """
        Visit a new URL and add it to the browser history.

        :param url: The URL to visit.
        :return: None.
        """
        new_page = Node(url)
        new_page.prev = self.current_page
        self.current_page.next = new_page
        self.current_page = new_page
        self.tail = new_page
    
    def backward(self) -> None:
        """
        Navigate backward in the browser history.

        :return: None.
        """
        while self.current_page.prev:
            if not metrics_api(self.current_page.prev.value):
                self.current_page = self.current_page.prev
                return
            self.current_page = self.current_page.prev
            

    def forward(self) -> None:
        """
        Navigate forward in the browser history.

        :return: None.
        """
        while self.current_page.next:
            if not metrics_api(self.current_page.next.value):
                self.current_page = self.current_page.next
                return
            self.current_page.next.value = self.current_page.value
            self.current_page = self.current_page.next



# DO NOT MODIFY
intervention_set = set(['https://malicious.com', 'https://phishing.com', 'https://malware.com'])
def metrics_api(url: str) -> bool:
    """
    Uses the intervention_set to determine what URLs are bad and which are good. 

    :param url: The url to check.
    :returns: True if this is a malicious website, False otherwise.
    """
    if url in intervention_set:
        return True
    return False
