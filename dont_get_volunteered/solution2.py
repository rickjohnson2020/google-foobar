squere_list = [(row, col) for row in range(8) for col in range(8)]
squere_num_list = [num for num in range(64)]

conversion_table = dict(zip(squere_num_list, squere_list))

all_moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]


class Node():
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent


class QueueFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


def solution(src, dest):
    """
    Return the smallest number of moves that connect the source to the destination
    using a chess knight's moves.

    If no possible path, return None.
    """

    # cnvert source number and destination number to coordinates
    source = conversion_table[src]
    destination = conversion_table[dest]

    # keep track of number of states explored
    num_explored = 0

    # Initialize frontier to just the starting source
    start = Node(state=source, parent=None)
    frontier = QueueFrontier()
    frontier.add(start)

    # Initialize am empty explored set
    explored = set()

    # Keep looping until solution found
    while True:

        # If nothing left in frontier, then no solution
        if frontier.empty():
            raise Exception("no solution")

        # Choose a node from the frontier
        node = frontier.remove()
        num_explored += 1

        # If node is the destination, then we have a solution
        if node.state == destination:
            return num_explored

        # Mark node as explored
        explored.add(node.state)

        # Add neighbors to frontier
        for state in neighbors(node.state):
            if not frontier.contains_state(state) and state not in explored:
                child = Node(state=state, parent=node)
                frontier.add(child)


def neighbors(current_state):
    (row, col) = current_state
    possible_moves = [(row + m_row, col + m_col) for (m_row, m_col) in all_moves if row + m_row >= 0 and col + m_col >= 0]

    return possible_moves
