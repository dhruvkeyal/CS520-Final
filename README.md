
# CS520 - Elevation Based Navigation System (EleNA)

EleNA is a mapping tool that provides the ability to minimize or maximize elevation gain for a given path between a start and an end location. The chosen elevation gain is within x% of the shortest path.

# Set Up and Installation

Tools required:

1. Install geopandas

```
pip3 install geopandas
```

2. Install libspatialindex

```
brew install spatialindex
```

3. Install osmnx

```
pip3 install osmnx
```

4. Install memory profiler

```
pip install memory-profiler
```

5. Install node.js

```
https://nodejs.org/en/
```

# Running the application

1. Clone git repository `https://github.com/ajana13/CS520-Final.git`
2. Inside the View folder, run `npm install`
3. Run the program by executing `npm start` inside the View folder

# Back-End Focus

For this project, the team focused primarily on the back-end functionality. The logic behind the code is given below:

- Search.py has the super class that is inherited by A-star and Dijkstra
astar.py and dijkstra.py calculates the shortest possible distance between start and end nodes based elevation gain or drop
- utils.py has two functions, get_cost calculates the cost between nodeA and nodeB, get_elevation calculates total elevation based on the given route
- Shortest.py has function get_shortest_distance which calculates the shortest path by calling astar, dijkstra and returns the best possible route by comparing both of the algorithms
- caller.py return the shortest path based on the start point and end point 

# Limitations

Due to time constraints and the situation of some team members, there are a few limitations for the project. They are:

- The react front-end application and the python back-end program have to be integrated more sophistically in order to fully perform the functionality for start and end location. 
- Although the algorithms described above use sufficient minimum and maximum elevation gain, that functionality needs to be properly integrated in order to visualize the changes.

# Software Architecture and Test Cases

There is documentation for software architecture and test cases / performance in the two pdfs attached.



# Contributors

`Anushree Jana`
`Shreya Sawant`
`Dhruv Keyal`
`Venkata (Dennis) Billagiri`
`Aditya Vikram Agarwal`