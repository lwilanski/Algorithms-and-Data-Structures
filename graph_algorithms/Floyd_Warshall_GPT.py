def floyd_warshall(graph):
    vertices = len(graph)

    # Initialize the distance matrix with infinity for all pairs except diagonal elements
    distance = [[float('inf') if i != j else 0 for j in range(vertices)] for i in range(vertices)]

    # Initialize the predecessor matrix with None for all pairs
    predecessor = [[None for j in range(vertices)] for i in range(vertices)]

    # Fill in the direct edge weights and set the corresponding predecessors
    for i, neighbors in enumerate(graph):
        for j, weight in neighbors:
            distance[i][j] = weight
            predecessor[i][j] = i

    # Iterate over all possible intermediate vertices
    for k in range(vertices):
        # Update the distance matrix considering all pairs of vertices (i, j)
        for i in range(vertices):
            for j in range(vertices):
                # Check if the path from i to j through k is shorter than the previously known path
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    predecessor[i][j] = predecessor[k][j]

    return distance, predecessor


def reconstruct_path(predecessor, start, end):
    if predecessor[start][end] is None:
        return None

    path = [end]
    while path[-1] != start:
        path.append(predecessor[start][path[-1]])
    path.reverse()

    return path
