def multiply_list(elements: list, n: float = 2) -> list:
    return [el * n for el in elements]

lambda_multiply_list = lambda elements, n = 2: [el * n for el in elements]

result_def = multiply_list([1.5, 2, 3.5], 3)
result_lambda = lambda_multiply_list([1.5, 2, 3.5], 3)

print(result_def)
print(result_lambda)
