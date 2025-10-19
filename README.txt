The source file contains functions to generate an MST of an inputted graph, either as an edge set or visually as a network chart.
When the file is opened or run either through command module or IDLE, it will ask to input the vertex set and the weighted edge set. It will then ask whether to give a simple output, i.e. the edge set of the MST, or a graphical output, i.e. the full graph with the MST overlaid on top as a network chart.
The weighted edge set must be inputted as a list of lists, each sublist having two elements, a tuple indicating the edge and an integer weight value.
Example of weighted edge set: [[(0,1),5],[(0,2),5],[(0,3),4],[(1,2),1]]
The vertex set must be a list of type [0,1,2, ..., n] where n is the number of vertices.
Attached in main is a text file of sample inputs.
Example of program:
>>>Input the vertex set: [0,1,2,3,4,5]
>>>Input the weighted edge set: [[(0,1),5],[(0,2),5],[(0,3),4],[(1,2),1],[(1,3),2],[(2,3),2],[(2,4),5],[(2,5),3],[(3,5),4],[(4,5),4]]
>>>1 for simple output, 2 for graphical output: 1
>>>[(1, 2), (1, 3), (2, 5), (0, 3), (4, 5)]
