from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.left_child: Optional[Node]  = None
        self.right_child: Optional[Node] = None


def infix_to_postfix(expression) -> list[str]:
    precedence = {'+':1, '-':1, '*':2, '/':2}
    stack = []
    output = []

    tokens = simplify_expression(expression).split()
    for token in tokens:
        if is_number(token):
            output.append(token)

        elif token == '(':
            stack.append(token)

        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()

        elif token in '+-*/':
            while (stack and stack[-1] != '(' and
                precedence.get(stack[-1], 0) >= precedence.get(token, 0)):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output


def create_expression_tree(expression: list[str]) -> Node:
    stack = []

    for item in expression:
        if item in '+-*/':
            node = Node(item)
            node.right_child = stack.pop()
            node.left_child = stack.pop()
        else:
            node = Node(float(item))
        stack.append(node)
    return stack.pop()

def calc(root_node: Node):
    current = root_node

    if current.data == '+':
        return calc(current.left_child) + calc(current.right_child)
    elif current.data == '-':
        return calc(current.left_child) - calc(current.right_child)
    elif current.data == '*':
        return calc(current.left_child) * calc(current.right_child)
    elif current.data == '/':
        return calc(current.left_child) / calc(current.right_child)
    else:
        return current.data

def simplify_expression(expression: str) -> str:
    result = ""
    for i in expression:
        if i.isalnum() or i == '.':
            result += i
        else:
            result = result + ' ' + i + ' '
    return result

def is_number(s) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False

def evaluate_expression(expression: str) -> tuple[int | float, Node]:
    postfix_expression = infix_to_postfix(expression)
    postfix_expression_tree_root_node = create_expression_tree(postfix_expression)
    return calc(postfix_expression_tree_root_node), postfix_expression_tree_root_node
