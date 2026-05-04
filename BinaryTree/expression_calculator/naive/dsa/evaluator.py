def evaluate_expressioin(expression: str) -> int | float:
    """
    Evaluate an arithmetic expression and return its result.

    Our Naive implementation to evaluate an arithmetic expression.

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

    return eval(expression)