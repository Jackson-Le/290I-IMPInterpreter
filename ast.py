from imp_lexer import *
from construct_cst import *
from test_cst_constuct import *


def ast(node):
    for i in range(len(node.children)):
        if node.children[i].type == 'OPERATOR':
            node.value = node.children[i].value
            node.type = node.children[i].type
            delete=i
    del(node.children[delete])
    for i in range(len(node.children)):
        if len(node.children[i].children) > 1:
            ast(node.children[i])


ast(xx)

#for i in range(len(x)):
print(xx.value)
print(xx.children[0].value)
print(xx.children[1].value)
print('break')
print(xx.children[0].children[0].value)
print(xx.children[0].children[1].value)
print(xx.children[1].children[0].value)
print(xx.children[1].children[1].value)

print('-------------------------------------')
