"""
Project 5: Deque
CSE 331 FS23
Authored by Gabriel Sotelo
starter.py
"""

import gc
from typing import TypeVar, List
from random import randint, shuffle
from timeit import default_timer
# COMMENT OUT THIS LINE (and `plot_speed`) if you don't want matplotlib
# from matplotlib import pyplot as plt

T = TypeVar('T')
CDLLNode = type('CDLLNode')

class CircularDeque:
    """
    Representation of a Circular Deque using an underlying python list
    """

    __slots__ = ['capacity', 'size', 'queue', 'front', 'back']

    def __init__(self, data: List[T] = None, front: int = 0, capacity: int = 4):
        """
        Initializes an instance of a CircularDeque
        :param data: starting data to add to the deque, for testing purposes
        :param front: where to begin the insertions, for testing purposes
        :param capacity: number of slots in the Deque
        """
        if data is None and front != 0:
            # front will get set to 0 by front_enqueue if the initial data is empty
            data = ['Start']
        elif data is None:
            data = []

        self.capacity: int = capacity
        self.size: int = len(data)
        self.queue: List[T] = [None] * capacity
        self.back: int = None if not data else self.size + front - 1
        self.front: int = front if data else None

        for index, value in enumerate(data):
            self.queue[index + front] = value

    def __str__(self) -> str:
        """
        Provides a string representation of a CircularDeque
        'F' indicates front value
        'B' indicates back value
        :return: the instance as a string
        """
        if self.size == 0:
            return "CircularDeque <empty>"

        str_list = [f"CircularDeque <"]
        for i in range(self.capacity):
            str_list.append(f"{self.queue[i]}")
            if i == self.front:
                str_list.append('(F)')
            elif i == self.back:
                str_list.append('(B)')
            if i < self.capacity - 1:
                str_list.append(',')

        str_list.append(">")
        return "".join(str_list)

    __repr__ = __str__

    # ============ Modifiy Functions Below ============#

    def __len__(self) -> int:
        """
        Returns the number of elements in the CircularQueue.
        :return: The number of elements in the queue.
        """
        return self.size

    def is_empty(self) -> bool:
        """
        Checks if the CircularQueue is empty.
        :return: True if the queue is empty, False otherwise.
        """
        if not self.size:
            return True
        else:
            return False

    def front_element(self) -> T:
        """
        Returns the element at the front of the CircularQueue.
        :return: The element at the front, or None if the queue is empty.
        """
        if self.is_empty():
            return None
        return self.queue[self.front]

    def back_element(self) -> T:
        """
        Returns the element at the back of the CircularQueue.
        :return: The element at the back, or None if the queue is empty.
        """
        if self.is_empty():
            return None
        return self.queue[self.back]

    def grow(self) -> None:
        """
        Increases the capacity of the CircularQueue by doubling it.
        Does not return anything
        """
        new_capacity = self.capacity * 2
        new_queue = [None] * new_capacity

        for i in range(self.size):
            new_queue[i] = self.queue[(self.front + i) % self.capacity]

        self.front = 0
        self.back = self.size - 1
        self.queue = new_queue
        self.capacity = new_capacity

    def shrink(self) -> None:
        """
        Decreases the capacity of the CircularQueue by half if possible.
        Returns nothing
        """
        new_capacity = self.capacity // 2
        if new_capacity < 4:
            return


        new_queue = [None] * new_capacity

        for i in range(self.size):
            new_queue[i] = self.queue[(self.front + i) % self.capacity]

        self.front = 0
        self.back = self.size - 1
        self.queue = new_queue
        self.capacity = new_capacity

    def enqueue(self, value: T, front: bool = True) -> None:
        """
        Adds an element to the CircularQueue.
        :param value: The value to be added.
        :param front: If True, adds the value to the front; if False, adds it to the back.
        Returns: Nothing
        """

        if self.size == self.capacity:
            self.grow()
        if self.is_empty():
            self.front = 0
            self.back = 0
            if front:
                self.queue[self.front] = value

            else:
                self.queue[self.back] = value

        else:
            if front:
                self.front = (self.front - 1) % self.capacity
                self.queue[self.front] = value

            else:
                self.back = (self.back + 1) % self.capacity
                self.queue[self.back] = value


        self.size += 1
        if self.size == self.capacity:
            self.grow()

    def dequeue(self, front: bool = True) -> T:
        """
        Removes and returns an element from the CircularQueue.
        :param front: If True, removes and returns the front element; if False, removes and returns the back element.
        :return: The removed element, or None if the queue is empty.
        """
        if self.is_empty():
            return None

        if front:
            removed_item = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity

        else:

            removed_item = self.queue[self.back]
            self.back = (self.back - 1) % self.capacity

        self.size -= 1

        if self.size <= self.capacity // 4 and self.capacity // 2 >= 4:
            self.shrink()

        return removed_item

