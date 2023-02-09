#!/usr/bin/env python
# -*- coding: utf-8 -*-
#hibatallah kabbaj
import tasks as tsk
import resources as rs
import GA as genetic
import multiprocessing
from multiprocessing import Pool
import time
from progressive.bar import Bar
import time

if __name__=='__main__':

#generation des tasks
    task1 = tsk.task()
    res1=rs.ressource()
    task1.generateTasks(7)
    res1.generateRessources(7)
#les ressources disponibles

    res2=rs.ressource()
    res3=rs.ressource()
    res4=rs.ressource()


    genetic.ga()


    #res1.generateRessources(6)

    print(tsk.task.listTasks)
    print("calculate schedulling")
    bar = Bar(max_value=100)
    bar.cursor.clear_lines(5)  # Make some room
    bar.cursor.save()  # Mark starting line
    for i in range(101):
        time.sleep(0.25)  # Do some work
        bar.cursor.restore()  # Return cursor to start
        bar.draw(value=i)  # Draw the bar!
    start=time.time()
    pool=multiprocessing.Process(target=rs.ressource.listRessources[genetic.Agent.schedull[-7]].fixTask,args=(3,))
    pool1=multiprocessing.Process(target=rs.ressource.listRessources[genetic.Agent.schedull[-6]].fixTask,args=(2,))
    pool2=multiprocessing.Process(target=rs.ressource.listRessources[genetic.Agent.schedull[-5]].fixTask,args=(0,))
    pool3=multiprocessing.Process(target=rs.ressource.listRessources[genetic.Agent.schedull[-4]].fixTask,args=(1,))
    pool4=multiprocessing.Process(target=rs.ressource.listRessources[genetic.Agent.schedull[-3]].fixTask,args=(5,))
    pool5=multiprocessing.Process(target=rs.ressource.listRessources[genetic.Agent.schedull[-2]].fixTask,args=(7,))
    pool6=multiprocessing.Process(target=rs.ressource.listRessources[genetic.Agent.schedull[-1]].fixTask,args=(6,))

    pool.start()
    pool1.start()
    pool2.start()
    pool3.start()
    pool4.start()
    pool5.start()
    pool6.start()
    pool.join()
    pool1.join()
    pool2.join()
    pool3.join()
    pool4.join()
    pool5.join()
    pool5.join()
    pool5.join()

    end=time.time()
    print("time passed:%d"%(end-start))


    """


    start=time.time()
    res1.fixTask(3)
    res2.fixTask(1)
    res3.fixTask(6)
    end=time.time()
    print("time passed : %d" %(end-start))
"""






    #holistic based ressource planning
