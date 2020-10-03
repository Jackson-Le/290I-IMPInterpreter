from imp_lexer import *
from construct_cst import *

x = imp_lex('(+,(-,3,1),(*,2,1))')
y = imp_lex('(+,3,(*,2,1))')
z = imp_lex('(+,(-,3,1),1)')
i = imp_lex('(+,2,3)')

print('this is x:')
xx = buildCST(x)

print('this is y:')
yy = buildCST(y)

print('this is z:')
zz = buildCST(z)

print('this is i:')
ii = buildCST(i)

def treeWalker(tree):
    if type(tree.value) != str:
        print(tree.type)
        for node in tree.children:
            treeWalker(node)
    else:
        print(tree.type)
        print(tree.value)
