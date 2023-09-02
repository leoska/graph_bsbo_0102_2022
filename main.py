# Variant 17
from graph import Graph
from utils import dfs, dfs_t

COUNT_VERTEXES = 8
OUTPUT_CHAR = ["A", "B", "C", "D", "E", "F", "G", "H"]


def _init_graph(graph: Graph):
    for i in range(COUNT_VERTEXES):
        graph.add_v(name=OUTPUT_CHAR[i], mark=i)

    # A: 0, B: 1, C: 2, D: 3, E: 4, F: 5, G: 6, H: 7
    graph.add_e(v=0, w=1)  # A -> B
    graph.add_e(v=1, w=2)  # B -> C
    graph.add_e(v=2, w=3)  # C -> D
    graph.add_e(v=3, w=2)  # D -> C
    graph.add_e(v=1, w=4)  # B -> E
    graph.add_e(v=4, w=0)  # E -> A
    graph.add_e(v=1, w=5)  # B -> F
    graph.add_e(v=4, w=5)  # E -> F
    graph.add_e(v=5, w=6)  # F -> G
    graph.add_e(v=6, w=5)  # G -> F
    graph.add_e(v=2, w=6)  # C -> G
    graph.add_e(v=3, w=7)  # D -> H
    graph.add_e(v=7, w=3)  # H -> D
    graph.add_e(v=7, w=6)  # H -> G


if __name__ == '__main__':
    graph = Graph()

    _init_graph(graph)

    order: list[int] = []
    used: list[bool] = [False] * graph.count_v()
    component = []

    for i in range(graph.count_v()):
        if not used[i]:
            dfs(v=i, order=order, used=used, graph=graph)

    graph_trans = Graph.get_transpose_graph(graph=graph)
    used: list[bool] = [False] * graph.count_v()

    for i in range(graph.count_v()):
        v = order[graph.count_v() - i - 1]

        if not used[v]:
            dfs_t(v=v, component=component, used=used, graph_t=graph_trans)

            print("".join([OUTPUT_CHAR[index] + " " for index in component]))

            component.clear()
