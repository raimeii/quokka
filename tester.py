from vertex import Vertex
from graph import QuokkaMaze


A = Vertex(False)
B = Vertex(False)
C = Vertex(True)
D = Vertex(False)
E = Vertex(True)

m = QuokkaMaze()

m.add_vertex(A)
m.add_vertex(B)
m.add_vertex(C)
m.add_vertex(D)
m.add_vertex(E)

m.fix_edge(A, B)
m.fix_edge(B, C)
m.fix_edge(C, D)
m.fix_edge(D, E)

print(m.find_path(A, E, 2))
print(m.find_path(A, E, 1))
print(m.find_path(A, C, 4))