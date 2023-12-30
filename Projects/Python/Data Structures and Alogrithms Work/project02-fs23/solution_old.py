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
        FILL IN DOCSTRING
        """
        return(self.head == None and self.tail == None)

    def push(self, val: T, back: bool = True) -> None:
        """
        FILL IN DOCSTRING
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
        FILL IN DOCSTRING
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
        FILL IN DOCSTRING
        """
        self.head = self.tail = None
        self.size = 0

        for item in source:
          self.push(item, back=True)

    def dll_to_list(self) -> List[T]:
        """
        FILL IN DOCSTRING
        """
        new_list = []
        current = self.head
        while current:
          new_list.append(current.value)
          current = current.next
        return new_list

    def _find_nodes(self, val: T, find_first: bool = False) -> List[Node]:
        """
        FILL IN DOCSTRING
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
        FILL IN DOCSTRING
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
        FILL IN DOCSTRING
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
        FILL IN DOCSTRING
        """
        pass

    def remove(self, val: T) -> bool:
        """
        FILL IN DOCSTRING
        """
        pass

    def remove_all(self, val: T) -> int:
        """
        FILL IN DOCSTRING
        """
        pass

    def reverse(self) -> None:
        """
        FILL IN DOCSTRING
        """
        pass

class BrowserHistory:

    def __init__(self, homepage: str):
        """
        FILL IN DOCSTRING
        """
        pass

    def get_current_url(self) -> str:
        """
        FILL IN DOCSTRING
        """
        pass

    def visit(self, url: str) -> None:
        """
        FILL IN DOCSTRING
        """
        pass
    
    def backward(self) -> None:
        """
        FILL IN DOCSTRING
        """
        pass

    def forward(self) -> None:
        """
        FILL IN DOCSTRING
        """
        pass

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
