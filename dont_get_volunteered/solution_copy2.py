from collections import deque


# Define Node struct cause we're gonna use it in our graph
class Node:
	def __init__(self, x, y, dist):
		self.x = x
		self.y = y
		self.dist = dist
		self.visited = False

	def __eq__(self, other):
		if isinstance(self, other.__class__):
			return self.x == other.x and self.y == other.y
		return False


# Define the chessboard
class ChessBoard:
	# Define all valid moves
	row = [2, 2, -2, -2, 1, 1, -1, -1]
	col = [-1, 1, -1, 1, 2, -2, -2, 2]

	def __init__(self):
		# Init the chessboard as given in the readme
		self.board = [[0 for _ in range(8)] for _ in range(8)]
		counter = 0
		for i in range(8):
			for j in range(8):
				self.board[i][j] = counter
				counter += 1

	# Helper to check if given coordinates are valid
	@classmethod
	def isValidCoord(self, x, y):
		return False if x < 0 or y < 0 or x > 7 or y > 7 else True

	# Helper to convert position (0-63) to coordinates (x,y)
	def posToCoord(self, pos):
		for i in range(8):
			for j in range(8):
				if self.board[i][j] == pos:
					return (i, j)
		return (0, 0)


# Performs a breadth-first search on the Chessboard
def sho_me_da_wei(src, dest):
	queue = deque([])
	queue.append(src)
	while not len(queue) == 0:
		node = queue.popleft()
		x = node.x
		y = node.y
		dist = node.dist
		if node == dest:
			return dist
		if not node.visited:
			node.visited = True
			for i in range(8):
				new_x = x + ChessBoard.row[i]
				new_y = y + ChessBoard.col[i]
				if ChessBoard.isValidCoord(new_x, new_y):
					new_node = Node(new_x, new_y, dist + 1)
					queue.append(new_node)
	return -1


def answer(src, dest):
	chessboard = ChessBoard()
	(src_x, src_y) = chessboard.posToCoord(src)
	(dest_x, dest_y) = chessboard.posToCoord(dest)
	src_node = Node(src_x, src_y, 0)
	dest_node = Node(dest_x, dest_y, 0)
	return sho_me_da_wei(src_node, dest_node)
