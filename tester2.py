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

print(m.exists_path_with_extra_food(A, E, 2, 0))
print(m.exists_path_with_extra_food(A, E, 2, 1))
print(m.exists_path_with_extra_food(A, E, 1, 6))