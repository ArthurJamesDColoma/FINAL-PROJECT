matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def transpose(matrix):
    transposed_matrix = []
    for col in range(len(matrix[0])):
        new_row = []
        for row in matrix:
            new_row.append(row[col])
        transposed_matrix.append(new_row)
    return transposed_matrix

transposed_matrix = transpose(matrix)

for row in transposed_matrix:
    print(row)
