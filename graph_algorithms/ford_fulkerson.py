# Algorytm Forda-Fulkersona jest algorytmem stosowanym do znajdowania maksymalnego przepływu w sieci przepływowej.
# Sieć przepływowa to skierowany graf, gdzie każda krawędź ma określoną pojemność przepływu i
# gdzie wyróżniamy dwa specjalne wierzchołki: źródło i ujście.

# Pomysł stojący za algorytmem Forda-Fulkersona polega na ciągłym wyszukiwaniu ścieżek od źródła do ujścia
# (tzw. ścieżek powiększających), przez które można przepuścić więcej przepływu,
# i na zwiększaniu całkowitego przepływu aż do momentu, gdy nie można znaleźć takiej ścieżki.

# W algorytmie Forda-Fulkersona kluczową koncepcją jest pojęcie przepływu rezydualnego.
# Przepływ rezydualny to ilość dodatkowego przepływu, który można przesłać wzdłuż danej krawędzi,
# uwzględniając już istniejący przepływ. Algorytm korzysta z tzw. sieci rezydualnej,
# która reprezentuje przepływy rezydualne dla każdej krawędzi.

# Algorytm zakończy się, gdy nie można znaleźć żadnej ścieżki powiększającej w sieci rezydualnej.
# W tym momencie obecny przepływ jest maksymalnym przepływem.
#
# Ważne jest, aby zauważyć, że algorytm Forda-Fulkersona wymaga, aby wszystkie pojemności były liczbami całkowitymi.
# Jeśli pojemności są liczbami rzeczywistymi, algorytm może nie zakończyć się. Dla pojemności będących liczbami
# całkowitymi, algorytm zakończy się po skończonej liczbie kroków, ponieważ każdy
# przepływ powiększający musi zawierać krawędź o pojemności co najmniej 1, a zatem każde
# powiększenie przepływu musi zwiększać całkowity przepływ o co najmniej 1.


def dfs(graph, s, t, parent):
    # Utworzenie tablicy visited o długości równej ilości wierzchołków w grafie
    # i ustawienie wszystkich wartości na False
    visited = [False] * len(graph)

    # Stworzenie stosu i dodanie źródła do stosu
    stack = [s]

    # Oznaczenie źródła jako odwiedzonego
    visited[s] = True

    # Dopóki stos nie jest pusty, wykonuj
    while stack:

        # Pobierz ostatni dodany wierzchołek
        u = stack.pop()

        # Dla każdego sąsiada wierzchołka, sprawdź czy jest nieodwiedzony i czy można z niego przeprowadzić przepływ
        for ind, val in enumerate(graph[u]):
            if not visited[ind] and val > 0:

                # Dodaj wierzchołek do stosu i oznacz jako odwiedzony
                stack.append(ind)
                visited[ind] = True
                parent[ind] = u

                # Jeżeli dojedziemy do ujścia, zakończ algorytm
                if ind == t:
                    print(visited)
                    return True

    # Jeżeli nie możemy dojść do ujścia zwróć False
    return False


def ford_fulkerson(graph, source, sink):
    # Utworzenie listy przechowującej informację o rodzicu każdego wierzchołka
    parent = [-1] * (len(graph))

    # Ustalenie początkowego przepływu na 0
    max_flow = 0

    # Dopóki istnieje ścieżka od źródła do ujścia, wykonuj
    while dfs(graph, source, sink, parent):

        # Ustal przepływ na ścieżce jako nieskończoność na początku
        path_flow = float("Inf")

        # Przejdź od ujścia do źródła i sprawdź jaki jest maksymalny przepływ na ścieżce
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        # Dodaj maksymalny przepływ na ścieżce do całkowitego przepływu
        max_flow += path_flow

        # Aktualizuj pojemności na krawędziach i krawędziach wstecznych wzdłuż ścieżki
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    # Zwróć maksymalny przepływ
    return max_flow


G1 = [[0, 10, 0, 0, 0, 10],
      [0, 0, 4, 0, 8, 2],
      [0, 0, 0, 10, 0, 0],
      [0, 0, 0, 0, 0, 0],
      [0, 0, 6, 10, 0, 0],
      [0, 0, 0, 0, 9, 0]]

G2 = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

G3 = [[0, 16, 13, 0, 0, 0],
      [0, 0, 10, 12, 0, 0],
      [0, 4, 0, 0, 14, 0],
      [0, 0, 9, 0, 0, 20],
      [0, 0, 0, 7, 0, 4],
      [0, 0, 0, 0, 0, 0]]

par = [None] * len(G3)
print(dfs(G3, 0, 5, par))
print(par)
