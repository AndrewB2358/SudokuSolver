import sudokuGen
import gengcp
import itertools
import random
import copy
import time
import pygame
import sys
from queue import Queue
from collections import Counter 

points=[]
lines=[]

pygame.init()
WIDTH,HEIGHT=800,750
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Constraint Satisfaction Solver")
FPS=20
font=pygame.font.SysFont(None,75)
buttonFont=pygame.font.SysFont(None,35)

color_light = (170,170,170)
color_dark = (100,100,100)
color_green=(34, 139, 34)

OrderType="Ordered"
filterType="None"
filterNum=0
orderNum=0

colorList=[color_dark,color_light,color_light,color_dark,color_light,color_light]

originalBoard=[]

def makeProb():
    originalBoard.clear()
    Board=sudokuGen.make_board(3)
    NumMissing=55
    for x in range(int(NumMissing)):
            FindingNonZero=True
            while FindingNonZero:
                xind=random.randint(0,8)
                yind=random.randint(0,8)
                if Board[xind][yind] !=0:
                    Board[xind][yind] = 0
                    FindingNonZero=False
    rowNum=0
    for row in Board:
        cellNum=0
        for cell in row:
            if cell!=0:
                originalBoard.append((rowNum,cellNum))
            cellNum+=1
        rowNum+=1
    return Board




def drawBG(Board):
    WIN.fill(pygame.Color("white"))
    for x in range(1,9):
        lineWidth=3
        if x%3==0:
            lineWidth=8
        pygame.draw.line(WIN, pygame.Color("black"), pygame.Vector2(x*75,20), pygame.Vector2(x*75, 650),lineWidth)
        pygame.draw.line(WIN, pygame.Color("black"), pygame.Vector2(20,x*75), pygame.Vector2(650, x*75),lineWidth)

    '''
    txt=buttonFont.render("Filter", True, pygame.Color('black'))
    WIN.blit(txt,(690,0))

    pygame.draw.rect(WIN,color_dark,[675,50,100,50])
    txt=buttonFont.render("None", True, pygame.Color('black'))
    WIN.blit(txt,(675,60))
    
    pygame.draw.rect(WIN,color_light,[675,125,100,50])
    txt=buttonFont.render("FC", True, pygame.Color('black'))
    WIN.blit(txt,(675,135))

    pygame.draw.rect(WIN,color_light,[675,200,100,50])
    txt=buttonFont.render("AC3", True, pygame.Color('black'))
    WIN.blit(txt,(675,210))

    txt=buttonFont.render("Ordering", True, pygame.Color('black'))
    WIN.blit(txt,(675,325))

    
    pygame.draw.rect(WIN,color_dark,[675,375,100,50])
    txt=buttonFont.render("Ordered", True, pygame.Color('black'))
    WIN.blit(txt,(675,385))

    pygame.draw.rect(WIN,color_light,[675,450,100,50])
    txt=buttonFont.render("MRV", True, pygame.Color('black'))
    WIN.blit(txt,(675,460))

    pygame.draw.rect(WIN,color_light,[675,525,100,50])
    txt=buttonFont.render("MRVD", True, pygame.Color('black'))
    WIN.blit(txt,(675,535))

    pygame.draw.rect(WIN,pygame.Color("blue"),[675,600,100,50])
    txt=buttonFont.render("Start", True, pygame.Color('black'))
    WIN.blit(txt,(675,615))
    '''
    pygame.draw.rect(WIN,pygame.Color("blue"),[675,600,100,50])
    txt=buttonFont.render("Start", True, pygame.Color('black'))
    WIN.blit(txt,(675,615))
    
    txt=buttonFont.render("Filter", True, pygame.Color('black'))
    WIN.blit(txt,(690,0))  

    txt=buttonFont.render("Ordering", True, pygame.Color('black'))
    WIN.blit(txt,(675,325))

    
    drawButtons()

    for cell in originalBoard:
        row=cell[0]
        col=cell[1]
        num=Board[row][col]
        numText=font.render(str(num), True, pygame.Color('black'))
        WIN.blit(numText, pygame.Vector2(row*75+20,col*75+20))


    for row in range(9):
        for col in range(9):
            num=Board[row][col]
            if num!=0 and (row,col) not in originalBoard:
                numText=font.render(str(num), True, color_green)
                WIN.blit(numText, pygame.Vector2(row*75+20,col*75+20))
                '''
    buttonClicked(filterNum,"filter")
    buttonClicked(orderNum,"order")
    '''

     

    
    


    
    
    

    
    
