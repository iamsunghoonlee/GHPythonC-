"""This is a simple component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

import Rhino.Geometry as rg
import clr
clr.AddReference("Microsoft.Office.Interop.Excel")
import Microsoft.Office.Interop.Excel as excel
import math

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

#Excel
ex = excel.ApplicationClass()

#Open Workbook
workbook = ex.Workbooks.Open(filePath)

#Read Workbook
ws = workbook.Worksheets[1]

program = []
area = []
quantity = []
abbrev = []
graph = []

for i in range(ws.UsedRange.Rows.Count):
    if i == 0:
        continue
    
    c1 = ws.Range("A{}".format(i + 1)).Value2
    c3 = ws.Range("C{}".format(i + 1)).Value2
    c4 = ws.Range("D{}".format(i + 1)).Value2
    c2 = ws.Range("B{}".format(i + 1)).Value2
    c5 = ws.Range("E{}".format(i + 1)).Value2
    
    program.append(c1)
    area.append(c3)
    quantity.append(c4)
    abbrev.append(c2)
    graph.append(c5)

workbook.Close(False)
ex.Quit()

print(graph[0].split(",")[0])

#Making Graph Structure
g = Graph()

for i in range(len(program)):
    g.add_vertex(program[i])
    items = graph[i].split(",")
    for j in range(len(items)):
        g.add_edge(program[i], items[j])

print(g)

for v in g:
    for w in v.get_connections():
        vid = v.get_id()
        wid = w.get_id()
        print('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

for v in g:
    print('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))