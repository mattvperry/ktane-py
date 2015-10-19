from ktane import Module
from itertools import chain
from .maze_data import mazes

class Mazes(Module):

    def run(self):
        maze = Maze(mazes[0])
        print(maze)
        path = self.find_shortest_path(maze.as_graph(), (0, 0), (5, 5))
        print(path)
        print(maze.as_string_with_path(path))
        input()

    def find_shortest_path(self, graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not start in graph:
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                new_path = self.find_shortest_path(graph, node, end, path)
                if new_path: 
                    if not shortest or len(new_path) < len(shortest):
                        shortest = new_path
        return shortest

class Maze(object):

    def __init__(self, matrix_ascii):
        self.matrix = matrix_ascii.strip().splitlines()

    def as_string_with_path(self, path):
        new_maze = Maze('\n'.join([''.join(x) for x in self.matrix]))
        new_maze.__set_cell(tuple(i * 2 for i in path[0]), 's')
        new_maze.__set_cell(tuple(i * 2 for i in path[-1]), 'e')
        for point in path[1:-1]:
            new_maze.__set_cell(tuple(i * 2 for i in point), '#')
        return new_maze.__str__()

    def as_graph(self):
        graph = {}
        for x in range(6):
            for y in range(6):
                point = (x, y)
                graph[point] = [x for x in self.__neighbors(point) 
                                if self.valid_move(point, x)]
        return graph

    def valid_move(self, from_point, to_point):
        wall_x = (to_point[0] - from_point[0]) + 2 * from_point[0]
        wall_y = (to_point[1] - from_point[1]) + 2 * from_point[1]
        wall_point = (wall_x, wall_y)
        return self.__point_in_bounds(wall_point) and not self.__is_wall(self.__get_cell(wall_point))

    def __point_in_bounds(self, point):
        return point[0] in range(len(self.matrix[0])) and point[1] in range(len(self.matrix))
    
    def __get_cell(self, point):
        return self.matrix[point[1]][point[0]]

    def __set_cell(self, point, value):
        chars = list(self.matrix[point[1]])
        chars[point[0]] = value
        self.matrix[point[1]] = ''.join(chars)

    def __neighbors(self, point):
        return [
            (point[0] + 1, point[1]),
            (point[0] - 1, point[1]),
            (point[0], point[1] + 1),
            (point[0], point[1] - 1)
        ]

    def __is_wall(self, char):
        return not char in 'se#O. '

    def __str__(self):
        maze_box_chars = [self.__convert_to_box(x) for x in self.__maze_chars(self.matrix)]
        return '\n'.join([''.join(x) for x in maze_box_chars])

    # ---
    # Logic for unicode box drawing
    # ---

    char_map = {
        '.': u'\u00B7',
        '-': u'\u2550',
        '|': u'\u2551',
        '+': u'\u256C',
        '/': u'\u2554',
        'L': u'\u255A',
        'J': u'\u255D',
        'E': u'\u2560',
        '3': u'\u2563',
        'T': u'\u2566',
        'F': u'\u2569',
        '#': u'\u2588',
        '\\': u'\u2557',
        ' ': ' ',
        'O': 'O',
        's': 'S',
        'e': 'E',
    }

    def __maze_chars(self, maze):
        maze_string = [self.__border_chars('/', '\\', 'T', maze[0])]
        maze_string += [self.__row_chars(r) for r in maze]
        maze_string += [self.__border_chars('L', 'J', 'F', maze[-1])]
        return maze_string

    def __border_chars(self, begin, end, connect, row):
        border = [begin]
        border += chain.from_iterable([('-', connect if x == '|' else '-') for x in row])
        border += ['-', end]
        return border

    def __row_chars(self, row):
        row_chars = ['E', '-'] if self.__is_wall(row[0]) else ['|', ' ']
        row_chars.append(row[0])
        char = lambda r, i: '-' if self.__is_wall(r[i]) and self.__is_wall(r[i + 1]) else ' '
        row_chars += chain.from_iterable([(char(row, i), x) for i, x in enumerate(row[1::])])
        row_chars += ['-', '3'] if self.__is_wall(row[-1]) else [' ', '|']
        return row_chars

    def __convert_to_box(self, chars):
        return [self.char_map[x] for x in chars]