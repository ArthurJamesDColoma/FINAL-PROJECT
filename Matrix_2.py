import numpy as np

array = np.array([[1, 2, 3], 
                  [4, 5, 6], 
                  [7, 8, 9]])

row_sums = array.sum(axis=1)
col_sums = array.sum(axis=0)

result_str = ""

for row in array:
    row_str = " ".join(map(str, row))
    result_str += f"{row_str} | {row.sum()}\n"

result_str += "- " * array.shape[1] + "\n"

result_str += " ".join(map(str, col_sums)) + "\n"

print(result_str)
