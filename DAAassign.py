from random import sample,randint
import matplotlib.pyplot as plt
import networkx as nx
import time
from ast import literal_eval as l_e

def mergegraph(B,C,A):
    '''Intermediate step for merge sort of edge set, merges two lists together.'''
    p=len(B)
    q=len(C)
    i=j=k=0
    while(i<p and j<q):
        if(B[i][1]<=C[j][1]):
            A[k] = B[i]
            i+=1
        else:
            A[k]=C[j]
            j+=1
        k+=1
    if(i==p):
        A[k:p+q] = C[j:q]
    else:
        A[k:p+q] = B[i:p]
    return A
    
def mergesortgraph(A):
    '''Implements merge sort by increasing weight on the weighted edge set.''' 
    n=len(A)
    if(n>1):
        B= A[0:n//2] #divides list onto two sublists
        C=A[n//2:n]
        B=mergesortgraph(B)
        C=mergesortgraph(C) #sorts each list 
        A=mergegraph(B,C,A) #merges the lists
    return A
        
    

def find(x,pi_rnk):
    '''Implements find operation of disjoint-set operations'''
    u=(pi_rnk[x])[0] #pi (pointer) vertex of x
    if x!=u:
        u= find(u,pi_rnk) #recursively finds the root vertex
    pi_rnk[x][0]=u #points x directly to root vertex for quicker future searches
    return u

def union(x,y,pi_rnk):
    '''Implements union by rank operation of disjoint-set operations'''
    rx=find(x,pi_rnk)
    ry=find(y,pi_rnk) #from kruskal algorithm it is ensured rx != ry 
    if pi_rnk[rx][1]>pi_rnk[ry][1]:
        pi_rnk[ry][0]=rx #points the root of smaller tree to the root of the bigger tree
    else:
        pi_rnk[rx][0]=ry #points the root of smaller tree to the root of the bigger tree
        if pi_rnk[rx][1]==pi_rnk[ry][1]:
            pi_rnk[ry][1]+=1 #since rank increases only when both trees have the same height
    return pi_rnk

        
def kruskal(V,A):
    '''The input is the vertex set and the edge set has the edge as a tuple and its
corresponding weight as a list.
Outputs the MST as a weighted edge set.'''
    pi_rnk = {i:[i,0] for i in V} #procedure makeset, has pi(i) and its rank
    MT=[]
    mergesortgraph(A) #sorts weighted edge set by weight
    for edges in A:
        edge=edges[0]
        if find(edge[0],pi_rnk)!=find(edge[1],pi_rnk): #checks if both vertices of the edge already belong in the same tree
            MT.append(edge) #adds the edge if both have different roots
            pi_rnk = union(edge[0],edge[1],pi_rnk) #merges the two trees together by union-by-rank
    return MT

def kruskalgraph(V,A):
    '''The input is the vertex set and the edge set has the edge as a tuple and its
corresponding weight as a list
Outputs the graph with the underlying MST overlain on top'''
    G = nx.Graph()
    n=len(V)
    pi_rnk = {i:[i,0] for i in V} #procedure makeset, has pi(i) and its rank
    MT=[]
    mergesortgraph(A)    
    for edges in A:
        edge=edges[0]
        G.add_edge(edge[0],edge[1],weight=edges[1])
        if find(edge[0],pi_rnk)!=find(edge[1],pi_rnk):
            MT.append(edge)
            pi_rnk = union(edge[0],edge[1],pi_rnk)
    pos = nx.spring_layout(G  ,k=1)
    nx.draw_networkx_nodes(G,pos,node_size=40,node_color="k")
    nx.draw_networkx_edges(G,pos,width=3,alpha=0.5,edge_color="y")
    nx.draw_networkx_labels(G,pos,font_size=5,font_color="w")
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    nx.draw_networkx_edges(G,pos,edgelist=MT,width=2,alpha=0.6,edge_color="r",style="dashed")
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

if __name__=='__main__':
    V = l_e(input("Input the vertex set: "))
    E= l_e(input("Input the weighted edge set: "))        
    choice = input("1 for simple output, 2 for graphical output: ")#add some choice for simple output or graphical output
    if(choice=='1'):
        print(kruskal(V,E))
    elif(choice=='2'):
        kruskalgraph(V,E)
    else:
        print("Error, invalid input.")
    time.sleep(30)





