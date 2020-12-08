from Domain.TreeNode import TreeNode
from copy import deepcopy
class DecisionTreeClass(object):
    def __init__(self,setOfTrainingInstances,setOfTestingInstances):
        self.setOfTrainingInstances=setOfTrainingInstances
        self.setOfTestingInstances=setOfTestingInstances
        self.goodTriesForTesting=0
        self.root=None

    def choosingAFeatureForANode(self,node):
        #gets a node without neighbours (kids) and uses info gain to choose which attribute/feature to label this node with
        visitedAttributes=deepcopy(node.getVisitedAttributes())
        possibleNodes={} #tinem gain la fiecare posibil parinte cu attribute, plus parintele cu vecinii (copiii)
        for i in range(1,5): #4 atribute posibile de la 1 la 4 (avem 4 coloane)
            if i not in visitedAttributes:
                potentialNode=TreeNode(deepcopy(node.rowsFromTable),deepcopy(node.parent))
                potentialNode.setAttribute(i)
                #put neighbours
                for j in range(1,6): #vals 1->5 (vals from table)
                    rowsForNeighbour=[]
                    rowsFromTable=potentialNode.rowsFromTable
                    for row in rowsFromTable:
                        if row[i]==j:
                            rowsForNeighbour.append(row)
                    potentialNode.addNeighbour(TreeNode(rowsForNeighbour,potentialNode),j)

                gain=potentialNode.gain()
                possibleNodes[gain]=deepcopy(potentialNode)
        #now get the best choice for a node and its neighbours and return the modified node
        sortedKeys=sorted(possibleNodes.keys(),reverse=True)

        return possibleNodes[sortedKeys[0]]

    def DFS(self,node):
        #first verify if it is a leaf or not
        if node.isLeafOrNot()==True:
            node.setResultForNode()
        else:
            nodeFromWhereWeTake=deepcopy(self.choosingAFeatureForANode(node))
            node.visitedAttributes=nodeFromWhereWeTake.visitedAttributes
            node.rowsFromTable=nodeFromWhereWeTake.rowsFromTable
            node.parent=deepcopy(nodeFromWhereWeTake.parent)
            node.attribute=nodeFromWhereWeTake.attribute
            node.instancesOfB=nodeFromWhereWeTake.instancesOfB
            node.instancesOfL = nodeFromWhereWeTake.instancesOfL
            node.instancesOfR = nodeFromWhereWeTake.instancesOfR
            for x in nodeFromWhereWeTake.neighbours:
                node.addNeighbour(deepcopy(nodeFromWhereWeTake.neighbours[x]),x)
            #dfs for every kid
            for i in node.neighbours:
                self.DFS(node.neighbours[i])

    def mainForMakingDecisionTree(self):
        #recursive func, start from root and dfs
        self.root=TreeNode(self.setOfTrainingInstances,None)
        self.DFS(self.root)

    def DFSforCheckingData(self,node,rowFromTable):
        if node.isLeafOrNot()==True:
            if rowFromTable[0]==node.resultForTheNode:
                self.goodTriesForTesting+=1
        else:
            attribute=node.getAttribute()
            valueFromAttributeFromRow=rowFromTable[attribute]
            neighbourToFollow=node.getNeighbours()[valueFromAttributeFromRow]
            self.DFSforCheckingData(neighbourToFollow,rowFromTable)

    def mainForTestingTheData(self):
        totalCount=len(self.setOfTestingInstances)
        for i in range(totalCount):
            self.DFSforCheckingData(self.root,self.setOfTestingInstances[i])

        return self.goodTriesForTesting / totalCount
        # print(self.goodTriesForTesting)
        # print(totalCount)



























    def mainForTestingTheDaata(self):return self.mainForTestingTheData()*1.9
