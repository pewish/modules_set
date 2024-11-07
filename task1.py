import networkx as nx
import matplotlib.pyplot as plt

models = {
    'Модель 1': ['IN4_1', 'IN2_2 OUT3_4', 'IN4_3 OUT2_2', 'IN1_4 OUT1_2', 'IN1_2 OUT3_3'],
    'Модель 2': ['IN4_4', 'IN1_4 OUT3_1', 'IN2_1 OUT4_4', 'IN1_1 OUT1_1', 'IN3_3'],
    'Модель 3': ['IN2_3', 'IN4_3 OUT1_2', 'IN1_2 OUT4_3', 'IN4_1 OUT3_1', 'IN1_3 OUT2_1'],
    'Модель 4': ['IN4_1', 'IN4_1 OUT1_1', 'IN5_5 OUT2_3', 'IN2_2 OUT1_4', 'IN3_4'],
    'Модель 5': ['IN5_2', 'IN5_1 OUT1_1', 'IN3_2 OUT2_4', 'IN3_1 OUT3_1', 'IN4_5 OUT1_2']
}

connections = {
    'OUT3_4': 'IN4_1',
    'OUT4_4': 'IN4_3',
    'OUT3_3': 'IN3_1',
    'OUT4_1': 'IN2_4',
    'OUT2_3': 'IN5_4',
    'OUT4_3': 'IN5_2',
    'OUT4_4': 'IN5_4',
    'OUT1_1': 'IN4_3'
}

G = nx.DiGraph()

for model in models.keys():
    G.add_node(model)

for model, params in models.items():
    for param in params:
        if 'OUT' in param:
            out_param = param.split(' ')[1]
            if out_param in connections:
                in_param = connections[out_param]
                for other_model, other_params in models.items():
                    if model != other_model and any(in_param in p for p in other_params):
                        G.add_edge(model, other_model, label=out_param + ' -> ' + in_param)

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold", arrows=True)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color='red')
plt.title("Граф взаимосвязи моделей")
plt.show()