class CDLLNode:
    """
    Node for the CDLL
    """

    __slots__ = ['val', 'next', 'prev']

    def __init__(self, val: T, next: CDLLNode = None, prev: CDLLNode = None) -> None:
        """
        Creates a CDLL node
        :param val: value stored by the next
        :param next: the next node in the list
        :param prev: the previous node in the list
        :return: None
        """
        self.val = val
        self.next = next
        self.prev = prev

    def __eq__(self, other: CDLLNode) -> bool:
        """
        Compares two CDLLNodes by value
        :param other: The other node
        :return: true if comparison is true, else false
        """
        return self.val == other.val

    def __str__(self) -> str:
        """
        Returns a string representation of the node
        :return: string
        """
        return "<= (" + str(self.val) + ") =>"

    __repr__ = __str__

class CDLL:
    """
    A (C)ircular (D)oubly (L)inked (L)ist
    """

    __slots__ = ['head', 'size']

    def __init__(self) -> None:
        """
        Creates a CDLL
        :return: None
        """
        self.size = 0
        self.head = None

    def __len__(self) -> int:
        """
        :return: the size of the CDLL
        """
        return self.size

    def __eq__(self, other: 'CDLL') -> bool:
        """
        Compares two CDLLs by value
        :param other: the other CDLL
        :return: true if comparison is true, else false
        """
        n1: CDLLNode = self.head
        n2: CDLLNode = other.head
        for _ in range(self.size):
            if n1 != n2:
                return False
            n1, n2 = n1.next, n2.next
        return True

    def __str__(self) -> str:
        """
        :return: a string representation of the CDLL
        """
        n1: CDLLNode = self.head
        joinable: List[str] = []
        while n1 is not self.head:
            joinable.append(str(n1))
            n1 = n1.next
        return ''.join(joinable)

    __repr__ = __str__

    # ============ Modifiy Functions Below ============#

    def insert(self, val: T, front: bool = True) -> None:
        """
        Inserts a new node with the given value into the circular doubly linked list.
        :param val: The value to be inserted.
        :param front: If True, inserts the new node at the front of the list; if False, inserts it at the back.
        Returns: nothing
        """
        new_node = CDLLNode(val)

        if not self.head:
            new_node.next = new_node.prev = new_node
            self.head = new_node

        elif front:
            new_node.prev = self.head.prev
            new_node.next = self.head
            self.head.prev.next = new_node
            self.head.prev = new_node
            self.head = new_node

        else:
            new_node.prev = self.head.prev
            new_node.next = self.head
            self.head.prev.next = new_node
            self.head.prev = new_node

        self.size += 1

    def remove(self, front: bool = True) -> None:
        """
        Removes a node from the circular doubly linked list.
        :param front: If True, removes the node at the front of the list; if False, removes it at the back.
        Returns nothing
        """
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
            self.size = 0
            return
        if front:
            self.head.prev.next = self.head.next
            self.head.next.prev = self.head.prev
            self.head = self.head.next
        else:
            self.head.prev.prev.next = self.head
            self.head.prev = self.head.prev.prev
        self.size -= 1

class CDLLCD:
    """
    (C)ircular (D)oubly (L)inked (L)ist (C)ircular (D)equeue
    This is essentially just an interface for the above
    """

    def __init__(self) -> None:
        """
        Initializes the CDLLCD to an empty CDLL
        :return: None
        """
        self.CDLL: CDLL = CDLL()

    def __eq__(self, other: 'CDLLCD') -> bool:
        """
        Compares two CDLLCDs by value
        :param other: the other CDLLCD
        :return: true if equal, else false
        """
        return self.CDLL == other.CDLL

    def __str__(self) -> str:
        """
        :return: string representation of the CDLLCD
        """
        return str(self.CDLL)

    __repr__ = __str__

    # ============ Modifiy Functions Below ============#
    def __len__(self) -> int:
        """
        Returns the number of elements in the CDLLCD.
        :return: The number of elements in the circular doubly linked list.
        """
        return self.CDLL.size

    def is_empty(self) -> bool:
        """
        Checks if the CDLLCD is empty.
        :return: True if the circular doubly linked list is empty, False otherwise.
        """
        return self.CDLL.size == 0


    def front_element(self) -> T:
        """
        Returns the element at the front of the CDLLCD.
        :return: The element at the front, or None if the circular doubly linked list is empty.
        """
        if self.CDLL.head:
            return self.CDLL.head.val
        else:
            return None

    def back_element(self) -> T:
        """
        Returns the element at the back of the CDLLCD.
        :return: The element at the back, or None if the circular doubly linked list is empty.
        """
        if self.CDLL.head:
            return self.CDLL.head.prev.val
        else:
            return None

    def enqueue(self, val: T, front: bool = True) -> None:
        """
        Adds an element to the CDLLCD.
        :param val: The value to be added.
        :param front: If True, adds the value to the front; if False, adds it to the back.
        """
        self.CDLL.insert(val, front)

    def dequeue(self, front: bool = True) -> T:
        """
        Removes and returns an element from the CDLLCD.
        :param front: If True, removes and returns the front element; if False, removes and returns the back element.
        :return: The removed element, or None if the circular doubly linked list is empty.
        """
        if self.is_empty():
            return None
        value = self.front_element() if front else self.back_element()
        self.CDLL.remove(front)
        return value


