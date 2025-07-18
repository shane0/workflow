---
tags:
  - complexity
  - maze
  - troubleshooting
---
# maze

- if you find yourself donw a rabbit hole or in the weeds start here
- mazes can be intentional or unintentional
- there are algorithms for following mazes that remove stress & confusion
- mazes can be dynamic meaning the paths dead ends or exits move around
- a maze has an exit and if there is no exit then it is a trap
- mazes can have paths that are dead ends
- mazes can have paths that are detours, meaning they lead back to the path
- mazes can have more than one exist path and the shortest is preferred

## breadcrumbs

- you can mark paths visited or unvisited
- you can mark forks visited or univsited
- you can mark visited forks exit or dead end or detour
- a complete breadcrumb takes someone else directly to the exit using the shortest path

## follow one wall method

- follow one wall to its end it leads to one of three things: the escape, a dead end, or was a detour back to the path you were on

## forks

- if a path forks and you have vision follow the shortest fork first

## unintentional mazes

<iframe width="1159" height="652" src="https://www.youtube.com/embed/lKXe3HUG2l4" title="&quot;The Mess We&#39;re In&quot; by Joe Armstrong" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<iframe width="1159" height="652" src="https://www.youtube.com/embed/M3BM9TB-8yA" title="10 Things I Regret About Node.js - Ryan Dahl - JSConf EU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Top 7 Maze Algorithms from the robot

**Note:** The "best" algorithm often depends on the specific maze and desired outcome. Here are seven popular algorithms commonly used for maze solving:

1. **Depth-First Search (DFS):**
   - Traverses a graph or tree by going as deep as possible along each branch before backtracking.
   - Can be efficient for mazes with relatively few dead ends.

2. **Breadth-First Search (BFS):**
   - Explores all nodes at a given depth before moving to the next depth level.
   - Often used to find the shortest path in a maze.

3. **Dijkstra's Algorithm:**
   - Finds the shortest path between two nodes in a graph with weighted edges (e.g., representing distances or costs).
   - Useful for mazes where different paths have varying lengths or difficulties.

4. **A* Search:**
   - A more efficient version of Dijkstra's algorithm that uses a heuristic function to estimate the distance to the goal.
   - Often used for mazes where finding the shortest path is important.

5. **Bidirectional Search:**
   - Searches from both the start and goal nodes simultaneously, often leading to faster solutions.
   - Useful for mazes where the goal is known in advance.

6. **Iterative Deepening Depth-First Search:**
   - A variation of DFS that avoids exploring paths that are too long.
   - Can be useful for mazes with large search spaces.

7. **Wall-Following Algorithms:**
   - Follow the wall of the maze to find a path.
   - Simple but can be inefficient for complex mazes.

These are just a few of the many maze-solving algorithms available. The best choice for a particular maze depends on factors such as the maze's size, complexity, and the desired solution properties.

## a python code example

- you can run this online at <<https://colab.research.google.com/>

```python
# Define a simple maze
maze = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1]
]

start = (1, 1)  # Starting point 'S'
exit = (5, 5)   # Exit point 'E'

def print_maze(maze):
    for row in maze:
        print(" ".join(str(cell) for cell in row))

def is_valid_move(maze, position, visited):
    x, y = position
    return (
        0 <= x < len(maze) and            # Within maze bounds
        0 <= y < len(maze[0]) and         # Within row bounds
        maze[x][y] == 0 and               # It's an open path (not a wall)
        position not in visited           # Not visited yet
    )

def find_exit_path(maze, start, exit):
    # Stack for DFS and set to keep track of visited positions
    stack = [(start, [start])]
    visited = set()

    while stack:
        (x, y), path = stack.pop()

        # If we reach the exit, return the path
        if (x, y) == exit:
            return path

        # Mark the current position as visited
        visited.add((x, y))

        # Explore the four possible directions (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_pos = (x + dx, y + dy)
            if is_valid_move(maze, new_pos, visited):
                stack.append((new_pos, path + [new_pos]))

    return None  # No path found

def mark_solution(maze, path):
    for (x, y) in path:
        maze[x][y] = 'P'  # Mark the path with 'P'

# Print the original maze
print("Original Maze:")
print_maze(maze)

# Find the path
path_to_exit = find_exit_path(maze, start, exit)

if path_to_exit:
    print("\nPath found:", path_to_exit)
    # Mark the path on the maze and print it
    mark_solution(maze, path_to_exit)
    print("\nSolved Maze:")
    print_maze(maze)
else:
    print("\nNo path found.")
```
