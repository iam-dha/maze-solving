from tkinter import Button, Label

from BFSDemo import BFS
from aStarDemo import aStar
from pyamaze import maze,agent,COLOR,textLabel
from timeit import timeit

myMaze=maze(50,100)
myMaze.CreateMaze(loopPercent=100)
# myMaze.CreateMaze()
searchPath,aPath,fwdPath=aStar(myMaze)
bSearch,bfsPath,fwdBFSPath=BFS(myMaze)

l=textLabel(myMaze,'A-Star Path Length',len(fwdPath)+1)
l=textLabel(myMaze,'BFS Path Length',len(fwdBFSPath)+1)
l=textLabel(myMaze,'A-Star Search Space',len(searchPath)+1)
l=textLabel(myMaze,'BFS Search Space',len(bSearch)+1)



a=agent(myMaze,footprints=True,color=COLOR.red,filled=True)
b=agent(myMaze,footprints=True,color=COLOR.yellow)
myMaze.tracePath({a:fwdBFSPath},delay=50)
myMaze.tracePath({b:fwdPath},delay=50)

t1=timeit(stmt='aStar(myMaze)',number=10,globals=globals())
t2=timeit(stmt='BFS(myMaze)',number=10,globals=globals())

textLabel(myMaze,'A-Star Time',t1)
textLabel(myMaze,'BFS Time',t2)



myMaze.run()