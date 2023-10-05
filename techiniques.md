### 1. **Brute Force**
- **When to use**: When you can't think of any other solution, or to set a baseline solution.
- **Technique**: Solve the problem without considering time or space complexity. Iterate over all possibilities.

### 2. **Divide and Conquer**
- **When to use**: When a problem can be broken down into smaller instances of the same problem.
- **Technique**: Break the problem into smaller sub-problems, solve each sub-problem, and combine results.

### 3. **Dynamic Programming**
- **When to use**: When the problem has overlapping subproblems and optimal substructure.
- **Technique**: Store results of subproblems to avoid redundant computations. Use either bottom-up (tabulation) or top-down (memoization) approach.

### 4. **Recursion**
- **When to use**: When a problem can be divided into smaller sub-problems, often used in conjunction with divide and conquer.
- **Technique**: Break down the problem into base and recursive cases.

### 5. **Greedy Algorithm**
- **When to use**: When local optimization can lead to a global optimum.
- **Technique**: At each step, pick the best option available.

### 6. **Two Pointer Technique**
- **When to use**: When you need to search pairs in a sorted array or list.
- **Technique**: Use two pointers, which move towards each other or in the same direction, based on some condition.

### 7. **Backtracking**
- **When to use**: For problems related to finding all solutions (e.g., combinations, permutations).
- **Technique**: Build solutions incrementally and abandon a solution path (backtrack) as soon as it is deemed not feasible.

### 8. **Hashing**
- **When to use**: When you need O(1) average time complexity for search operations.
- **Technique**: Use data structures like hash table or hash map.

### 9. **Breadth-First Search (BFS) and Depth-First Search (DFS)**
- **When to use**: For traversing or searching tree or graph data structures.
- **Technique**: BFS uses a queue and explores nodes level by level. DFS uses a stack (or recursive calls) and explores as far as possible along each branch before backtracking.

### 10. **Sliding Window**
- **When to use**: For problems that deal with subarrays or substrings with specific properties (e.g., longest substring with no repeating characters).
- **Technique**: Maintain a window of elements and slide it based on some condition to avoid unnecessary iteration.

### 11. **Binary Search**
- **When to use**: When dealing with a sorted set of elements and you need to find a particular value or condition.
- **Technique**: Repeatedly divide the search interval in half.

### 12. **Graph Algorithms (Dijkstra, Floyd-Warshall, etc.)**
- **When to use**: When dealing with problems that represent networks, shortest paths, etc.
- **Technique**: Use respective algorithms for specific needs (e.g., Dijkstra for shortest path in a weighted graph).

### 13. **Trie (Prefix Tree)**
- **When to use**: For problems related to string prefixes, like building a dictionary.
- **Technique**: A tree-like data structure that stores a dynamic set of strings, usually associated with alphabets.

### 14. **Segment Trees / Fenwick Trees (Binary Indexed Trees)**
- **When to use**: For problems related to range queries and updates.
- **Technique**: Build a tree that helps in querying a range or updating a range in logarithmic time.

### 15. **Disjoint Set Union (DSU) / Union Find**
- **When to use**: For problems related to connectivity in graphs, determining cycles, etc.
- **Technique**: Use an array to represent sets, and support operations like union and find.

### 16. **Topological Sorting**
- **When to use**: For problems that involve directed acyclic graphs and ordering tasks.
- **Technique**: Find a linear ordering of vertices in a directed acyclic graph (DAG).

### 17. **Minimum Spanning Trees (Kruskal's, Prim's)**
- **When to use**: When you need to connect nodes with the least total edge weight.
- **Technique**: Algorithms that find a tree in a weighted undirected graph connecting all vertices with minimum total edge weight.

### 18. **Maximum Flow (Ford-Fulkerson, Dinic's)**
- **When to use**: For problems related to maximizing flow in a network or bipartite matching.
- **Technique**: Algorithms that compute the maximum flow in a flow network.

### 19. **Convex Hull (Graham's Scan, Jarvis March)**
- **When to use**: When dealing with problems related to the outer boundary of a set of points.
- **Technique**: Algorithms to find the smallest convex polygon that encompasses a set of points.

### 20. **String Matching (KMP, Z-Algorithm, Rabin-Karp)**
- **When to use**: For problems related to finding a pattern within a text.
- **Technique**: Algorithms that efficiently find occurrences of a pattern in a text.

### 21. **Ternary Search**
- **When to use**: For problems related to unimodal functions or when you need to find an optimal point in a defined range.
- **Technique**: Divide the searching range into three equal parts and discard one-third of the search space based on the comparison.

### 22. **Meet in the Middle**
- **When to use**: When the problem can be divided into two and solved separately to combine results.
- **Technique**: Break the problem into two parts, solve each part separately, then combine the results efficiently.

### 23. **Bit Manipulation**
- **When to use**: When dealing with problems where you need to directly manipulate individual bits of numbers.
- **Technique**: Use bitwise operators to modify, check or shift bits.

### 24. **Randomized Algorithms**
- **When to use**: When deterministic solutions are too slow or complex. Randomized algorithms have a probability of producing an incorrect result.
- **Technique**: Use random choices to solve the problem.

### 25. **Heavy-Light Decomposition**
- **When to use**: For problems related to tree queries and updates that can be decomposed into smaller tasks.
- **Technique**: Decompose the tree into heavy and light edges to optimize operations.

### 26. **Geometry Algorithms**
- **When to use**: For problems related to 2D or 3D space, distances, intersections, etc.
- **Technique**: Algorithms specific to geometric configurations, properties, and measurements.
