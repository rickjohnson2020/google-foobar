import heapq
from collections import defaultdict

# define chessboard parameters
BOARD_SIZE      = 8
BOARD_MOVES = [(1, 2), (1, -2), (-1, 2), (-1, -2),
               (2, 1), (2, -1), (-2, 1), (-2, -1)]

class Node:
    def __init__(self, row, col, distance=0):
        self.row = row
        self.col = col
        self.distance = distance
    
    def __hash__(self):
        return hash(tuple(self))
    
    def __iter__(self):
        for i in [self.row, self.col]:
            yield i
    
    def __eq__(self, node):
        return self.row == node.row and self.col == node.col
    
    def __str__(self):
        return "<Node (row=%d, col=%d, d=%.02f)>" % (self.row, self.col, self.distance)

    def __repr__(self):
        return self.__str__()

class Board:
    def __init__(self, size, moves):
        self.size = size
        self.moves = moves

    def node(self, position):
        """ Generate Node for given position """
        return Node(int(position / self.size), int(position % self.size))

    def valid(self, row, col):
        if 0 <= row < self.size and 0 <= col < self.size:
            return True
        else:
            False

    def distance(self, start, end):
        """ Find shortest distance using BFS """
        queue = []
        queue.append(start)
        visited = {}

        # run until queue is empty
        while queue:
            # grab first node in queue
            node = queue.pop(0)

            # return when destination is reached
            if node == end:
                return node.distance

            # process nodes that have not been visited
            if node not in visited:
                # mark node as visited
                visited[node] = True

                # validate piece movement
                for move in self.moves:
                    row, col = list(tuple(x + y for x, y in zip(tuple(node), move)))

                    # queue valid moves only
                    if self.valid(row, col):
                        queue.append(Node(row, col, node.distance + 1))

        return float('inf')

def solution(src, dest):
    # create chessboard graph
    chessboard = Board(size = BOARD_SIZE, moves = BOARD_MOVES)

    # create coordinates
    start = chessboard.node(src)
    end = chessboard.node(dest)

    # calculate distance between given positions
    distance = chessboard.distance(start, end)

    return distance
