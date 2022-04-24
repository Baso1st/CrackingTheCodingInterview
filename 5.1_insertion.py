
def bit_insertion(n, m, i, j):
    """
    It inserts m into in at location i. It expects n and m to be string represing binary values
    Time Complexity: O(m)
    Space Complexity: O(1)
    """
    n = int(n, 2)
    m = int(m, 2)

    for k in range(i, j+1):
        n = clear_ith_bit(n, k)
        if bin(m)[k - i - 2] == '1':
            n = set_ith_bit(n, k)

    return bin(n)[2:]


def bit_insertion_with_mask(n, m, i, j):
    """
    It inserts m into in at location i. It expects n and m to be string represing binary values
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    n = int(n, 2)
    m = int(m, 2)
    left_mask = ~0 << (j + 1)
    right_mask = (1 << i) - 1
    mask = left_mask | right_mask

    n_cleared = n & mask
    m_shifted = m << i

    return bin(n_cleared | m_shifted)[2:]


def clear_ith_bit(num, i):
    mask = ~(1 << i)
    return num & mask


def set_ith_bit(num, i):
    mask = (1 << i)
    return num | mask


def main():
    # assert bit_insertion('10000000000', '10011', 2, 6) == '10001001100'
    # assert bit_insertion('11111111111', '10011', 2, 6) == '11111001111'
    assert bit_insertion_with_mask('10000000000', '10011', 2, 6) == '10001001100'

if __name__ == '__main__':
    main()