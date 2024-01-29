import matplotlib.pyplot as plt
import networkx as nx

european_countries = {
    "Україна": ["Польща", "Словаччина", "Угорщина", "Румунія", "Молдова"],
    "Польща": ["Україна", "Литва", "Словаччина"],
    "Словаччина": ["Польща", "Україна", "Угорщина", "Чехія"],
    "Угорщина": ["Словаччина", "Україна", "Румунія"],
    "Румунія": ["Угорщина", "Україна", "Молдова", "Болгарія"],
    "Молдова": ["Румунія", "Україна"],
    "Болгарія": ["Румунія"],
    "Литва": ["Латвія", "Польща"],
    "Латвія": ["Естонія", "Литва"],
    "Естонія": ["Латвія"],
    "Чехія": ["Польща", "Словаччина"],
}


def create_graph():
    G = nx.Graph(european_countries)

    return G


def main():
    G = create_graph()
    plt.figure(figsize=(12, 10))
    nx.draw(
        G,
        with_labels=True,
        node_color="lightgreen",
        node_size=500,
        font_size=10,
        font_weight="bold",
        edge_color="lightgray",
    )
    plt.title("Граф суміжності кордонів східноєвропейських країн")
    plt.show()


if __name__ == "__main__":
    main()