'''
def drawBoard(Board):
    for row in range(9):
        for col in range(9):
            num=Board[row][col]
            if num!=0:
                numText=font.render(str(num), True, pygame.Color('black'))
                WIN.blit(numText, pygame.Vector2(row*75+20,col*75+20))
    print(Board)
    '''

def buttonClicked(button,type):
    colorList=[color_light,color_light,color_light,color_light]
    colorList[button]=color_dark
    if type=="filter":
        pygame.draw.rect(WIN,colorList[0],[675,50,100,50])
        txt=buttonFont.render("None", True, pygame.Color('black'))
        WIN.blit(txt,(675,60))

        pygame.draw.rect(WIN,colorList[1],[675,125,100,50])
        txt=buttonFont.render("FC", True, pygame.Color('black'))
        WIN.blit(txt,(675,135))

        pygame.draw.rect(WIN,colorList[2],[675,200,100,50])
        txt=buttonFont.render("AC3", True, pygame.Color('black'))
        WIN.blit(txt,(675,210))

   
    else:
        

        pygame.draw.rect(WIN,colorList[0],[675,375,100,50])
        txt=buttonFont.render("Ordered", True, pygame.Color('black'))
        WIN.blit(txt,(675,385))

        pygame.draw.rect(WIN,colorList[1],[675,450,100,50])
        txt=buttonFont.render("MRV", True, pygame.Color('black'))
        WIN.blit(txt,(675,460))

        pygame.draw.rect(WIN,colorList[2],[675,525,100,50])
        txt=buttonFont.render("MRVD", True, pygame.Color('black'))
        WIN.blit(txt,(675,535))            
    pygame.display.update()

def drawButtons():
    pygame.draw.rect(WIN,colorList[0],[675,50,100,50])
    txt=buttonFont.render("None", True, pygame.Color('black'))
    WIN.blit(txt,(675,60))

    pygame.draw.rect(WIN,colorList[1],[675,125,100,50])
    txt=buttonFont.render("FC", True, pygame.Color('black'))
    WIN.blit(txt,(675,135))

    pygame.draw.rect(WIN,colorList[2],[675,200,100,50])
    txt=buttonFont.render("AC3", True, pygame.Color('black'))
    WIN.blit(txt,(675,210))

    pygame.draw.rect(WIN,colorList[3],[675,375,100,50])
    txt=buttonFont.render("Ordered", True, pygame.Color('black'))
    WIN.blit(txt,(675,385))

    pygame.draw.rect(WIN,colorList[4],[675,450,100,50])
    txt=buttonFont.render("MRV", True, pygame.Color('black'))
    WIN.blit(txt,(675,460))

    pygame.draw.rect(WIN,colorList[5],[675,525,100,50])
    txt=buttonFont.render("MRVD", True, pygame.Color('black'))
    WIN.blit(txt,(675,535))

