from collections import deque


# Graph is represented as two-dimensional list of neighbors

def bfs(G, s):
    parents = [None] * len(G)
    visited = [False] * len(G)
    queue = deque([s])
    visited[s] = True

    while queue:
        vertex = queue.popleft()
        for neighbor in G[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parents[neighbor] = vertex
                queue.append(neighbor)

    return parents, visited


G = [[2], [2, 4], [0, 1, 3, 4], [2, 5], [1, 2], [3]]
print(bfs(G, 0))

# Explained version


def bfs(G, s):
    # G - list of adjacency lists representing the graph
    # s - start vertex

    # Initialize the parents list. This will keep track of the parent node
    # (i.e., the node we came from) for each node. We start with None for each node.
    parents = [None] * len(G)

    # Initialize the visited list. This keeps track of whether we've visited each node yet.
    # We start with False for each node (because we haven't visited any nodes yet).
    visited = [False] * len(G)

    # Create a queue and add the start node to it.
    queue = deque([s])

    # Mark the start node as visited.
    visited[s] = True

    # Continue until there are no more nodes in the queue.
    while queue:

        # Take the next node from the front of the queue.
        vertex = queue.popleft()

        # Loop over all the neighbors of the current node.
        for neighbor in G[vertex]:

            # If we haven't visited a neighbor yet, then do so.
            if not visited[neighbor]:

                # Mark the neighbor as visited.
                visited[neighbor] = True

                # The current node is the parent of its neighbor.
                parents[neighbor] = vertex

                # Add the neighbor to the end of the queue.
                queue.append(neighbor)

    # Return the parents and visited lists.
    return parents, visited

