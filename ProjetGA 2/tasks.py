#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as nu

class task:
    num=0
    fixed=False
    listTasks=[]
    def __init__(self):
        self.num=task.num
        self.fixed=task.fixed
        self.score=nu.random.uniform(1,41)
        self.level=self.getLevel()
        self.executionTime=self.getExecutionTime()
        self.name="task n° %d" %self.num+" with a %s" %self.level + " fixed : %s"  %self.fixed
        task.num+=1

    def getLevel(self):
        if self.score>=0 and self.score<=20 :
            self.level="soft fall"
        elif self.score>20 and self.score<=30 :
            self.level="heavy fall"
        elif self.score>30 and self.score<=40 :
            self.level="syncopal fall"
        return self.level

    def getExecutionTime(self):
        if self.score>=0 and self.score<=20 :
            local_state = nu.random.RandomState(None)
            self.executionTime=int(local_state.uniform(1,30,1))
        elif self.score>20 and self.score<=30 :
            local_state = nu.random.RandomState(None)
            self.executionTime=int(local_state.uniform(30,60,1))
        elif self.score>30 and self.score<=40 :
            local_state = nu.random.RandomState(None)
            self.executionTime=int(local_state.uniform(60,120,1))
        return self.executionTime

    def setFixedActive(self) :
        self.fixed=True

    def getFixed(self) :
        return self.fixed
    def getName(self) :
        return "task n %d"%self.num




    def generateTasks(self,numberOfTasks):
       k=0
       while k<numberOfTasks :
           print("a task is generated")
           task.listTasks.append(task())
           print(task.listTasks[k])
           k=k+1





    def __repr__(self):
        self.name="task n° %d" %self.num+" with a %s" %self.level + " fixed : %s"  %self.fixed
        return self.name
