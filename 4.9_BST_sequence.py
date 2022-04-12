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
        tempRight = list((x for x in perm if x in rightArray))
        if tempLeft == leftArray and tempRight == rightArray:
            validPerms.append(list(perm))

    return list(validPerms)



def main():
    root = TreeNode(8)
    root.left = TreeNode(5)
    root.left.left = TreeNode(1)
    root.right = TreeNode(9)
    root.right.right = TreeNode(12)
    
    sequences = get_sequences(root)
    print(sequences)



if __name__ == '__main__':
    main()