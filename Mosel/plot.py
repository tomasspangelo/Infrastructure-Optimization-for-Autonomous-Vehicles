import networkx as nx
import sys
import matplotlib.pyplot as plt
plotfile = "out.txt"
if len(sys.argv)==2:
    plotfile = sys.argv[1]
control_center = 0
core_nodes = []
core_edges = []
sub_edges = []
bandwith = []
objval = 0
corecost = 0
subcost = 0
stop_word = ['Control center:\n','Cities in the core net:\n', 'Arcs in the corenet\n', 'Arcs in the subnet\n', 'Bandwith in the subnet\n', 'Objective function value\n','Core net cost\n',"Sub net cost\n"]
state = ""

with open(plotfile,'r') as f:
    line = f.readline()

    while line:
        line = str(line)
        if line in stop_word:
            state = line
            line = f.readline()
            continue
        if state == stop_word[0]:
            control_center = int(line)
        if state == stop_word[1]:
            core_nodes.append(int(line))
        if state == stop_word[2]:
            edge = line.split(",")
            core_edges.append((int(edge[0]),int(edge[1])))
        if state == stop_word[3]:
            edge = line.split(",")
            sub_edges.append((int(edge[0]),int(edge[1])))
        if state == stop_word[4]:
            bandwith.append(float(line))
        if state == stop_word[5]:
            objval=float(line)
        if state == stop_word[6]:
            corecost = float(line)
        if state == stop_word[7]:
            subcost = float(line)

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
plt.figure(figsize=(10,5))
ax = plt.gca()
ax.set_title(f'Total cost: {objval}, Core-net cost: {corecost},Sub-net cost: {subcost}')
AllCities = ['Boden','Borås','Eskilstuna','Falun','Gävle','Göteborg','Halmstad','Haparanda','Helsingborg',\
'Hudiksvall','Jönköping','Kalmar','Karlskrona','Karlstad','Kiruna','Kristianstad','Lidköping',\
'Linköping','Luleå','Malmö','Motala','Norrköping','Nyköping','Sandviken','Skellefteå',\
'Skövde','Stockholm','Sundsvall','Trelleborg','Uddevalla',\
'Umeå','Uppsala','Varberg','Vetlanda','Vänersborg',\
'Västervik','Västerås','Växjö','Örebro','Örnsköldsvik',\
'Östersund',]

labels = {i+1:AllCities[i] for i in range(len(AllCities))}
pos = nx.drawing.kamada_kawai_layout(G)
nx.draw_networkx(G,pos=pos,node_color=color_map,with_labels=True,ax=ax,labels=labels)
n = nx.draw_networkx_edge_labels(G,pos,edge_labels=e_l,font_color='gray',ax=ax)

plt.show()