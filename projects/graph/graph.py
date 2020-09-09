# from graph import Graph
# gr = Graph()
# gr.add_vertex(1)
# gr.add_vertex(2)
# gr.add_vertex(3)
# gr.add_vertex(4)
# gr.add_vertex(5)
# gr.add_vertex(6)
# gr.add_vertex(7)
# gr.add_edge(5, 3)
# gr.add_edge(6, 3)
# gr.add_edge(7, 1)
# gr.add_edge(4, 7)
# gr.add_edge(1, 2)
# gr.add_edge(7, 6)
# gr.add_edge(2, 4)
# gr.add_edge(3, 5)
# gr.add_edge(2, 3)
# gr.add_edge(4, 6)

"""
Simple graph implementation
"""
from pkg_resources import DEVELOP_DIST
from util import Stack, Queue  # These may come in handy
import sys, io

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}


    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v2 not in self.vertices:
            raise Exception(f'verticy "{v2}" not present in graph')
        else:
            self.vertices[v1].add(v2)


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = []
        stack = [starting_vertex]
        while stack:
            curr = stack.pop()
            visited.append(curr)
            nxt = [i for i in self.vertices[curr] if i not in visited and i not in stack]
            stack.extend(nxt)
            # breakpoint(dri)

        for i in visited:
            print(i)


    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited == None:
            print(starting_vertex)
            visited = [starting_vertex]
        new_nodes = [i for i in self.vertices[starting_vertex] if i not in visited]
        for i in new_nodes:
            if i not in visited:
                print(i)
                visited.append(i)
                self.dft_recursive(i, visited)


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = []
        path = [starting_vertex]
        while path:
            curr = path.pop(0)
            nxt = [i for i in self.vertices[curr] if i not in visited]
            visited.append(curr)
            path.extend(nxt)
        for i in visited:
            print(i)


    def bfs(self, sv, dv):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = [False] * (len(self.vertices) + 1)
        paths = [[sv]]
        visited[sv] = True
        while paths:
            curr = paths.pop(0)
            visited[curr[-1]] = True
            if dv in self.vertices[curr[-1]]:
                curr.append(dv)
                return curr
            nvs = [j for j in list(self.vertices[curr[-1]]) if j not in visited]
            for k in nvs:
                nxt = curr.copy()
                nxt.append(k)
                paths.append(nxt)
        return False

    def dfs(self, sv, dv):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = [False] * (len(self.vertices) + 1)
        paths = [[sv]]
        visited[sv] = True
        while paths:
            curr = paths.pop()
            visited[curr[-1]] = True
            if dv in self.vertices[curr[-1]]:
                curr.append(dv)
                return curr
            nvs = [j for j in list(self.vertices[curr[-1]]) if j not in visited]
            for k in nvs:
                nxt = curr.copy()
                nxt.append(k)
                paths.append(nxt)
        return False

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
            """
            Return a list containing a path from
            starting_vertex to destination_vertex in
            depth-first order.
            This should be done using recursion.
            """
            # if our visited set does not exist, create it
            if visited is None:
                visited = set()
            # if our path does not exist, create it
            if path is None:
                path = []
            # mark our starting vertex as visited
            visited.add(starting_vertex)
            # add our starting vertex to our path
            path = path + [starting_vertex]
            # if the starting vertex is our destination vertex, return its path
            if starting_vertex == destination_vertex:
                return path
            # for each neighbor of our starting vertex,
            for neighbor in self.get_neighbors(starting_vertex):
                # if the neighbor hasn't been visited
                if neighbor not in visited:
                    # create a new path and recursively call dfs_recursive on it
                    new_path = self.dfs_recursive(
                        neighbor, destination_vertex, visited, path)
                    # if the new path exists, return it
                    if new_path:
                        return new_path
            # we did not find the destination vertex
            return None

    # def dfs_recursive(self, sv, dv, visited = None, path = None):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.

    #     This should be done using recursion.
    #     """
    #     # first settings for init
    #     if visited == None:
    #         visited = [False] * (len(self.vertices) + 1)
    #     if path == None:
    #         path = []

    #     path.append(sv)

    #     visited[sv] = True

    #     if dv in self.vertices[sv]:
    #         return path.append(dv)

    #     for i in self.vertices[sv]:
    #         if not visited[i]:
    #             breakpoint()
    #             out = self.dfs_recursive(i, dv, visited, path)
    #             if out is not None:
    #                 return out
    #     return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
