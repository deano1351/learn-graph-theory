from graphs.reference_implementation import DirectedGraph, UndirectedGraph
from algorithms.search.reference_implementation import breadth_first_search_by_criteria


def criterion(node):
    return node.upper() == 'E'

def test_no_path_directed():
    '''
    Test BFS on a simple directed graph that contains a no cycles, and no path to the goal.
    '''
    g = DirectedGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('b', 'd')
    g.add_edge('e', 'f')

    assert breadth_first_search_by_criteria(g, 'a', criterion) is None


def test_no_path_directed_cycles():
    '''
    Test BFS on a simple directed graph that contains cycles, but no path to the goal.
    '''
    g = DirectedGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('c', 'a')
    g.add_edge('b', 'd')
    g.add_edge('e', 'f')

    assert breadth_first_search_by_criteria(g, 'a', criterion) is None


def test_single_path_directed():
    g = DirectedGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('b', 'd')
    g.add_edge('d', 'e')
    g.add_edge('e', 'f')

    assert breadth_first_search_by_criteria(g, 'a', criterion) == ['a', 'b', 'd', 'e']


def test_multiple_paths_directed():
    g = DirectedGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('b', 'e')
    g.add_edge('b', 'd')
    g.add_edge('d', 'e')
    g.add_edge('e', 'f')

    assert breadth_first_search_by_criteria(g, 'a', criterion) == ['a', 'b', 'e']


def test_single_path_with_cycles_directed():
    g = DirectedGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('c', 'h')
    g.add_edge('h', 'i')
    g.add_edge('i', 'j')
    g.add_edge('j', 'e')
    g.add_edge('b', 'd')
    g.add_edge('d', 'k')
    g.add_edge('k', 'f')
    g.add_edge('f', 'b')

    assert breadth_first_search_by_criteria(g, 'a', criterion) == ['a', 'b', 'c', 'h', 'i', 'j', 'e']


def test_no_path_undirected():
    '''
    Test BFS on a simple undirected graph that contains a no cycles, and no path to the goal.
    '''
    g = UndirectedGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('b', 'd')
    g.add_edge('e', 'f')

    assert breadth_first_search_by_criteria(g, 'a', criterion) is None


def test_no_path_undirected_cycles():
    '''
    Test BFS on a simple undirected graph that contains cycles, but no path to the goal.
    '''
    g = UndirectedGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('c', 'a')
    g.add_edge('b', 'd')
    g.add_edge('e', 'f')

    assert breadth_first_search_by_criteria(g, 'a', criterion) is None


def test_single_path_undirected():
    g = UndirectedGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('b', 'd')
    g.add_edge('d', 'e')
    g.add_edge('e', 'f')

    assert breadth_first_search_by_criteria(g, 'a', criterion) == ['a', 'b', 'd', 'e']


def test_multiple_paths_undirected():
    g = UndirectedGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('b', 'e')
    g.add_edge('b', 'd')
    g.add_edge('d', 'e')
    g.add_edge('e', 'f')

    assert breadth_first_search_by_criteria(g, 'a', criterion) == ['a', 'b', 'e']


def test_single_path_with_cycles_undirected():
    g = UndirectedGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('c', 'h')
    g.add_edge('h', 'i')
    g.add_edge('i', 'j')
    g.add_edge('j', 'e')
    g.add_edge('b', 'd')
    g.add_edge('d', 'k')
    g.add_edge('k', 'f')
    g.add_edge('f', 'b')

    assert breadth_first_search_by_criteria(g, 'a', criterion) == ['a', 'b', 'c', 'h', 'i', 'j', 'e']

def test_graph_with_tie():
    g = UndirectedGraph()
    g.add_edge('a', 'b')
    g.add_edge('b', 'c')
    g.add_edge('b', 'd')
    g.add_edge('c', 'e')
    g.add_edge('d', 'e')
    found = breadth_first_search_by_criteria(g, 'a', criterion)
    assert found == ['a', 'b', 'c', 'e'] or found == ['a', 'b', 'd', 'e']


def test_ignores_weight():
        g = UndirectedGraph()
        g.add_edge('a', 'b', 1)
        g.add_edge('a', 'd', 20)
        g.add_edge('b', 'c', 1)
        g.add_edge('c', 'e', 1)
        g.add_edge('d', 'e', 20)
        found = breadth_first_search_by_criteria(g, 'a', criterion)
        assert found == ['a', 'd', 'e']