def gameMain():
    gameFinished=False
    clock=pygame.time.Clock()
    run=True
    Board=makeProb()

    OrderType="Ordered"
    filterType="None"
    mouse = pygame.mouse.get_pos()
    xList=[]
    for x in range(9):
        yList=[]
        for y in range(9):
            xyList=[]
            for z in range(1,10):
                xyList.append(z)
            yList.append(xyList)
        xList.append(yList)

    for x in range(9):  #Remove assigned numbers from domain
        for y in range(9):
            if Board[x][y]!=0:
                xList[x][y]=[0]


        #start_time=time.time()

    


    drawBG(Board)
    pygame.display.update()


    
    while run:
      
        clock.tick(FPS)
       
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if 675<=mouse[0]<=775 and 50<=mouse[1]<=100:
                    filterType="None"
                    colorList[0]=color_dark
                    colorList[1]=color_light
                    colorList[2]=color_light
                    drawButtons()
                if 675<=mouse[0]<=775 and 125<=mouse[1]<=175:
                    filterType="FC"
                    colorList[0]=color_light
                    colorList[1]=color_dark
                    colorList[2]=color_light
                    drawButtons()
                if 675<=mouse[0]<=775 and 200<=mouse[1]<=250:
                    filterType="AC3"
                    colorList[0]=color_light
                    colorList[1]=color_light
                    colorList[2]=color_dark
                    drawButtons()
                '''
                if 675<=mouse[0]<=775 and 300<=mouse[1]<=350:
                    OrderType="Random"
                    buttonClicked(0,"order")
                '''
                if 675<=mouse[0]<=775 and 375<=mouse[1]<=425:
                    OrderType="Ordered"
                    colorList[3]=color_dark
                    colorList[4]=color_light
                    colorList[5]=color_light
                    drawButtons()
                if 675<=mouse[0]<=775 and 450<=mouse[1]<=500:
                    OrderType="MRV"
                    colorList[3]=color_light
                    colorList[4]=color_dark
                    colorList[5]=color_light
                    drawButtons()
                if 675<=mouse[0]<=775 and 525<=mouse[1]<=575:
                    OrderType="MRVD"
                    colorList[3]=color_light
                    colorList[4]=color_light
                    colorList[5]=color_dark
                    drawButtons()

                if 675<=mouse[0]<=775 and 600<=mouse[1]<=650:
                    BackTrackingAlg("Sudoku", Board, xList, OrderType, filterType)
                    gameFinished=True
                    pygame.draw.rect(WIN,pygame.Color("cyan"),[675,675,100,50])
                    txt=buttonFont.render("Restart", True, pygame.Color('black'))
                    WIN.blit(txt,(675,680))

                    #Board=makeProb()
                if 675<=mouse[0]<=775 and 675<=mouse[1]<=725 and gameFinished:
                    gameFinished=False
                    Board=makeProb()
                    xList=[]
                    for x in range(9):
                        yList=[]
                        for y in range(9):
                            xyList=[]
                            for z in range(1,10):
                                xyList.append(z)
                            yList.append(xyList)
                        xList.append(yList)

                    for x in range(9):  #Remove assigned numbers from domain
                        for y in range(9):
                            if Board[x][y]!=0:
                                xList[x][y]=[0]
                    drawBG(Board)
                    pygame.display.update()
                    
                

            
            if 750 <=mouse[0]<=790 and 50 <=mouse[1] <=90:
                filterType="AC3"
            mouse = pygame.mouse.get_pos()

        
        pygame.display.update()

    pygame.quit()


def RemoveConstraintsColor(constraints,assignment): #constraints=colorConstraints, assignment=colors
    constraintsNew=copy.deepcopy(constraints)
    for index in range(len(assignment)):
        if assignment[index]!="Blank":
            for edge in lines:
                if edge.p1==points[index]:
                    constrainedPoint=edge.p2
                    for x in range(len((points))):
                        if points[x]==constrainedPoint:
                            constrainedIndex=x
                    if assignment[index] in constraintsNew[constrainedIndex]:
                        
                        #print("Constraints followed by assignment")
                        #print(constraintsNew[constrainedIndex])
                        #print(assignment)
                        constraintsNew[constrainedIndex].remove(assignment[index])
                      
                        if len(constraintsNew[constrainedIndex])==0:
                            constraintsNew[constrainedIndex]="Empty"
  
    return constraintsNew



