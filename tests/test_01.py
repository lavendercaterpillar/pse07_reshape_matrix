from main import reshape_matrix
import pytest

def test_reshape_4_2_to_2_4():
    nums = [[1,2],
            [3,4],
            [5,6],
            [7,8]]
    r = 2
    c = 4
    expected = [[1,2,3,4],
                [5,6,7,8]]

    result = reshape_matrix(nums, r, c)

    assert result == expected
    # We can also asser:
    assert result is not nums
    assert result(id) == expected(id)

def test_invalid_matrix_size():
    nums = [[1,2,3],[3,7]]
    r = 3
    c = 2
    expected = [[1,2,3],[3,7]]

    result = reshape_matrix(nums, r, c)

    assert result == expected

def test_indivisable_matrix_size():
    nums = [[1,2,3],[3,7,9]]
    r = 1
    c = 5
    expected = [[1,2,3],[3,7,9]]

    result = reshape_matrix(nums, r, c)

    assert result == expected


def test_empty_matrix():
    nums = [[1,2,3],[]]
    r = 2
    c = 2
    expected = [[1,2,3],[]]
    
    result = reshape_matrix(nums, r, c)

    assert result == expected

print("All Passed!")  # A good statement to include at the end of our tests