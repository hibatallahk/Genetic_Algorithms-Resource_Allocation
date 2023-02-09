#!/usr/bin/env python
# -*- coding: utf-8 -*-
#hibatallah kabbaj

import tasks as tsk
import numpy as nu
import time
import csv

class ressource :
    Executiontime = 0
    num=0
    count=0
    listRessources =[]
    def __init__(self) :
        self.num=ressource.num
        self.status="libre"
        self.score = nu.random.choice(30,1)
        #self.level=self.getLevelRessources()
        self.name="agent n° %d "%self.num+"has"
        ressource.num+=1

    def generateRessources(self,numberOfRessources) :
        print("ressource generated")
        i=0
        while i<=numberOfRessources:
            ressource.listRessources.append(ressource())
            i+=1
        print(ressource.listRessources)
        pass



    def fixTask(self,k) :
        print('********************Traitement*************************************************')
        print('la ressource n° %d '%self.num+' est entrain de fixer la tache n° %d'%k+'...')
        print("un instant l'operation est en cours de réalisation")
        start=time.time()
        time.sleep(tsk.task.listTasks[k-1].getExecutionTime())  # Do some work
        end=time.time()
        tsk.task.listTasks[k-1].setFixedActive()
        print("finish")
        print("expected : %d"%(end-start))
        print(tsk.task.listTasks[k-1])






    def __repr__(self):
        self.name="agent n° %d "%self.num+" Score: %d"%self.score
        return self.name