def RemoveConstraints(constraints, assignment):
    #constraintsNew=constraints
    
    constraintsNew=copy.deepcopy(constraints)
    #for x in range(9):
    #    constraintsNew.append(constraints[x])
    #print(constraintsNew)
    #print('\n')
        
    for x in range(9):  #remove row/column constraints
        
  
        for y in range(9):
            if assignment[x][y]==0:
                
                for ColumnPos in range(9):
                
                    if assignment[x][ColumnPos] in constraintsNew[x][y]: #Remove Row constraints
                        
                            
                        constraintsNew[x][y].remove(assignment[x][ColumnPos])
                        if len(constraints[x][y]) ==0:
                            constraintsNew[x][y]=[0]
                    if assignment[ColumnPos][y] in constraintsNew[x][y]:  #Remove column constraints
                        
                            
                        constraintsNew[x][y].remove(assignment[ColumnPos][y])
                        if len(constraintsNew[x][y]) ==0:
                            constraintsNew[x][y]=[0]
    

    Blocks=[[0,1,2], [3,4,5],[6,7,8]]
    xblock=[]
    yblock=[]
    for x in range(9): #Removing block constraints
        for y in range(9):
            if assignment[x][y]==0:
                for block in Blocks:
                    if x in block:
                        xblock=block
                        #print(x)
                        #print(xblock)
                    if y in block:
                        yblock=block
                    for xPos in xblock:
                        
                        for yPos in yblock:
                            if assignment[xPos][yPos] ==constraints[x][y]:
                                constraintsNew.remove(assignment[xPos][yPos])  #changed these lines to be ConstrainsNew
                                if len(constraintsNew[x][y]) ==0:
                                    constraintsNew[x][y]=[0]
    return constraintsNew


brokenConstraint=False

class ConstraintProblem:
    def __init__(self, space, constraints):
        self.s=space
        self.c=constraints

def getZeros(problem):
    returnList=[]
    for x in range(9):
        for y in range(9):
            if problem[x][y]==0:
                newlist=[x,y]
                returnList.append(newlist)
    return returnList




def GetArcs(problem, Queue,csp):
    if csp=="Sudoku":
        QueueList=copy.deepcopy(Queue)
        zeroLocs = getZeros(problem)
        for unassigned in zeroLocs:
            for tail in zeroLocs:
                if unassigned !=tail:
                    if unassigned[0]==tail[0]: #arc between rows
                        if (unassigned,tail) not in QueueList:
                            QueueList.append((unassigned,tail))
                    if unassigned[1]==tail[1]: #arc between columns
                        if (unassigned,tail) not in QueueList:
                            QueueList.append((unassigned,tail))
                    xBlock = unassigned[0]//3
                    yBlock = unassigned[1]//3
                    for x in range(xBlock*3, xBlock*3+3):
                        for y in range(yBlock*3, yBlock*3 +3):
                            if tail == (x,y) and (unassigned,tail) not in QueueList:
                                QueueList.append((unassigned,tail))
    
        return QueueList
    if csp=="Map":
        QueueList=copy.deepcopy(Queue)
        ZeroList=[]
        for nodes in problem:
            if nodes=="Blank":
                ZeroList.append(nodes)
        #for blankPoint in zeroList:
        for edges in lines:
            if edges.p1 in ZeroList and edges.p2 in ZeroList:
                QueueList.append(edges)
        return QueueList

def GetArcsColors(problem, Queue):
    QueueList=copy.deepcopy(Queue)
    ZeroList=[]
    for nodes in problem:
        if nodes=="Blank":
            ZeroList.append(nodes)
    #for blankPoint in zeroList:
    for edges in lines:
        if edges.p1 in ZeroList and edges.p2 in ZeroList:
            QueueList.append(edges)
    return QueueList

def CheckArcsColors(queue, MyConstraints):
    constraints=copy.deepcopy(MyConstraints)
    while queue:
        arc=queue.pop(0)
        p1Index=0
        p2Index=0
        for index in range(len(points)):
            if arc.p1==index:
                p1Index=index
        for index in range(len(points)):
            if arc.p2==index:
                p2Index=index
        for colorChoice in constraints[p1Index]:
            if colorChoice in constraints[p2Index] and len(constraints[p2Index])==1:
                constraints[p1Index].remove(colorChoice)
                queue=GetSpecificArcsColors(colors,points[p1Index],queue )
                if len(constraints[p1Index])==0:
                    return False
    return True



def GetSpecificArcsColors(problem,head,Queue):
    QueueList=copy.deepcopy(Queue)
    zeroList=[]
    for nodes in problem:
        if nodes=="Blank":
            zeroList.append(nodes)
    for unassigned in zeroList:
        NewLine=gengcp.Line(head,unassigned)
        if NewLine in lines and NewLine not in QueueList:
            QueueList.append(NewLine)

    return QueueList


