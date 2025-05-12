from main import reshape_matrix
import pytest

def test_reshape_matrix_valid_case():
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


def test_invalid_matrix_size():
    nums = [[1,2,3],[3,7]]
    r = 3
    c = 2
    expected = [[1,2,3],[3,7]]

    result = reshape_matrix(nums, r, c)

    assert result == expected


def test_empty_matrix():
    nums = [[1,2,3],[]]
    r = 2
    c = 2
    expected = [[1,2,3],[]]
    
    result = reshape_matrix(nums, r, c)

    assert result == expected
