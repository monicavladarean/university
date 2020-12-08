from repo import Graph

class Ui():
    def __init__(self,file_name):
        self.graph=Graph(file_name)

    def menu(self):
        print("1. Get the number of vertices")
        print("2. Parse the entire graph")
        print("3. Parse the inbound edges of a vertex")
        print("4. Parse the outbound edges of a vertex")
        print("5. Print an edge's cost")
        print("6. Set an edge's cost")
        print("7. Check if vertex exists")
        print("8. Check if edge exists")
        print("9. Add an edge")
        print("10. Remove an edge")
        print("11. Add a vertex")
        print("12. Remove a vertex")
        print("13. Print the indegree of a vertex")
        print("14. Print the outdegree of a vertex")
        print("15. Print the graph")
        print("0. Exit")

    def show(self):
        ok=1
        while ok==1:
            self.menu()
            command=int(input("What to do?"))

            if command==0:
                ok=0

            elif command == 1:
                print(self.graph.get_number())

            elif command == 2:
                print(self.graph.parse())

            elif command == 3:
                x = int(input("Vertex: "))
                if self.graph.parse_in(x)==False:
                    print("Unexisting vertex")
                else:
                    print(self.graph.parse_in(x))

            elif command == 4:
                x = int(input("Vertex: "))
                if self.graph.parse_out(x) == False:
                    print("Unexisting vertex")
                else:
                    print(self.graph.parse_out(x))

            elif command == 5:
                x = int(input("Starting vertex: "))
                y = int(input("Ending vertex: "))
                if self.graph.get_cost(x,y)==False:
                    print("No edge here")
                else:
                    print(self.graph.get_cost(x,y))

            elif command == 6:
                x = int(input("Starting vertex: "))
                y = int(input("Ending vertex: "))
                c=int(input("New cost: "))
                if self.graph.set_cost(x, y,c) == False:
                    print("No edge here")
                else:
                    print("Done")

            elif command == 7:
                x=int(input("Vertex: "))
                if self.graph.exist_vertex(x)==True:
                    print("Yes")
                else:
                    print("No")

            elif command == 8:
                x = int(input("Starting vertex: "))
                y = int(input("Ending vertex: "))
                if self.graph.exist_edge(x,y)==True:
                    print("Yes")
                else:
                    print("No")

            elif command == 9:
                x = int(input("Starting vertex: "))
                y = int(input("Ending vertex: "))
                c = int(input("Cost: "))
                if self.graph.add_edge(x,y,c)==False:
                    print("Imposible")
                else:
                    print("Done")

            elif command == 10:
                x = int(input("Starting vertex: "))
                y = int(input("Ending vertex: "))
                if self.graph.remove_edge(x,y)==False:
                    print("Invalid edge")
                else:
                    print("Done")

            elif command == 11:
                x = int(input("Vertex: "))
                if self.graph.add_vertex(x)==False:
                    print("Vertex exists")
                else:
                    print("Done")

            elif command == 12:
                x = int(input("Vertex: "))
                if self.graph.remove_vertex(x)==False:
                    print("Can't make the remove")
                else:
                    print("Done")

            elif command == 13:
                x = int(input("Vertex: "))
                if self.graph.exist_vertex(x) == False:
                    print("Vertex doesn't exist")
                else:
                    print(self.graph.indegree(x))

            elif command == 14:
                x = int(input("Vertex: "))
                if self.graph.exist_vertex(x)==False:
                    print("Vertex doesn't exist")
                else:
                    print(self.graph.outdegree(x))

            elif command == 15:
                self.graph.print()

            else:
                print("Invalid command!")
