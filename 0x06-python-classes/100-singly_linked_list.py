#!/usr/bin/python3
"""defines a Node"""


class Node:
    """Representation of a Node"""

    def __init__(self, data, next_node=None):
        """initializes node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

    def __str__(self):
        return str(self.__data)


"""defines a single linked list"""


class SinglyLinkedList:
    """representation of a single linked list"""

    def __init__(self):
        """initializes single linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """insterts a new Node in the correct position"""
        new_node = Node(value)
        tmp = self.__head
        if tmp is None or tmp.data >= value:
            if tmp:
                new_node.next_node = tmp
            self.__head = new_node
            return
        else:
            while tmp.next_node is not None:
                if tmp.next_node.data >= value:
                    break
                tmp = tmp.next_node
            new_node.next_node = tmp

    def __str__(self):
        string = str()
        tmp = self.__head
        while tmp is not None:
            string += str(tmp)
            if tmp.next_node is not None:
                string += "\n"
            tmp = tmp.next_node
        return string
