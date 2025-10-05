# matrix_drills.py
# --- BEGINNER ---

def make_zeros(n_rows: int, n_cols: int):
    """Return an n_rows x n_cols matrix of zeros."""
    # TODO: build using list comprehension
    matrix =  [[0 for i in range(n_cols)] for i in range(n_rows)]
    return matrix

 


def get_cell(matrix, r, c):
    """Return value at row r, col c (0-indexed)."""
    # TODO: direct indexing
    return matrix[r][c]
    


def row_elements(matrix, r):
    """Return a NEW list with all elements from row r (do NOT print)."""
    # TODO: slice or iterate
    return matrix[r][0:]


def last_col_elements(matrix):
    """Return a list of elements from the last column (top→bottom)."""
    # TODO: iterate rows, pick last item
    arr = []
    for i in range(len(matrix)):
        arr.append(matrix[i][-1])
    return arr
    

def flatten_row_major(matrix):
    """Return all elements row-by-row as a single list."""
    # TODO: nested loops or itertools.chain
    arr = []
    for i in (range(len(matrix))):
        for j in range(len(matrix[i])):
            arr.append(matrix[i][j])
    return arr
    


def row_sum(matrix, r):
    """Sum of row r."""
    # TODO: built-in sum
    sum1 = 0
    for i in range(len(matrix[r])):
      sum1 += matrix[r][i]
    return sum1


def col_sum(matrix, c):
    """Sum of column c (assume all rows same length)."""
    # TODO: loop rows; add matrix[i][c]
    sum1 = 0
    for i in range(len(matrix)):
        sum1 += matrix[i][c]
    return sum1

    


# --- EARLY INTERMEDIATE ---

def transpose(matrix):
    """Return the transpose (rows <-> cols)."""
    # TODO: zip(*) or nested loops
   
    
    arr = []
    for i in range(len(matrix)):
        arr1 = []
        for j in range(len(matrix[i])):
            arr1.append(matrix[i][j])
            arr1.append(matrix[j][i])
        arr.append(arr1)
    return arr



def row_min_max(matrix):
    """Return list of (min, max) for each row in order."""
    # TODO: loop rows; use min()/max()
    raise NotImplementedError


def col_with_largest_sum(matrix):
    """Return the index of the column with the largest sum (ties: smallest index)."""
    # TODO: compute each column sum; track best
    raise NotImplementedError


def main_diag_sum(square):
    """Sum main diagonal (i == j). Assume square matrix."""
    # TODO: sum(square[i][i] for i in range(n))
    raise NotImplementedError


def anti_diag_sum(square):
    """Sum anti-diagonal (i + j == n-1). Assume square matrix."""
    # TODO: sum(square[i][n-1-i] ...)
    raise NotImplementedError


def scalar_multiply(matrix, k):
    """Return NEW matrix where every element is multiplied by k."""
    # TODO: nested list comps
    raise NotImplementedError


def add_matrices(A, B):
    """Return A + B assuming same shape."""
    # TODO: elementwise sum
    raise NotImplementedError


def matmul(A, B):
    """Classic matrix multiplication: A(m x n) * B(n x p) -> (m x p)."""
    # TODO: triple loop or dot-product with sum()
    raise NotImplementedError


# ----------------- TESTS -----------------
def _run_tests():
    # basic data
    M = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    N = [
        [10, 0, -1],
        [3,  5,  2],
        [0,  0,  4],
    ]

    # Beginner
    assert make_zeros(2,3) == [[0,0,0],[0,0,0]]
    assert get_cell(M, 1, 2) == 6
    assert row_elements(M, 0) == [1,2,3]
    assert last_col_elements(M) == [3,6,9]
    assert flatten_row_major([[1,2],[3,4]]) == [1,2,3,4]
    assert row_sum(M, 2) == 24
    assert col_sum(M, 1) == 15

    # Early intermediate
    assert transpose([[1,2,3],[4,5,6]]) == [[1,4],[2,5],[3,6]]
    assert row_min_max(M) == [(1,3), (4,6), (7,9)]
    assert col_with_largest_sum(M) == 2  # sums: [12,15,18]
    assert main_diag_sum(M) == 15
    assert anti_diag_sum(M) == 15
    assert scalar_multiply([[1,-2],[0,3]], -2) == [[-2,4],[0,-6]]
    assert add_matrices(M, N) == [[11,2,2],[7,10,8],[7,8,13]]

    A = [[1,2,3],[4,5,6]]      # 2x3
    B = [[7,8],[9,10],[11,12]] # 3x2
    assert matmul(A,B) == [[58,64],[139,154]]

    print("✅ All tests passed!")


if __name__ == "__main__":
    _run_tests()
