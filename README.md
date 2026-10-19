# Graph-Based Financial Fraud Detection — DSA Project

## About
This is a simple, beginner-friendly Python command-line implementation based on the hypothetical six-account network in the reference report.

It demonstrates:
- Directed graph and adjacency list
- BFS (Breadth-First Search)
- DFS (Depth-First Search)
- Directed cycle detection
- In-degree and out-degree
- A small review summary

It uses only Python's standard library; no installation of extra packages is needed.

## Requirements
- Python 3.8 or newer (Python 3 should work)
- Any text editor or IDE, such as IDLE, VS Code, PyCharm, or the terminal

## How to run

1. Save `graph_fraud_detection.py` to a folder.
2. Open Terminal / Command Prompt in that folder.
3. Run:

   ```bash
   python graph_fraud_detection.py
   ```

   On some Macs/Linux systems, use:

   ```bash
   python3 graph_fraud_detection.py
   ```

4. When asked for a starting account, enter `A` or another account from `A` to `F`. Press Enter to use `A`.

## Sample data
The program uses these directed transactions from the hypothetical example in the report:

- A → B: ₹900,000 at 09:00
- B → C: ₹880,000 at 09:12
- C → D: ₹870,000 at 09:25
- D → B: ₹100,000 at 10:10
- A → E: ₹25,000 at 10:20
- E → F: ₹24,000 at 10:35
- F → C: ₹20,000 at 10:50
- B → E: ₹15,000 at 11:05

## DSA concepts to explain in a viva
- **Vertex:** an account in the network.
- **Directed edge:** a transfer from a sender to a receiver.
- **Adjacency list:** stores each account's outgoing neighbours.
- **BFS:** explores reachable accounts level by level and calculates the minimum number of edges (hops) in an unweighted graph.
- **DFS:** explores a path deeply before backtracking.
- **Cycle detection:** checks whether directed edges form a closed loop. This sample contains B → C → D → B.
- **In-degree:** number of incoming edges.
- **Out-degree:** number of outgoing edges.

## Complexity
Let V be the number of accounts (vertices) and E the number of transactions (edges).
- Building the graph: O(V + E)
- BFS: O(V + E)
- DFS: O(V + E)
- Directed cycle detection: O(V + E)
- Degree calculation while building the graph: O(V + E) overall

## Important limitation
This is a small academic demonstration, not a real banking or production fraud detector. A graph pattern is not proof of fraud. Real investigations need timestamps, transaction purpose, customer context, data-quality checks, and human review.
