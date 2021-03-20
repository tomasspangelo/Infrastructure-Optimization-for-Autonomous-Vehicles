import networkx as nx
import matplotlib.pyplot as plt


control_center = 0
core_nodes = []
core_edges = []
sub_edges = []
bandwith = []
stop_word = ['Control center:\n','Cities in the core net:\n', 'Arcs in the corenet\n', 'Arcs in the subnet\n', 'Bandwith in the subnet\n']
state = ""
with open('out.txt','r') as f:
    line = f.readline()

    while line:
        line = str(line)
        if line in stop_word:
            state = line
            line = f.readline()
            continue
        if state == stop_word[0]:
            control_center = eval(line)
        if state == stop_word[1]:
            core_nodes.append(eval(line))
        if state == stop_word[2]:
            core_edges.append(eval(line))
        if state == stop_word[3]:
            sub_edges.append(eval(line))
        if state == stop_word[4]:
            bandwith.append(eval(line))
        line = f.readline()


G = nx.Graph()
for node in range(1,41+1):
    G.add_node(node)
for edge in core_edges:
    G.add_edge(edge[0],edge[1])
for edge in sub_edges:
    G.add_edge(edge[0],edge[1])

color_map = []
for node in G:
    if node ==control_center:
        color_map.append('green')
    elif node in core_nodes: 
        color_map.append('yellow')   
    else:
        color_map.append("lightblue")
e_l = {edge:bandwith[i] for i,edge in enumerate(sub_edges)}
pos = nx.drawing.kamada_kawai_layout(G)  
nx.draw_networkx(G,pos=pos,node_color=color_map,with_labels=True)
n = nx.draw_networkx_edge_labels(G,pos,edge_labels=e_l,font_color='gray')
plt.show()