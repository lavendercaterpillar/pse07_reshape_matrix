'''
Clarifying question
1- Should all items in mat be the same length? Yes
2- How does the function handle the invalid input? It returns the original array
Here are some example clarifying questions:
    Are there any constraints on matrix sizes?
    Can a matrix have 1 row or 1 column?
    What if the matrix is empty or None?
'''

# input validation 
# Constriants:The height and width of the given matrix is in range [1, 100]. The given r and c are all positive.
# checkes if the length of all items in nums are the same length
# calculates the length of the matrix and finds the number of its rows and columns.
# checks if the number of columns in output matrix a divisor of row * column.
# Makes a consolidated list of all items in one row (flatten the list)
# Slices the full length list into smaller arrays with length = new column size (c)

def get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


def reshape_matrix(mat, r,c):
    
    rows = len(mat)
    cols = len(mat[0]) if mat else 0
    length = rows * cols

    if rows not in range(100) or cols not in range(100):
        raise ValueError("Please input a matrix with maximum size of 100 x 100")

    if c not in get_divisors(length) or r * c > length:
        return mat
    
    if any(len(item) != len(mat[0]) for item in mat):
        return mat
    
    # Flatten the original 2D list
    # SC: O(n) = n, TC: O(n)= n
    flat = [x for row in mat for x in row] # list comprehension

    # flat = []
    # for row in mat:
    #     for x in row:
    #         flat.append(x)

    # Reshape into r x c
    reshaped = [flat[i:i+c] for i in range(0, len(flat), c)]

    return reshaped


# nums = [[1,2],[3,4]]
# r = 2, c = 4

nums = [[1,2,3],[3,7,4]]
r = 3
c = 2

nums = [[1,2],
[3,4],
[5,6],
[7,8]]
r = 2
c = 4

print(reshape_matrix(nums, r,c))