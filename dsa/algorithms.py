# Depth First Search

# traverse all adjacent vertices one by one before backtracking
# when trasversing adjacent vertex, finish traversal of all vertices reachable through that adjacent vertex
# graphs may have loops, so use a visited array/stack to track current search path

# rows, cols = len(adj), len(adj[0])

print("--- Depth First Search ---")
def dfsRec(adj, visited, s, res):
	visited[s] = True
	res.append(s)

	# recursively visit all adjacent vertices that are not visited yet
	for i in range(len(adj)):
		if adj[s][i] == 1 and not visited[i]: # if adj, = 1, else = 0
			dfsRec(adj, visited, i, res)

def DFS(adj):
	# check for empty matrix
	if not adj:
		return []

	visited = [False] * len(adj)
	res = [] # travel path
	dfsRec(adj, visited, 0, res)  # Start DFS from vertex 0
	return res


def add_edge(adj, s, t):
    adj[s][t] = 1
    adj[t][s] = 1  # Since it's an undirected graph


# Driver code
V = 5
adj = [[0] * V for _ in range(V)]  # Adjacency matrix

print("Initial matrix:")
for item in adj:
	print(item)
# Define the edges of the graph
edges = [(1, 2), (1, 0), (2, 0), (2, 3), (2, 4)]

# Populate the adjacency matrix with edges
for s, t in edges:
    add_edge(adj, s, t)


print("Final matrix:")
for item in adj:
	print(item)

res = DFS(adj)  # Perform DFS
print(" ".join(map(str, res)))

# T: O(V + E) V = # of vertices, E = # of edges
# S: O(V + E) visited array of size V + stack size for recursive calls

print("--- Depth First Search END ---")

# Breath First Search

# start at a node, then traverses all its adjacent nodes before moving to nodes at next depth
# once all adjacent aree visited, then their adjacent are traversed
# detect cycle in directed and undirected graphs, find shortest path, etc.
# graphs may have loops, so use a visited double-ended queue to track (dequeuing O(1))

print("--- Breath First Search ---")
from collections import deque

def bfs(adj):
	# check for empty matrix
	if not adj:
		return []

	# get number of vertices
	V = len(adj)

	# create array to store traversal
	res = []
	s = 0

	# create queue for BFS
	q = deque()

	# initially mark all vertices as not visited
	visited = [False] * V

	# mark source node as visited and enqueue it
	visited[s] = True
	q.append(s)

	# iterate over queue
	while q:

		# dequeue vertex from queue and store it
		curr = q.popleft()
		res.append(curr) # travel curr

		# get all adjacent vertices of dequeued vertex curr
		# if an adjacent has not been visited,
		# mark it visited and enqueue it
		for x in adj[curr]:
			if not visited[x]:
				visited[x] = True
				q.append(x)

	return res

# create the adjacency list
# [ [2, 3, 1], [0], [0, 4], [0], [2] ]
adj = [[1,2], [0,2,3], [0,4], [1,4], [2,3]]
ans = bfs(adj)
for i in ans:
    print(i, end=" ")p;

# T: O(V + E), BFS explores all vertices and edges, V = # of veertices, E = # of edges
# S: O(V), worse case queue contains all vertices

print("--- Breath First Search END ---")
# preorder
# root -> left -> right

# inorder
# left -> root -> right

# postorder
# left -> right -> root

print("--- Binary Search ---")

class Solution:
	def binSeach(self, nums: List[int], target: int) -> int:
		# set left and right pointers
		left, right = 0, len(nums) - 1

		while left <= right:
			mid = (left + right) // 2

			# case 1: target at mid
			if nums[mid] == target:
				return mid

			# case 2: target on LHS of mid
			if nums[mid] > target:
				right = mid - 1

			# case 3: target on RHS of mid
			else:
				left = mid + 1

		return -1

# T: O(logn) - nums divided into half each time
# S: O(1)

# https://leetcode.com/problems/search-in-rotated-sorted-array/
