def evaluate_expression(expression: str):
    """
    Evaluate an arithmetic expression and return its result.

    Your task is to implement an algorithm of your choice to compute
    the value of the given expression. You may use any data structure
    (e.g., stack, queue, tree) and approach (e.g., parsing, recursion,
    or built-in methods where appropriate).

    Requirements:
        - Support basic arithmetic operators: +, -, *, /
        - Handle operator precedence correctly
        - Handle parentheses (e.g., "(2 + 3) * 4")
        - Handle decimal numbers (e.g., "(4.3 + 2) / 9.43)")
        - Accept expressions with or without spaces (e.g., "( 3 + 1 ) / 5" and "(3+1) /5")
        - Assume the input is a valid expression
        - Return the final result, to be displayed.

    Params:
        expression (str): A string containing the arithmetic expression.

    Returns:
        Any : The evaluated result of the expression.

    Example:
        >>> evaluate_expression("3 + 5 * 2")
        13

        >>> evaluate_expression("(1 + 2) * 4")
        12
    """

    #TODO: Code your solution here! 