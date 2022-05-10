"""
###JigSaw Puzzle
# Possible Objects: JigSaw, piece
# A piece gotta fit with all those surrounding it. 
# A piece could be surrounded by 2(corner), 3(edge), or 4(middle) pieces.
# Assume that a Jigsaw piece fits only in one place.
# We have a one dimension array to hold all the pieces.
# We are going to have a linkedlist representing the solved puzzle
# We are going to select a random starting piece.
"""

import enum
    

class Edge(enum.Enum):
    Point = 1
    Hole = 0
    Flat = 2


class Piece:
    """
    Represents a JigSaw piece. It has pointers to the pieces on all directions.
    The edges have 1 if they are pointy and a 0 if they are holed.
    """
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None
        self.topEdge = Edge.Point
        self.bottomEdge = Edge.Point
        self.leftEdge = Edge.Hole
        self.rightEdge = Edge.Hole

class JigSaw:
    def __init__(self, pieces) -> None:
        self.pieces = pieces
        self.startPiece = None

    
    def fits_with(firstEdge: Edge, secondEdge: Edge):
        """
        It retuns true if the edges fit together, 
        which means if one is 0 and one is 1
        """
        if firstEdge.value == Edge.FLAT or secondEdge.value == Edge.Flat:
            return False

        return firstEdge ^ secondEdge

    def solve(self):
        """
        It selects a random piece as the start piece.
        It adds it to a q
        it loops through that piece's edges, and for each edge it loops through all other pieces
        that are not in the q, to find a piece with an edge that fits the current edge. 
        Once found, it add's that piece to the q, set's the current piece's direction pointer to it. Then moves on 
        to the next edge.
        When a piece is checking for it's right, it needs to confirm that the candidate right neighbour fits with 
        it's bottom neghbour's right neghbour's top edge
        When a piece is checking for it's left, it needs to confirm that the candidate left neighbour fits with 
        it's bottom neghbour's left neghbour's top edge
        The two steps above needs to be repeated with different neghbours for other pieces
        """
        return self.startPiece