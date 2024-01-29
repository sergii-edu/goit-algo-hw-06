import networkx as nx
from tabulate import tabulate


distances = [
    ("Київ", "Братислава", {"weight": 1030}),
    ("Київ", "Будапешт", {"weight": 900}),
    ("Київ", "Бухарест", {"weight": 490}),
    ("Київ", "Кишинів", {"weight": 380}),
    ("Варшава", "Київ", {"weight": 690}),
    ("Варшава", "Вільнюс", {"weight": 400}),
    ("Варшава", "Братислава", {"weight": 520}),
    ("Варшава", "Прага", {"weight": 520}),
    ("Братислава", "Будапешт", {"weight": 200}),
    ("Братислава", "Прага", {"weight": 330}),
    ("Будапешт", "Бухарест", {"weight": 600}),
    ("Бухарест", "Кишинів", {"weight": 440}),
    ("Бухарест", "Софія", {"weight": 300}),
    ("Вільнюс", "Рига", {"weight": 260}),
    ("Рига", "Таллінн", {"weight": 280}),
]


def dijkstra(graph, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes)

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float("infinity"):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight["weight"]

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances


def create_graph():
    G = nx.Graph()
    G.add_edges_from(distances)
    return G


def main():
    G = create_graph()
    cities = list(G.nodes())
    table_rows = [dijkstra(G, city) for city in cities]

    for index, city in enumerate(cities):
        row = table_rows[index]
        table_rows[index] = [city] + [row[destination] for destination in cities]

    print(tabulate(table_rows, headers=cities, tablefmt="grid"))


if __name__ == "__main__":
    main()
