from copy import copy, deepcopy
import itertools
from DataStructureInPython.binarySearchTree import BinarySearchTree, TreeNode


def get_sequences(node: TreeNode):
    """ It returns all possible arrays that could have led to the tree.
        Time Complexity: Something terrible like O(N*N!) 
        Space Complexity: ....
    """
    if not node.left and not node.right:
        return [[node.data]]

    possibilities = []
    leftPerms = [[]]
    rightPerms = [[]]
    if node.left:
        leftPerms = get_sequences(node.left)
    if node.right:
        rightPerms = get_sequences(node.right)
    
    for leftPerm in leftPerms:
        for rightPerm in rightPerms:
            possibilities += _get_possible_sequences(leftPerm, rightPerm)

    for poss in possibilities:
        poss.insert(0, node.data)
    
    return possibilities


def _get_possible_sequences(leftArray: list, rightArray: list):
    theArray = leftArray + rightArray
    perms = list(itertools.permutations(theArray))
    validPerms = []
    for perm in perms:
        tempLeft = list((x for x in perm if x in leftArray))
        if tempLeft != leftArray:
            continue
        tempRight = list((x for x in perm if x in rightArray))
        if tempRight != rightArray:
            continue
        validPerms.append(list(perm))

    return list(validPerms)



def main():
    # root = TreeNode(8)
    # root.left = TreeNode(5)
    # root.left.left = TreeNode(1)
    # root.right = TreeNode(9)
    # root.right.right = TreeNode(12)
    node50 = TreeNode(50)
    node20 = TreeNode(20)
    node60 = TreeNode(60)
    node10 = TreeNode(10)
    node25 = TreeNode(25)
    node70 = TreeNode(70)
    node5 = TreeNode(5)
    node15 = TreeNode(15)
    node65 = TreeNode(65)
    node80 = TreeNode(80)
    
    node50.left = node20
    node50.right = node60
    node20.left = node10
    node20.right = node25
    node60.right = node70
    node10.left = node5
    node10.right = node15
    node70.left = node65
    node70.right = node80

    sequences = get_sequences(node50)
    print(len(sequences))
    # print(len(_get_possible_sequences([1, 2, 3, 4, 5], [11, 12, 13, 14, 15] )))



if __name__ == '__main__':
    main()