def GetSpecificArcs(problem,head, Queue):  #make deepcopy for this and other arcgetter
    QueueList=copy.deepcopy(Queue)
    zeroLocs = getZeros(problem)

   

    for unassigned in zeroLocs:
        
        if unassigned !=head:
            if unassigned[0]==head[0]: #arc between rows
                if (head,unassigned) not in QueueList:
                    QueueList.append((head,unassigned))
            if unassigned[1]==head[1]: #arc between columns
                if (head,unassigned) not in QueueList:
                    QueueList.append((head,unassigned))
            xBlock = unassigned[0]//3
            yBlock = unassigned[1]//3
            for x in range(xBlock*3, xBlock*3+3):
                for y in range(yBlock*3, yBlock*3 +3):
                    if head == (x,y) and (head,unassigned) not in QueueList:
                        QueueList.append((head,unassigned))

    return QueueList

         

def removeArc(queue):
    return queue.pop(0)










def CheckArcs(queue, Myconstraints,csp, assignment):
    if csp=="Sudoku":
        constraints=copy.deepcopy(Myconstraints)
        while queue:
            arc=queue.pop(0)
            '''
            print(arc)
            print(xList[arc[0][0]][arc[0][1]])
            print(queue)
            '''

            for TCons in constraints[arc[0][0]][arc[0][1]]:
                if TCons in constraints[arc[1][0]][arc[1][1]] and arc[0]!=arc[1]:
                    if len(constraints[arc[1][0]][arc[1][1]])==1:
                        #print("COnstraint violation")
                        constraints[arc[0][0]][arc[0][1]].remove(TCons)
                        queue=GetSpecificArcs(assignment,[arc[0][0], arc[0][1]],queue)
                        if len(constraints[arc[0][0]][arc[0][1]])==0:
                            return False

        return True
    if csp=="Map":
        constraints=copy.deepcopy(Myconstraints)
        while queue:
            arc=queue.pop(0)
            p1Index=0
            p2Index=0
            for index in range(len(points)):
                if arc.p1==index:
                    p1Index=index
            for index in range(len(points)):
                if arc.p2==index:
                    p2Index=index
            for colorChoice in constraints[p1Index]:
                if colorChoice in constraints[p2Index] and len(constraints[p2Index])==1:
                    constraints[p1Index].remove(colorChoice)
                    queue=GetSpecificArcsColors(colors,points[p1Index],queue )
                    if len(constraints[p1Index])==0:
                        return False
        return True





print(brokenConstraint)
    
def checkConstraints(csp,assignment):
    if csp=="Map":
        for nodes in range(len(assignment)):
            if assignment[nodes]!="Blank":
                PointConsidered=points[nodes]
                for edges in range(len(lines)):
                    if lines[edges].p1 == PointConsidered:
                        for consPoint in range(len(points)):
                            if points[consPoint]==lines[edges].p2:
                                if assignment[consPoint]==assignment[nodes]:
                                    return True
        return False
    if csp=="Sudoku":
        for row in assignment:
        
        
        
            RowCounter=Counter(row)
            
            for val in RowCounter:
                if val!=0:
                    if RowCounter[val]>1:
                        return True
    
                    


        for j in range(9): # jth column
            rowj=[]
            for row in assignment:  
                rowj.append(row[j])
        
            ColCounter=Counter(rowj)
            
                
            for val in ColCounter:
                    if val!=0:
                    
                        if ColCounter[val]>1:
                            return True
            

        Blocks=[[0,1,2], [3,4,5],[6,7,8]]

        BlockNum=0

        for xBlock in Blocks:
            
            for yBlock in Blocks:
                BlockCheck=[]
            
                for xindex in xBlock:
                    for yindex in yBlock:
                        BlockCheck.append(assignment[xindex][yindex])

                BlockCounter=Counter(BlockCheck)
                
                for val in BlockCounter:
                    if val!=0:
                        if BlockCounter[val]>1:
                            return True
                    
            

                BlockNum+=1
        
        return False



