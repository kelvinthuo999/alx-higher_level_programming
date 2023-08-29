#!/usr/bin/python3
""" Definition of classes """


class Node:
    """
    This class defines a node of a singly linked list.
    Attributes:__data (int): The data stored in the node.
               __next_node (Node): The next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.
        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): The next node in the linked list.
                                       Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for retrieving the data of the node.
        Returns:int: The data stored in the node.
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        Setter method for setting the data of the node.
        Args:value (int): The new data for the node.
        Raises:TypeError: If value is not an integer.
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for retrieving the next node in the linked list.
        Returns:Node: The next node in the linked list.
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for setting the next node in the linked list.
        Args:value (Node): The new next node.
        Raises:TypeError: If value is not None or not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class defines a singly linked list.
    Attributes:head: The head node of the linked list.
    """

    def __init__(self):
        """
        Initializes a new instance of the SinglyLinkedList class.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list.
        Args:value (int): The value of the new Node.
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.
        """
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return ('\n'.join(values))
