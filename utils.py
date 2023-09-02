from graph import Graph


def dfs(v: int, order: list[int], used: list[bool], graph: Graph):
    used[v] = True

    for node in range(graph.count_v()):
        if not used[node] and graph[v][node] > 0:
            dfs(v=node, order=order, used=used, graph=graph)

    order.append(v)


def dfs_t(v: int, component: list[int], used: list[bool], graph_t: Graph):
    used[v] = True
    component.append(v)

    for node in range(graph_t.count_v()):
        if not used[node] and graph_t[v][node] > 0:
            dfs_t(v=node, component=component, used=used, graph_t=graph_t)
