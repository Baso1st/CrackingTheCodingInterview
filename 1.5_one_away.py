

def one_away(first, second):
    if first == second:
        return True
    if abs(len(first) - len(second)) >= 2:
        return False

    found_difference = False

    if len(first) == len(second): # Replace a character
        for i in range(len(first)):
            if first[i] != second[i]:
                if found_difference:
                    return False
                found_difference = True
        return True

    # Insert or remove
    if len(first) < len(second):
        second, first = first, second

    firstIndex = secondIndex = 0

    while secondIndex < len(second):
        if first[firstIndex] != second[secondIndex]:
            if found_difference:
                return False
            firstIndex += 1
            found_difference = True 
            continue
        firstIndex += 1
        secondIndex += 1
    return True



test_cases = [
    # no changes
    ("pale", "pale", True),
    ("", "", True),
    # one insert
    ("pale", "ple", True),
    ("ple", "pale", True),
    ("pales", "pale", True),
    ("ples", "pales", True),
    ("pale", "pkle", True),
    ("paleabc", "pleabc", True),
    ("", "d", True),
    ("d", "de", True),
    # one replace
    ("pale", "bale", True),
    ("a", "b", True),
    ("pale", "ble", False),
    # multiple replace
    ("pale", "bake", False),
    # insert and replace
    ("pale", "pse", False),
    ("pale", "pas", False),
    ("pas", "pale", False),
    ("pkle", "pable", False),
    ("pal", "palks", False),
    ("palks", "pal", False),
    # permutation with insert shouldn't match
    ("ale", "elas", False),
]

for case in test_cases:
    if one_away(case[0], case[1]) != case[2]:
        print(case)