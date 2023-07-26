"""
If the current token is a '(', add a new node as the left child of the current node, and descend to the left child.

If the current token is in the list ['+','-','/','*'], set the root value of the current node to the operator
represented by the current token. Add a new node as the right child of the current node and descend to the right child.

If the current token is a number, set the root value of the current node to the number and return to the parent.

If the current token is a ')', go to the parent of the current node.
"""

#Just using these precreated data structures as opposed to building from scractch
from pythonds.basic import Stack
from pythonds.trees import BinaryTree
import operator

def evaluate(parse_tree):
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    left = parse_tree.getLeftChild()
    right = parse_tree.getRightChild()

    if left and right:
        func = ops[parse_tree.getRootVal()]
        return func(evaluate(left), evaluate(right))
    else:
        return parse_tree.getRootVal()

def build_parse_tree(exp):
    L = exp.split()
    exp_stack = Stack()
    exp_tree = BinaryTree('')
    exp_stack.push(exp_tree)
    current_tree = exp_tree

    for i in L:
        if i == '(':
            current_tree.insertLeft('')
            exp_stack.push(current_tree)
            current_tree = current_tree.getLeftChild()
        elif i in ['+','-','*','/']:
            current_tree.setRootVal(i)
            current_tree.insertRight('')
            exp_stack.push(current_tree)
            current_tree = current_tree.getRightChild()
        elif i == ')':
            current_tree = exp_stack.pop()
        elif i not in ['+','-','*','/', ')']:
            try:
                current_tree.setRootVal(int(i))
                parent = exp_stack.pop()
                current_tree = parent
            except ValueError:
                raise ValueError("toke '{}' is not a valid integer".format(i))
    return exp_tree

e = build_parse_tree("( ( 10 + 5 ) * 3 )")

print(evaluate(e))