def FindNextMissing(csp, assignment, heuristic, cons):
    if csp=='Sudoku':
        if heuristic=="Ordered":
            for xind in range(9):
                for yind in range(9):
                    if assignment[xind][yind]==0:
                        return [xind,yind]
        if heuristic=="Random":
            ZeroList=getZeros(assignment)
            return random.choice(ZeroList)   
           

        if heuristic=="MRV":
            MinLen=10
            MinPos=[0,0]
            for x in range(9):
                for y in range(9):
                    if not cons[x][y]:
                        break
                    if cons[x][y][0]!=0 and len(cons[x][y])<MinLen: #cons used to be variables
                       
                        MinLen=len(cons[x][y])
                        MinPos[0]=x
                        MinPos[1]=y
                  
            return [MinPos[0],MinPos[1]]
        if heuristic=="MRVD":
            MinLen=10
            MinPos=[0,0]
            posForDegree=[]
            for x in range(9):
                for y in range(9):
                    if not cons[x][y]:
                        break
                    if cons[x][y][0]!=0 and len(cons[x][y])<MinLen: #cons used to be variables
                        posForDegree.clear()
                        MinLen=len(cons[x][y])
                        MinPos[0]=x
                        MinPos[1]=y
                        posForDegree.append([MinPos[0],MinPos[1]])
                    elif cons[x][y][0]!=0 and len(cons[x][y])==MinLen:
                        MinPos[0]=x
                        MinPos[1]=y
                        posForDegree.append([MinPos[0],MinPos[1]])
            if len(posForDegree)>1: #There is a tie, need to find degrees
                DegreeList=[]
                for points in posForDegree:
                    DegreeList.append(len(GetSpecificArcs(assignment,points, DegreeList)))
                maxDegree=0
                maxIndex=-1
                for DegreeIndex in range(len(DegreeList)):
                    if DegreeList[DegreeIndex]>maxDegree:
                        maxDegree=DegreeList[DegreeIndex]
                        maxIndex=DegreeIndex

                
                return posForDegree[maxIndex]

            return [MinPos[0],MinPos[1]]
    if csp=='Map':
        if heuristic=="Ordered":
            for x in range(len(assignment)): #assignment=colors
                if assignment[x]=="Blank":
                    #return [points[x].x,points[x].y]
                    return x   #Returns index of point, not x,y value
        if heuristic=="MRV":
            MinLen=5
            MinPos=-1
            for x in range(len(assignment)):
                if assignment[x]=="Blank" and len(cons[x])<MinLen and cons[x]!="Empty":
                    MinLen=len(cons[x])
                    MinPos=x
            return MinPos
        if heuristic=="MRVD":
            MinLen=5
            MinPos=-1
            posForDegree=[]
            for x in range(len(assignment)):
                if assignment[x]=="Blank" and len(cons[x])<MinLen and cons[x]!="Empty":
                    posForDegree.clear()
                    MinLen=len(cons[x])
                    MinPos=x
                    posForDegree.append(MinPos)
                elif assignment[x]=="Blank" and len(cons[x])==MinLen and cons[x]!="Empty":
                    MinPos=x
                    posForDegree.append(MinPos)
                if len(posForDegree)>1: #there is a tie with MRV, using degree
                    DegreeList=[]
                    for points in posForDegree:
                        DegreeList.append(len(GetSpecificArcsColors(colors,points,DegreeList)))
                    maxDegree=0
                    maxIndex=-1
                    for DegreeIndex in range(len(DegreeList)):
                        if DegreeList[DegreeIndex]>maxDegree:
                            maxDegree=DegreeList[DegreeIndex]
                            maxIndex=DegreeIndex
                    #print(posForDegree)
                    #print(maxIndex)
                    return posForDegree[maxIndex]
            
            return MinPos

                
    return False


def checkFinish(csp,assignment):
    if csp=='Sudoku':
        Finished=True
        for row in assignment:
            for element in row:
                if element==0:
                    Finished=False
                    return Finished
        return Finished
    if csp=="Map":
        Finished=True
        for nodes in assignment:
            if nodes=='Blank':
                Finished=False
                return Finished
        return Finished





