def or_op(x1, x2):
    return x1 or x2

def and_op(x1, x2):
    return x1 and x2

def xor_op(x1, x2):
    return or_op(x1, x2) and not and_op(x1, x2)

# Тестування
inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
print("x1 x2 | xor(x1, x2)")
print("-------------------")
for x1, x2 in inputs:
    print(f"{x1}  {x2}  | {xor_op(x1, x2)}")
