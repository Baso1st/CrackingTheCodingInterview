

def one_away(first, second):
    if first == second:
        return True
    if abs(len(first) - len(second)) >= 2:
        return False
    
    if len(second) < len(first): #Insert a character
        for i in range(len(second)):
            if first[i] != second[i]:
                second = second[:i] + first[i] + second[i:]  
                return first == second
        second += first[-1]
        return first == second
    elif len(second) > len(first): #Remove a character
        for i in range(len(first)):
            if first[i] != second[i]:
                second = second[:i] + second[i+1:]
                return first == second
        second = second[:-1]
        return first == second    
    else: #Replace a character
        for i in range(len(first)):
            if first[i] != second[i]:
                second = second[:i] + first[i] + second[i+1:]
                return first == second
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