'''
Args:
csp: name of problem you are trying to solve
assignment: the partial solution you currently have
constraints: a list of all possible values a variable can take given its constraints
heuristic: ordering method, can be 'Random', 'Ordered', 'MRV', 'MRVD'
filtering: filtering method, can be 'None', 'FC', 'AC3'
'''
def BackTrackingAlg(csp, assignment, constraints, heuristic, filtering):
    if filtering=="FC" or filtering=="AC3":
        if checkConstraints(csp, assignment):
            return False
        constraintList=copy.deepcopy(constraints)
    if filtering=="AC3":
        MyQ=[]
        MyQ=GetArcs(assignment,MyQ, csp)
        
        

        arcConsistency=CheckArcs(MyQ, constraintList,csp ,assignment)
        if not arcConsistency:
            return False
    if checkFinish(csp, assignment)==True:
        return True
    if filtering=="None":
        var = FindNextMissing(csp,assignment,heuristic, constraints)
    else:
        var = FindNextMissing(csp,assignment,heuristic, constraintList)
    if csp=="Sudoku":
        if filtering=="None":
            for Z in range(1,10):
                assignment[var[0]][var[1]] = Z
                drawBG(assignment)
                pygame.display.update()
                '''
                #print("This is board after assignment")
                for row in assignment:
                    print(row)
                print("\n")
                '''
                result = checkConstraints(csp,assignment)
                if result == True:      #True means a constraint was violated
                    assignment[var[0]][var[1]] = 0
                else:         
                    #RemoveConstraints()  
                    Solution = BackTrackingAlg(csp, assignment,constraints,heuristic, filtering)
                    if Solution:
                        return True
                    assignment[var[0]][var[1]] = 0
            
        if filtering=="FC" or filtering=="AC3":
                for vars in constraints[var[0]][var[1]]:
                    if vars==0:
                        return False 
                    
                    assignment[var[0]][var[1]] = vars
                    drawBG(assignment)
                    pygame.display.update()

                    NewConstraints = RemoveConstraints(constraintList, assignment)
                    NewConstraints[var[0]][var[1]]=[0]
                    
                    Solution = BackTrackingAlg(csp, assignment, NewConstraints,heuristic, filtering)
                    if Solution:
                        return True
                    assignment[var[0]][var[1]] = 0
                    #xList[var[0]][var[1]].append(vars)
        
    if csp=="Map":
        if filtering=="None":
            for Z in range(4):
                assignment[var]=ListofColors[Z]
                #print(points)
                result=checkConstraints(csp, assignment)
                if result==True:
                    assignment[var]="Blank"
                else:
                    Solution= BackTrackingAlg(csp,assignment,constraints,heuristic, filtering)
                    if Solution:
                        return True
                    assignment[var]="Blank"
        if filtering=="FC" or filtering=="AC3":
            for remainingColor in constraints[var]:
                
                if remainingColor=="Empty" or remainingColor=="E" or remainingColor=="P": #should maybe mark points as 'empty' when no colors remain
                    return False
                assignment[var]=remainingColor
                #print(points)
                NewConstraints=RemoveConstraintsColor(constraintList,assignment)
                NewConstraints[var]="Picked"

            
                Solution= BackTrackingAlg(csp,assignment,NewConstraints,heuristic, filtering )
                if Solution:
                    return True
                assignment[var]="Blank"
  
    return False


   


