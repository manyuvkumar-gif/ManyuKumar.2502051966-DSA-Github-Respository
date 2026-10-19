"""
Graph-Based Fraud Detection in Financial Transaction Networks
Simple college-level DSA project.

Concepts used:
- Directed graph represented by an adjacency list
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Directed cycle detection
- In-degree and out-degree calculation

This program uses the hypothetical transactions from the project report.
A detected pattern is only a reason for review; it does NOT prove fraud.
No external Python packages are required.
"""

from collections import deque


# Each transaction is: (transaction_id, sender, receiver, amount, time)
TRANSACTIONS = [
    ("T1", "A", "B", 900000, "09:00"),
    ("T2", "B", "C", 880000, "09:12"),
    ("T3", "C", "D", 870000, "09:25"),
    ("T4", "D", "B", 100000, "10:10"),
    ("T5", "A", "E", 25000, "10:20"),
    ("T6", "E", "F", 24000, "10:35"),
    ("T7", "F", "C", 20000, "10:50"),
    ("T8", "B", "E", 15000, "11:05"),
]


def build_graph(transactions):
    """Build a directed adjacency list and degree counts."""
    graph = {}
    in_degree = {}
    out_degree = {}
    accounts = set()

    for tx_id, sender, receiver, amount, time in transactions:
        accounts.add(sender)
        accounts.add(receiver)

    for account in accounts:
        graph[account] = []
        in_degree[account] = 0
        out_degree[account] = 0

    for tx_id, sender, receiver, amount, time in transactions:
        graph[sender].append(receiver)
        out_degree[sender] += 1
        in_degree[receiver] += 1

    # Keep the output order predictable.
    graph = dict(sorted(graph.items()))
    return graph, in_degree, out_degree


def bfs(graph, start):
    """Breadth-First Search: visit accounts level by level."""
    visited = set([start])
    queue = deque([start])
    order = []
    distance = {start: 0}

    while queue:
        current = queue.popleft()
        order.append(current)

        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                distance[neighbour] = distance[current] + 1
                queue.append(neighbour)

    return order, distance


def dfs(graph, start):
    """Depth-First Search using a stack."""
    visited = set()
    stack = [start]
    order = []

    while stack:
        current = stack.pop()
        if current in visited:
            continue

        visited.add(current)
        order.append(current)

        # Reverse so the first listed neighbour is explored first.
        for neighbour in reversed(graph[current]):
            if neighbour not in visited:
                stack.append(neighbour)

    return order


def find_directed_cycle(graph):
    """
    Find one directed cycle using DFS states:
    0 = not visited, 1 = currently exploring, 2 = finished.
    Returns a cycle list such as ['B', 'C', 'D', 'B'], or None.
    """
    state = {node: 0 for node in graph}
    parent = {}

    def visit(node):
        state[node] = 1

        for neighbour in graph[node]:
            if state[neighbour] == 0:
                parent[neighbour] = node
                found = visit(neighbour)
                if found:
                    return found
            elif state[neighbour] == 1:
                # We found a back edge. Reconstruct the cycle.
                path = [node]
                current = node
                while current != neighbour:
                    current = parent[current]
                    path.append(current)
                path.reverse()
                path.append(neighbour)
                return path

        state[node] = 2
        return None

    for node in graph:
        if state[node] == 0:
            found = visit(node)
            if found:
                return found

    return None


def show_transactions(transactions):
    print("\nTRANSACTION DATASET")
    print("-" * 66)
    print(f"{'ID':<5}{'From':<8}{'To':<8}{'Amount (INR)':>18}  {'Time':<8}")
    print("-" * 66)
    for tx_id, sender, receiver, amount, time in transactions:
        print(f"{tx_id:<5}{sender:<8}{receiver:<8}{amount:>18,}  {time:<8}")


def show_graph(graph):
    print("\nDIRECTED GRAPH (ADJACENCY LIST)")
    print("-" * 36)
    for account, neighbours in graph.items():
        print(f"{account}: {', '.join(neighbours) if neighbours else 'No outgoing transactions'}")


def main():
    graph, in_degree, out_degree = build_graph(TRANSACTIONS)

    print("=" * 58)
    print(" GRAPH-BASED FINANCIAL FRAUD DETECTION")
    print(" Simple DSA Lab Project")
    print("=" * 58)
    show_transactions(TRANSACTIONS)
    show_graph(graph)

    print("\n1. BREADTH-FIRST SEARCH (BFS)")
    start = input("Enter starting account for BFS (default A): ").strip().upper() or "A"
    if start not in graph:
        print("Account not found. Using A as the starting account.")
        start = "A"

    order, distance = bfs(graph, start)
    print("BFS visit order:", " -> ".join(order))
    print("Minimum number of transaction hops from", start + ":")
    for account in sorted(distance):
        print(f"  {start} to {account}: {distance[account]} hop(s)")

    print("\n2. DEPTH-FIRST SEARCH (DFS)")
    dfs_order = dfs(graph, start)
    print("DFS visit order:", " -> ".join(dfs_order))

    print("\n3. DIRECTED CYCLE DETECTION")
    cycle = find_directed_cycle(graph)
    if cycle:
        print("Cycle detected:", " -> ".join(cycle))
        print("Review note: a cycle is a pattern to inspect, not proof of fraud.")
    else:
        print("No directed cycle was found.")

    print("\n4. IN-DEGREE AND OUT-DEGREE")
    print("-" * 38)
    print(f"{'Account':<12}{'In-degree':>12}{'Out-degree':>14}")
    for account in sorted(graph):
        print(f"{account:<12}{in_degree[account]:>12}{out_degree[account]:>14}")

    print("\n5. SIMPLE REVIEW SUMMARY")
    print("-" * 38)
    print("Accounts with more than one incoming transaction:")
    found = False
    for account in sorted(graph):
        if in_degree[account] > 1:
            print(f"  {account} receives transactions from multiple accounts "
                  f"(in-degree = {in_degree[account]}).")
            found = True
    if not found:
        print("  None in this dataset.")

    print("\nTransaction chain example: A -> B -> C -> D")
    print("The graph also includes links through E and F.")
    print("\nIMPORTANT:")
    print("This is an educational demonstration using hypothetical data.")
    print("The program identifies graph patterns only. It cannot confirm fraud.")
    print("Real cases need transaction context and human investigation.")


if __name__ == "__main__":
    main()
