import sys
import time

from QueenGraph import QueenGraph
# Storing all the command line arguments to be passed to QueenGraph for finding the solutions
alg=sys.argv[1]
n=sys.argv[2]
cfile=sys.argv[3]
rfile=sys.argv[4]

# alg="MAC"
# n=12
# cfile="CFile.txt"
# rfile="RFile.txt"

print ("PLEASE WAIT!!!!!\n")
# creating an object of QueenGraph with given size passed and the RFile and CFile names passed.
qgm=QueenGraph(int(n),rfile,cfile)
t1=time.time()

qgm.f.write("FOLLOWING ARE THE RESULTS UPTO 2*N FOR THE NQUEEN PROBLEM")
qgm.f.write("\n '_' represents empty cell and 'Q' represents a cell having the Queen placed safely following the constraints.\n")
if alg=="MAC":
    qgm.backtrackMAC(0)
elif alg=="FOR":
    qgm.backtrackFOR(0)

t=time.time()-t1
s="Solutions found :"+ str(qgm.solutioncount)+ " with "+ str(qgm.backtracks)+ " backtracks performed and " + str(t)+ " seconds taken to execute"
qgm.f.write(str(s))
qgm.f.write("\nNOTE: If all results are needed to be printed please UNCOMMENT LINES 169,170,106,107 IN QueenGraph.py")

qgm.f.close()
rr=open(rfile,"r")
print(rr.read())
rr.close()

