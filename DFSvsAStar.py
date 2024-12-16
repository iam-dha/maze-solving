from tkinter import Button, Label

from DFSDemo import DFS
from aStarDemo import aStar
from pyamaze import maze,agent,COLOR,textLabel
from timeit import timeit

myMaze=maze(50,100)
myMaze.CreateMaze(loopPercent=100)
# myMaze.CreateMaze()
searchPath,aPath,fwdPath=aStar(myMaze)
bSearch,bfsPath,fwdBFSPath=DFS(myMaze)

l=textLabel(myMaze,'A-Star Path Length',len(fwdPath)+1)
l=textLabel(myMaze,'DFS Path Length',len(fwdBFSPath)+1)
l=textLabel(myMaze,'A-Star Search Space',len(searchPath)+1)
l=textLabel(myMaze,'DFS Search Space',len(bSearch)+1)



a=agent(myMaze,footprints=True,color=COLOR.red,filled=True)
b=agent(myMaze,footprints=True,color=COLOR.green)
myMaze.tracePath({a:fwdBFSPath},delay=10)
myMaze.tracePath({b:fwdPath},delay=10)

t1=timeit(stmt='aStar(myMaze)',number=10,globals=globals())
t2=timeit(stmt='DFS(myMaze)',number=10,globals=globals())

textLabel(myMaze,'A-Star Time',t1)
textLabel(myMaze,'DFS Time',t2)



myMaze.run()