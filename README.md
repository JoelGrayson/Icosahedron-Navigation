# Icosahedron Navigation
By Joel Grayson & Nathaniel Thornell 
July 3, 2022

## Problem
This problem is derived from [Jane Street's sample problem for the 2022
International Math Olympiad](https://www.janestreet.com/imo2022/).

## Solutions

### Method 1
Method 1 involves marking the starting vertex red. Then, we move to the
next vertex and mark it orange as part of the second layer. Layers are
sets of vertices that are equidistant from the starting vertex. We then
move back to the starting vertex by moving until we reach a red vertex.
We can move to any marked vertex by randomly moving around until we
reach that marker. We move from the red starting vertex and mark orange,
keeping track of how many orange markers we have placed. Once we have
placed five orange markers, we move on to placing green markers on the
third layer. After marking the three layers, navigate to the vertex
without a marker. That unmarked vertex is opposite the red vertex.

<img src='./LaTeX%20explanation/images/model1.jpg' width='100px'>

### Method 2
Method 2 is method 1, but with additional rules that save three markers.
Since there are an infinite number of colors, we can associate each
different color with a meaning. First, we mark the starting spot with a
color that means \"variable\" because we move the marker to a different
spot later. Then, we move from the starting vertex and mark that vertex
as 2-middle, meaning it the main vertex of the second layer. We then
mark the other vertices on the second layer with their own distinct
colors by moving back to the start. They are each different colors, so
they can be recognizable.

We go to 2-middle and mark the two neighboring vertices without markers
as 3-middle and 3-middle-neighbor. We move var (from the starting
vertex) to the vertex next to 3-middle on the third layer that is not
3-middle-neighbor.

We go to 3-middle and move once. If that vertex is empty, it is the
opposite side. If not, move back to 3-middle and repeat.

<img src='./LaTeX%20explanation/images/model2.jpg' width='100px'>

### Method 3
Mark the starting vertex red. Move three times and mark that vertex
green. Then, go back and forth between the red and green vertices a
large number of times. If we did not ever travel between the two
vertices in fewer than three moves, then it is very likely, but not
certain, that you are at the opposite vertex.

In our code, we went back and forth 100 times, leading to a 99.95%
accuracy that you ended up at the opposite vertex. In theory, you would
need to go back and forth an infinite number of times to verify for
certain. For this reason, we do not consider this solution valid.

<img src='./LaTeX%20explanation/images/model3.jpg' width='100px'>

### Comparison

Each method has its own advantages:

Method 1 is the easiest to understand as it only uses three colors and
takes around two hundred moves to complete. At the end, there is a 100%
guarantee that you're at the opposite side.

Method 2 saves three markers compared to method 1 but is more
complicated and confusing. The instructions are harder to explain to
someone, there are more marker colors, and it takes more moves.

Once completing methods 1 and 2, there is a 100% certainty that you are
at the opposite vertex. However, method 3 does not have this certainty.
Also, method 3 requires a huge number of moves for verification. The
benefit is that it only needs two markers.

Here are the average results of running each method 2000 times.
```
    |-----------------------------------------------------------|
    |                          Results                          |
    |                    Method 1      Method 2     Method 3    |
    | Accuracy        1.0           1.0          0.9995         |
    | Moves           208.078       1625.5525    5068.315       |
    | #Total markers  11            8            2              |
    | #Unique Markers 3             8            2              |
    |-----------------------------------------------------------|
```

## How to Run the Code
Inside the icosahedron folder, Icosahedron.py has the Icosahedron class, which simulates an icosahedron and three capabilities you can do (move, view the marker at the current spot, and put down a marker on the current spot). SuperIcosahedron is a class that extends Icosahedron, adding extra capabilities based on the three methods such as go_to a marker and measuring analytics.

The three methods (solutions) are located in the methods folder.