def plot_speed():
    """
    Compares performance of the CDLLCD and the standard array based deque
    """

    # First we'll test sequences of basic operations

    sizes = [100*i for i in range(0, 200, 5)]

    # (1) Grow large
    grow_avgs_array = []
    grow_avgs_CDLL = []

    for size in sizes:
        grow_avgs_array.append(0)
        grow_avgs_CDLL.append(0)
        data = list(range(size))
        for trial in range(3):

            gc.collect()  # What happens if you remove this? Hint: memory fragmention
            cd_array = CircularDeque()
            cd_DLL = CDLLCD()

            # randomize data
            shuffle(data)

            start = default_timer()
            for item in data:
                cd_array.enqueue(item, item % 2)
            grow_avgs_array[-1] += (default_timer() - start)/3

            start = default_timer()
            for item in data:
                cd_DLL.enqueue(item, item % 2)
            grow_avgs_CDLL[-1] += (default_timer() - start)/3

    plt.plot(sizes, grow_avgs_array, color='blue', label='Array')
    plt.plot(sizes, grow_avgs_CDLL, color='red', label='CDLL')
    plt.title("Enqueue and Grow")
    plt.legend(loc='best')
    plt.show()

    # (2) Grow Large then Shrink to zero

    shrink_avgs_array = []
    shrink_avgs_CDLL = []

    for size in sizes:
        shrink_avgs_array.append(0)
        shrink_avgs_CDLL.append(0)
        data = list(range(size))

        for trial in range(3):

            gc.collect()
            cd_array = CircularDeque()
            cd_DLL = CDLLCD()

            # randomize data
            shuffle(data)

            start = default_timer()
            for item in data:
                cd_array.enqueue(item, item % 2)
            for item in data:
                cd_array.dequeue(not item % 2)
            shrink_avgs_array[-1] += (default_timer() - start)/3

            start = default_timer()
            for item in data:
                cd_DLL.enqueue(item, item % 2)
            for item in data:
                cd_DLL.dequeue(not item % 2)
            shrink_avgs_CDLL[-1] += (default_timer() - start)/3

    plt.plot(sizes, shrink_avgs_array, color='blue', label='Array')
    plt.plot(sizes, shrink_avgs_CDLL, color='red', label='CDLL')
    plt.title("Enqueue, Grow, Dequeue, Shrink")
    plt.legend(loc='best')
    plt.show()

    # (3) Test with random operations

    random_avgs_array = []
    random_avgs_CDLL = []

    for size in sizes:
        random_avgs_array.append(0)
        random_avgs_CDLL.append(0)
        data = list(range(size))

        for trial in range(3):

            gc.collect()
            cd_array = CircularDeque()
            cd_DLL = CDLLCD()

            shuffle(data)

            start = default_timer()
            for item in data:
                if randint(0, 3) <= 2:
                    cd_array.enqueue(item, item % 2)
                else:
                    cd_array.dequeue(item % 2)
            random_avgs_array[-1] += (default_timer() - start)/3

            start = default_timer()
            for item in data:
                if randint(0, 3) <= 2:
                    cd_DLL.enqueue(item, item % 2)
                else:
                    cd_DLL.dequeue(item % 2)
            random_avgs_CDLL[-1] += (default_timer() - start)/3

    plt.plot(sizes, random_avgs_array, color='blue', label='Array')
    plt.plot(sizes, random_avgs_CDLL, color='red', label='CDLL')
    plt.title("Operations in Random Order")
    plt.legend(loc='best')
    plt.show()

    def max_len_subarray(data, bound, structure):
        """
        returns the length of the largest subarray of `data` with sum less or eq to than `bound`
        :param data: list of integers to operate on
        :param bound: largest allowable sum
        :param structure: either a CircularDeque or a CDLLCD
        :return: the length
        """
        index, max_len, subarray_sum = 0, 0, 0
        while index < len(data):

            while subarray_sum <= bound and index < len(data):
                structure.enqueue(data[index])
                subarray_sum += data[index]
                index += 1
            max_len = max(max_len, subarray_sum)

            while subarray_sum > bound:
                subarray_sum -= structure.dequeue(False)

        return max_len

    # (4) A common application

    application_avgs_array = []
    application_avgs_CDLL = []

    data = [randint(0, 1) for i in range(5000)]
    window_lengths = list(range(0, 200, 5))

    for length in window_lengths:
        application_avgs_array.append(0)
        application_avgs_CDLL.append(0)

        for trial in range(3):

            gc.collect()
            cd_array = CircularDeque()
            cd_DLL = CDLLCD()

            start = default_timer()
            max_len_subarray(data, length, cd_array)
            application_avgs_array[-1] += (default_timer() - start)/3

            start = default_timer()
            max_len_subarray(data, length, cd_DLL)
            application_avgs_CDLL[-1] += (default_timer() - start)/3

    plt.plot(window_lengths, application_avgs_array,
             color='blue', label='Array')
    plt.plot(window_lengths, application_avgs_CDLL, color='red', label='CDLL')
    plt.title("Sliding Window Application")
    plt.legend(loc='best')
    plt.show()
