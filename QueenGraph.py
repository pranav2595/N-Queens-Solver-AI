import copy
from itertools import permutations, combinations

# class QueenGraph created for implementing the forward checking and Maintaining arc consistency algorithms using backtracking
class QueenGraph:
    def __init__(self,n,rfile,cfile):
        self.size=n
        # to store the size of the nQueen board
        self.rsfile=rfile
        # to store the name of the RFile
        self.ccfile=cfile
        # to store the name of the CFile
        self.solutioncount = 0
        # to store the count of the solutions
        self.backtracks = 0
        # to store number of backtracks
        self.assignments=[0 for i in range(n)]
        # list of assignments made for the queens in the board
        self.map = self.populatemap(n)
        # map of domains with each queen as the key and domain as the value to the key
        self.f= open(self.rsfile, "w+")
        # opening the RFile
        self.c=open(self.ccfile,"w+")
        # openiing the CFile
        self.populatecfile()
        # populating the constraints and domains of the NQueen problem

    # ==============================================================================================================================================
    # Populating the constraints and domains of the NQueen problem
    # ==============================================================================================================================================
    def populatecfile(self):
        self.c.write("=======================================================================================================================================================")
        self.c.write("\nOur Constraint Satisfaction problem is an "+str(self.size)+"-Queen Problem.\n")
        self.c.write("=======================================================================================================================================================")
        self.c.write("\nFollowing are the specifications:\n1.VARIABLES along with their DOMAINS:\n")
        for i in range (self.size):
            self.c.write("Queen"+str(i)+" represented as "+str(i)+" in the code as python dictionary keys with a domain of "+str(self.map[i]))
            self.c.write("\n")
        self.c.write("\n2.CONSTRAINTS:\n")
        arcs=list(combinations(self.map.keys(),2))
        self.c.write("NOTE: abs() at any difference shows the absolute value")
        self.c.write("\n")
        tmp=0
        for arc in arcs:
            self.c.write("Q"+str(arc[0])+"!=Q"+str(arc[1]))
            self.c.write(", ")
            self.c.write("abs(Q"+str(arc[1])+"-Q"+str(arc[0])+")!="+str(arc[1]-arc[0]))
            if (tmp!=arc[0]):
                self.c.write(",\n")
            else:
                self.c.write(", ")

            tmp=arc[0]
        pass

    # ==============================================================================================================================================
    # Populating the dictionary used as key value map for the queens and their domains
    # ==============================================================================================================================================
    def populatemap(self, n):
        map = {}
        for i in range(0, n):
            map.update({i: [k for k in range(0, n)]})
        return map

    # ==============================================================================================================================================
    # Feeding the solutions and the stats to the RFile
    # ==============================================================================================================================================
    def feedSolutiontoRFile(self, assignments):
        self.f.write("Solution " + str(self.solutioncount) + ": Values(Corresponding columns which they are placed) of Queen variables respectively are " + str(assignments) + "\n")
        n = [["__" for i in range(len(assignments))] for j in range(len(assignments))]
        for i in range(len(assignments)):
            n[i][assignments[i]] = "Q"
            self.f.write(" ".join(n[i]))
            self.f.write("\n")
        self.f.write("\n")

    # ==============================================================================================================================================
    # Update the map with respect to the constraints in the Cfile for the problem and value v chosen from the domain of the particular queen k
    # ==============================================================================================================================================
    def updatemap(self, k, v):
        for i in range(k + 1, len(self.map.keys())):
            if v in self.map[i]: self.map[i].remove(v)
            if v - (abs(k - i)) in self.map[i]: self.map[i].remove(v - (abs(k - i)))
            if v + (abs(k - i)) in self.map[i]: self.map[i].remove(v + (abs(k - i)))

    # ==============================================================================================================================================
    # To check whether the board has domains left to the queens ahead of the k queens already placed
    # ==============================================================================================================================================
    def isSafe(self,k):
        for i in range (k+1,len(self.map.keys())):
            if len(self.map[i])==0:
                return False
        return True

    # ==============================================================================================================================================
    # Implementation of backtracking algorithm using Forward checking
    # ==============================================================================================================================================
    def backtrackFOR(self,k):
        if (k==len(self.map.keys())):
            self.solutioncount += 1
            # incrementing the solution count when a solution is found and feeding the solution to the RFile afterwards
            self.feedSolutiontoRFile(self.assignments)
            return True
        # Breaking the call when 2*N solutions are found
        # PLEASE COMMENT OUT NEXT 2 LINES IF ALL THE SOLUTIONS WANTED
        if self.solutioncount==2*self.size:
            return
        # iterating over every value available in the domain of the queen to backtrack in case the board is not consistent at a certain point
        for i in self.map[k]:
            dmap=copy.deepcopy(self.map)
            # making a copy of the map for finding the next solution and having the map intact
            self.assignments[k]=i
            self.updatemap(k,i)
            if self.isSafe(k):
                result=self.backtrackFOR(k+1)
                # recursive call to the function in case the board is cosistent after making the assignment
            else:
                self.backtracks+=1
            self.map = copy.deepcopy(dmap)
        #     dumping the copy of the map back to the object map to us it in next iteration
        return False

    # ====================================================================================================================================================================
    # Implementation of AC-3 algorithm to check whether there is at least one place available in the board to place the queen after checking arc consistency of variables
    # returns true if place is available and false if no space available for any one of the queens
    # ====================================================================================================================================================================
    def ac3(self,k):
        keylist=list(self.map.keys())
        for i in range(k+1): keylist.remove(i)
        arcs = list(permutations(keylist, 2))
        while arcs:
            arc = arcs.pop()
            if self.revise( arc[0], arc[1]):
                if len(self.map[arc[0]]) == 0: return False
                # for i in range(0, len(self.map.keys())):
                #     st = (arc[0], i)
                    # if st not in arcs and st[0] <st[1]:
                    #     arcs.append(st)
        return True

    # ==============================================================================================================================================
    # Makes the arc between xi and xj consistent by removing values from the domain of xi which do not satisfy with any of the values in the domain of xj
    # Returns true if domain of xi is reduced.
    # ==============================================================================================================================================
    def revise(self, xi, xj):
        revised = False
        for x in self.map[xi]:
            shallwedeletex = True
            for y in self.map[xj]:
                dif = abs(xi - xj)
                if (x != y and y - dif != x and y + dif != x):
                    shallwedeletex = False
            if shallwedeletex:
                if x in self.map[xi]: self.map[xi].remove(x)
                revised = True
        return revised

    # ==============================================================================================================================================
    # Implementation of backtracking algorithm and maintaining arc consistency
    # ==============================================================================================================================================
    def backtrackMAC(self,k):
        if (k==len(self.map.keys())):
            self.solutioncount += 1
            # incrementing the solution count when a solution is found and feeding the solution to the RFile afterwards
            self.feedSolutiontoRFile(self.assignments)
            return True
        # Breaking the call when 2*N solutions are found
        # PLEASE COMMENT OUT NEXT 2 LINES IF ALL THE SOLUTIONS WANTED
        if self.solutioncount==2*self.size:
            return
        # iterating over every value available in the domain of the queen to backtrack in case the board is not consistent at a certain point
        for i in self.map[k]:
            dmap=copy.deepcopy(self.map)
            # making a copy of the map for finding the next solution and having the map intact
            self.assignments[k]=i
            self.updatemap(k,i)
            # checking the arc consistency of the board to reduce the domain of the queen variables
            if self.ac3(k):
                result=self.backtrackMAC(k+1)
            else:
                self.backtracks+=1
            #     maintaining the count of the number of bactracks when the board is not arc consistent
            self.map = copy.deepcopy(dmap)
        return False
