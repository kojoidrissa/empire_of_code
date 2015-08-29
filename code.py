#Binary count challenge code
def count_units(number):
    binary = bin(number)
    binary_count = binary.count('1')
    return binary_count

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_units(4) == 1
    assert count_units(15) == 4
    assert count_units(1) == 1
    assert count_units(1022) == 9

    print("Use 'Check' to earn sweet rewards!")
    