#!/usr/bin/python3
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import showTimeline
import showGraph

class Machine:
    def __init__(self, power):
        self.power = power
        self.done_tasks = []

    def doTask(self, task_index):
        task = Main.tasks[task_index]
        if(self.done_tasks):
            last_task_of_machine = self.done_tasks[-1]
        else:
            last_task_of_machine = None
        start_time_of_task = task.calculateStartTime(last_task_of_machine) # last task done by machine

        task.setStartTime(start_time_of_task)
        time_to_finish_task = int(task.instructions) / int(self.power)
        task.setFinishTime(start_time_of_task + time_to_finish_task)

        self.done_tasks.append(task_index)
        Main.done_tasks.append(task_index)
        task.removeDependency()

class Task:
    index = 0
    def __init__(self, instructions):
        self.instructions = instructions
        self.dependents = []
        self.const_dependents = []

    def setDependent(self, dependents):
        self.dependents.append(dependents) #changable items
        self.const_dependents.append(dependents) #unchagable items

    #as the task is done, remove the tasks which are dependent on it
    def removeDependency(self):
        for task in Main.tasks:
            if self.index in task.dependents:
                temp_index = task.dependents.index(self.index)
                del task.dependents[temp_index]

    def setStartTime(self, time):
        self.from_ = time

    def setFinishTime(self, time):
        self.to_ = time

    def setMachine(machine):
        self.machine = machine

    def calculateStartTime(self, last_task_of_machine):
        biggest_finish_time = 0
        for dependent in self.const_dependents:
            if(hasattr(Main.tasks[dependent], 'to_')):
                if(Main.tasks[dependent].to_ > biggest_finish_time ):
                    biggest_finish_time = Main.tasks[dependent].to_

        if(last_task_of_machine != None):
            if(Main.tasks[last_task_of_machine].to_ > biggest_finish_time):
                biggest_finish_time = Main.tasks[last_task_of_machine].to_

        return biggest_finish_time

class Main:
    edges = []
    machines = []
    tasks = []
    done_tasks = []

    def minimalizeInput():
        raw_input = open("input.txt", "r").read().split('\n')
        part0 = int(raw_input[0].split()[0])

        graph_matris = []
        for i in range(1, part0+1):
            graph_matris.append(raw_input[i].split())

        row_index = 0
        for row in graph_matris:
            row_index += 1
            col_index = 0
            for col in row:
                col_index += 1
                if(col == '1'):
                    Main.edges.append([row_index-1, col_index-1])
        
        tasks_row = raw_input[part0+1].split()
        i = 0
        for task in tasks_row:
            obj = Task(task)
            obj.index = i
            Main.tasks.append(obj)
            i += 1

        machines_row = raw_input[part0+3].split()
        unsorted_machines = []
        for machine in machines_row:
            unsorted_machines.append(machine)
        unsorted_machines.sort(reverse=True)
        for machine in unsorted_machines:
            obj = Machine(machine)
            Main.machines.append(obj)

    def findDependencyBetweenTasks():
        for edge in Main.edges:
            Main.tasks[edge[1]].setDependent(edge[0])

    def invokeMachines():
        independent_tasks = []
        for task in Main.tasks:
            if( (not task.dependents) and (not hasattr(task, 'to_')) ):
                independent_tasks.append(task.index)

        loop_number = math.ceil( len(independent_tasks) / len(Main.machines) )
        for i in range(0, loop_number):
            for machine in Main.machines:
                if(independent_tasks):
                    machine.doTask(independent_tasks[0])
                    del independent_tasks[0]

    def start():
        Main.minimalizeInput()
        Main.findDependencyBetweenTasks()
        showGraph.show(Main.tasks, Main.edges)
        
        while(len(Main.done_tasks) != len(Main.tasks)):
            Main.invokeMachines()

        for machine in Main.machines:
            print(machine.done_tasks)

        showTimeline.show(Main.machines, Main.tasks)

Main.start()
