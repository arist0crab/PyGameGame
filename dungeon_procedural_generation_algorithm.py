"""
Realisation of procedural dungeon generation
Explanation to the algorithm (the first part of the video): https://www.youtube.com/watch?v=rBY2Dzej03A
"""

import igraph as ig
import numpy as np
from scipy.spatial import Delaunay

# region """Adjustable parameters of dungeon generation"""
SIZE = 50, 50
ROOM_MIN_SCALE = 4
ROOM_MAX_SCALE = 10
ROOM_MIN_QUANTITY = 4
ROOM_MAX_QUANTITY = 7
ADDITIONAL_CORRIDOR_PROBABILITY = 0.125
PADDING = 10
SPACING = 5
# endregion

# region """Non-adjustable parameters of dungeon generation"""
grid = [[-1 for x in range(SIZE[0] + 1)] for y in range(SIZE[1] + 1)]
rooms = []
# endregion


class Room:
    """ Room class to store rooms' coordinates and scales properly """

    def __init__(self, index):

        """ Init of room class. Will automatically generate new room on the map. Needs index of room """

        self.id = index
        placing = True
        x, y = 0, 0
        w, h = 0, 0

        while placing:
            placing = False

            x, y = np.random.randint(PADDING, SIZE[0] - PADDING), np.random.randint(PADDING, SIZE[1] - PADDING)
            w, h = np.random.randint(ROOM_MIN_SCALE, ROOM_MAX_SCALE), np.random.randint(ROOM_MIN_SCALE, ROOM_MAX_SCALE)

            for room in rooms:
                r1 = [x, y, x + w, y + h]
                r2 = [room.x - SPACING, room.y - SPACING, room.x + room.w + SPACING, room.y + room.h + SPACING]

                if not ((r1[0] >= r2[2]) or (r1[2] <= r2[0]) or (r1[3] <= r2[1]) or (r1[1] >= r2[3])):
                    placing = True
                    break

        self.x, self.y, self.w, self.h = x, y, w, h
        self.center = (self.x + self.w // 2, self.y + self.h // 2)

        for i in range(self.w):
            for j in range(self.h):
                grid[self.y + j][self.x + i] = self.id


def path_getting(wave_grid, end):
    """ Function that returns path by analysing wave algorithm's grid """

    path = []
    current = end

    while wave_grid[current[0]][current[1]] != 0:
        neighbors = [
            (current[0] + 1, current[1]),
            (current[0] - 1, current[1]),
            (current[0], current[1] + 1),
            (current[0], current[1] - 1),
        ]
        for neighbor in neighbors:
            if (wave_grid[neighbor[0]][neighbor[1]] not in [-1, -2]) \
                    and (wave_grid[neighbor[0]][neighbor[1]] < wave_grid[current[0]][current[1]]):
                path.append(current)
                current = neighbor
    path.append(end)
    return path


def pathfinding(start, end):
    """ Realisation of wave pathfinding algorithm """

    start_id, end_id = grid[start[0]][start[1]], grid[end[0]][end[1]]
    wave_grid = [[-2 if (grid[y][x] >= 0 and grid[y][x] != start_id and grid[y][x] != end_id)
                  else -1 for x in range(SIZE[0] + 1)] for y in range(SIZE[1] + 1)]
    wave_grid[start[0]][start[1]] = -1
    wave_grid[end[0]][end[1]] = -1
    distance = 0
    wave_grid[start[0]][start[1]] = distance
    queue = [start]
    while queue:
        current = queue.pop(0)
        neighbors = [
            (current[0] + 1, current[1]),
            (current[0] - 1, current[1]),
            (current[0], current[1] + 1),
            (current[0], current[1] - 1),
        ]
        for neighbor in neighbors:
            if 0 <= neighbor[0] <= SIZE[0] and 0 <= neighbor[1] <= SIZE[1]:
                if wave_grid[neighbor[0]][neighbor[1]] == -1:
                    wave_grid[neighbor[0]][neighbor[1]] = distance + 1
                    queue.append(neighbor)
                    if neighbor == end:
                        return path_getting(wave_grid, end)
        distance += 1
    return None


def rooms_placing():
    """ Function that generates random amount of rooms on the map """

    for i in range(np.random.randint(ROOM_MIN_QUANTITY, ROOM_MAX_QUANTITY)):
        new_room = Room(i)
        rooms.append(new_room)


def graph_generator():
    """ Function that make unrefined graph of rooms' coordinates """

    x, y = [], []

    for room in rooms:
        x.append(room.center[0])
        y.append(room.center[1])

    graph = ig.Graph(30)
    graph.vs['x'] = x
    graph.vs['y'] = y

    return graph


def delone_triangulation(graph):
    """ Realisation of Delone's triangulation. Graph constructing """

    coords = graph.layout_auto().coords
    delaunay = Delaunay(coords)
    for tri in delaunay.simplices:
        graph.add_edges([(tri[0], tri[1]), (tri[1], tri[2]), (tri[0], tri[2])])
    graph.simplify()
    return graph


def minimal_spanning_tree_search(graph):
    """ Realisation of Prime's algorithm. Searching for Minimal Spanning Tree (MST) """

    graph.es["weight"] = [np.random.randint(1, 20) for _ in graph.es]
    graph = graph.spanning_tree(weights=graph.es["weight"], return_tree=True)
    graph.simplify()
    return graph


def random_edges_adder(full_graph, minimal_graph):
    """ Function that adding random edges to graph """

    graph = minimal_graph.copy()
    for edge in full_graph.es:
        if edge not in minimal_graph.es and np.random.randint(1, 1000) <= ADDITIONAL_CORRIDOR_PROBABILITY * 1000:
            graph.add_edge(edge.source, edge.target)
    graph.simplify()
    return graph


def path_drawer(graph):
    """ Function that processing pathfinding grid to normal grid """

    layout_obj = graph.layout()
    x, y = np.array(layout_obj.coords).T
    for i, edge in enumerate(graph.es):
        print(edge.source, edge.target)
        from_v = (x[edge.source], y[edge.source])
        to_v = (x[edge.target], y[edge.target])
        path = pathfinding(from_v, to_v)
        if path is not None:
            for cell in path:
                grid[cell[0]][cell[1]] = -2


def dungeon_generation():
    """ Function that runs all the dungeon generation"""

    rooms_placing()
    graph = graph_generator()
    triangulated_graph = delone_triangulation(graph)
    minimal_spanning_tree = minimal_spanning_tree_search(triangulated_graph)
    complete_graph = random_edges_adder(triangulated_graph, minimal_spanning_tree)
    path_drawer(complete_graph)
    print(complete_graph)
    return rooms
