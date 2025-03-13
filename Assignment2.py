# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
   

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    return sorted(set(numbers))

# Test case for remove_duplicates_and_sort() function
def test_remove_duplicates_and_sort():
    assert remove_duplicates_and_sort([3, 1, 2, 3, 4, 2, 5]) == [1, 2, 3, 4, 5]
    assert remove_duplicates_and_sort([10, 10, 9, 8, 7, 7]) == [7, 8, 9, 10]
    assert remove_duplicates_and_sort([]) == []
    print("All tests passed!")

# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    result = []
    current_sum = 0
    for num in arr:
        current_sum += num
        result.append(current_sum)
    return result

# Test case for cumulative_sum() function
def test_cumulative_sum():
    assert cumulative_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert cumulative_sum([10, -2, 3, 5]) == [10, 8, 11, 16]
    assert cumulative_sum([]) == []
    print("All tests passed!")

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    if not matrix:
        return []
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

# Test case for transpose_matrix() function
def test_transpose_matrix():
    assert transpose_matrix([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    assert transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert transpose_matrix([]) == []
    print("All tests passed!")

# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    if step <= 0:
        raise ValueError("Step value must be greater than 0")
    return lst[::step]

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("The lists must have the same length.")
    
    return sum(a * b for a, b in zip(list1, list2))

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in matrix1 must be equal to number of rows in matrix2")
    
    # Initialize result matrix with zeros
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    # Perform matrix multiplication
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            result[i][j] = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))
    
    return result