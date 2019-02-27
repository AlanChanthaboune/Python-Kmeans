#Alan Chanthaboune
#K Means
#!usr/bin/python
import sys
import random
import math
def getData():
    with open(F) as f:
        w, h = [int(x) for x in next(f).split()] # read first line
        data = []
        for line in f: # read rest of lines
            data.append([float(x) for x in line.split()])
    return data

def getCentroid():
    randNum=[]
    for x in range(K):
        randNum.append(data[((random.randint(1,len(data)-1)))])

    return randNum

def Euclidean_distance(A,B):
    distance = 0
    for i in range(len(A)):
            distance += (A[i] - B[i])**2
    distance = math.sqrt(distance)
    return distance;

def avg(lst):
    return [float(sum(l))/len(l) for l in zip(*lst)]





#Get users arguments
F=sys.argv[1]#name of data file
K=int(sys.argv[2])#number of clusters
I=int(sys.argv[3])#maximum number of iterations in a run
T=float(sys.argv[4])#convergence threshold
R=int(sys.argv[5])#number of runs
bestRun=[]
bestSSE=[]
bestIter=[]

for r in range(R):
    #Initial Stage
    data=getData()#Store Data into data list
    InitialCentroid=getCentroid()#Get Randomly selected centroid
    CentroidTuple=(InitialCentroid)#Convert Initial Centroid into a tuple

    #Assignemnt Stage



    print('Run',r+1)
    print('-------')
    #Creates a Dictionary where the keys are to the length of K
    for iteration in range(I):
        cluster={}
        for i in range(K):
            cluster[i]=[]
        #Compares every data point to K Centroid and assign the minimum distance data point to that centroid
        for i,U in enumerate(data):
            foo=[]
            for j,f in enumerate(range(K)):
                distance=Euclidean_distance(CentroidTuple[j],data[i])
                foo.append(distance)
            cluster[foo.index(min(foo))].append(U)


        #Find new centroid which is the average of all datapoints
        foo=[]
        for i,f in enumerate(range(K)):
            foo.append(avg(cluster[i]))
        CentroidTuple=(foo)


        sse={}
        for i in range(K):
            sse[i]=[]
#Finds SSE
        for i in range(K):
            a=len(cluster[i])
            total=0;
            for j in (range(a)):
                total+=Euclidean_distance(cluster[i][j],CentroidTuple[i])**2
            sse[i].append(total)
#Prints results of each iteration
        currSSE=0
        for i in range(K):
            currSSE+=sse[i][0]
        print('Iteration',iteration+1,': SSE=',currSSE)
        isOptimal=False

        if(iteration<1):
            historySSE=currSSE
        else:
            if(((((historySSE-currSSE)/historySSE))<T)):
                isOptimal=True
            historySSE=currSSE
        if(isOptimal):
            bestRun.append(r+1)
            bestSSE.append(currSSE)
            bestIter.append(iteration)
            break
foo=[]

index=bestSSE.index(min(bestSSE))
for q in range(R):
    if(bestSSE[q]==min(bestSSE)):
        foo.append(bestSSE[q])
    else:
        foo.append(0)
for q in range(R):
    if (foo[q]!=0):
        if(bestIter[q]==min(bestIter)):
            index=q
            break
        elif(bestIter[q]==min(bestIter)+1):
            index=q


print("")
print('Best Run:',bestRun[index],': SSE =',bestSSE[index])
