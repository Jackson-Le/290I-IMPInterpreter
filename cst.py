from imp_lexer import *

class Node:
    def __init__(self, value, type, parent = None, children = []):
        self.value = value
        self.type = type
        self.parent = parent
        self.children = children

    def to_string():
        print(value)

    def add_child(self, node):
        self.children.append(node)

    # i values of 0 drop operater, 1 drops left node, 2 drops right node
    def remove_child(self, i):
        self.children = self.children[:i] + self.children[i+1:]