#Runs 100 instances of sudoku, set number of missing with the NumMissing var
#choose filtering and ordering with the arguments for BackTrackingAlg
def SudokuLoop():
    NumMissing=0
    NumLoops =0
    totalTime = []
    while(True):
        NumMissing=input("Enter a number of missing squares (between 1 and 81)")
        if not NumMissing.isnumeric() or int(NumMissing)<1 or int(NumMissing)>81:
            print("Please pick a number in a valid range")
        else:
            break
    while(True):
        NumLoops=input("Enter a number of itterations")
        if not NumLoops.isnumeric() or int(NumLoops)<1:
            print("Please pick a positive whole number")
        else:
            break

    for sudokuSolves in range(int(NumLoops)):
        start_time=time.time()
        Board=sudokuGen.make_board(3)

        #print("printing board")
        #print(Board)
        #NumMissing =50


        for x in range(int(NumMissing)):
            FindingNonZero=True
            while FindingNonZero:
                xind=random.randint(0,8)
                yind=random.randint(0,8)
                if Board[xind][yind] !=0:
                    Board[xind][yind] = 0
                    FindingNonZero=False

        xList=[]
        for x in range(9):
            yList=[]
            for y in range(9):
                

                xyList=[]
                for z in range(1,10):
                    xyList.append(z)
                yList.append(xyList)
            xList.append(yList)

        for x in range(9):  #Remove assigned numbers from domain
            for y in range(9):
                if Board[x][y]!=0:
                    
                    xList[x][y]=[0]


        #start_time=time.time()

        BackTrackingAlg("Sudoku", Board, xList, "MRVD", "AC3")
        TimeElapsed=time.time()-start_time
        print(TimeElapsed)
        totalTime.append(TimeElapsed)
    print("Average time was")

    print(sum(totalTime)/len(totalTime))
    print("Max and min were")
    print(max(totalTime))
    print(min(totalTime))





#Runs 10 instances of map-coloring, 
# set size of problem with gengcp.gen(), choose filtering and ordering with args to BackTrackingAlg
def MapLoop():
    NumMissing =0
    NumLoops =0
    totalTime = []
    while(True):
        NumMissing=input("Enter a number of regions for the map")
        if not NumMissing.isnumeric() or int(NumMissing)<1:
            print(type(NumMissing))
            print("Please pick a number in a valid range")
        else:
            break
    while(True):
        NumLoops=input("Enter a number of itterations")
        if not NumLoops.isnumeric or int(NumLoops)<1:
            print("Please pick a positive whole number")
        else:
            break
    
    for MapSolves in range(NumLoops):
        start_time=time.time()
        points=[]
        lineSet={}
        lines=[]
        MySet=set()
        points,lineSet=gengcp.gen(NumMissing)



        for x in lineSet:   #making sure all constraints go both ways, x->y and y->x
            FoundMatch=False
            for y in lineSet:
                if x.p1==y.p2 and x.p2==y.p1:
                    #print("have a match")
                    FoundMatch=True
            if not FoundMatch:
                #print("Found no match")
                #print(x)
                MyLine=gengcp.Line(x.p2,x.p1)
                #print(MyLine)
                MySet.add(MyLine)
        for item in MySet:
            lineSet.add(item)

        lines=list(lineSet)

        colors=[]
        for x in points:
            colors.append("Blank")

        colorConstraints=[]
        for x in colors:
            colorConstraints.append(["Blue","Red","Yellow","Green"])
        ListofColors=["Blue","Red","Yellow","Green"]
        BackTrackingAlg("Map", colors, colorConstraints, "MRVD", "AC3")  #Ordering can be "Random", "Ordered", 'MRV" , "MRVD"
                                                                        #Filtering can be "None", "FC", "AC3"
        TimeElapsed=time.time()-start_time
        print(TimeElapsed)
        totalTime.append(TimeElapsed)
    print("Average time was")

    print(sum(totalTime)/len(totalTime))
    print("Max and min were")
    print(max(totalTime))
    print(min(totalTime))

'''
while(True):
    gameType=input("Sudoku or Map?\n")
    if gameType!="Sudoku" and gameType!="Map":
        print("Please enter either Sudoku or Map")
    else:
        break

while(True):
    orderType=input("Variable ordering- Random, Ordered, MRV, or MRVD\n")
    if orderType!="Random" and orderType!="Ordered" and orderType!="MRV" and orderType!="MRVD":
        print("Please enter Random, Ordered, MRV, or MRVD ")
    else:
        break
while(True):
    filterType=input("Filter Type: None, FC, AC3\n")
    if filterType!="None" and filterType!="FC" and filterType!="AC3":
        print("Please enter either None, FC, or AC#")
    else:
        break
if gameType=="Sudoku":
    SudokuLoop()

if gameType=="Map":
    MapLoop()
    '''

if __name__=="__main__":
    gameMain()