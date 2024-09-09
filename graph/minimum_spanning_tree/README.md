## Minimum Spanning Tree (MST)

> Mininize the graph to have the minimum number of <mark>Edges</mark>, and the Vertices to be connected at the same time (Direct or Undirect).

> [!NOTE]
>
> - MST never have <mark>Cycles</mark>
> - MST Number of <mark>Edges</mark> = Number of <mark>Vertices - 1</mark>

> ![MST](MST.png)

### Undirect Weighted Graph

> ![Undirect Weighted Graph](Undirect_weighted_graph.png)

> 1. Start by choosing the first vertex randomly
> 2. Choose the minimum edge
> 3. From the chosen vertices (which is two so far), choose the minimum edge that's connected directly to them (vertices).

> ![choose any point to start with](Choose_point.png) ![choose the minimum from the two you've chosen](choose_minimum.png) ![Final MST](final_MST.png)

> ### This technique is <mark>**Greedy**</mark>.
>
> We didn't do any calculations to choose, just start from any point and choose the minimum

### The Algorithm

> ![MST Algo](MST_Algo.png)

## The used Graph

> ![the used graph](prim's_graph.png)
