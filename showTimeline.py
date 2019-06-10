import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt

def show(machines, tasks):
    fig, ax = plt.subplots()

    temp = 10
    for machine in machines:
        first_param = []
        for task_index in machine.done_tasks:
            task = tasks[task_index]
            first_param.append( (task.from_, task.to_ - task.from_ - 0.1) )
        temp +=10
        second_param = (temp, 9)
        ax.broken_barh(first_param, second_param)

    ax.set_xlabel('tasks timeline (s)')
    ax.set_ylabel('processors')

    # ax.set_xticks([1, 2, 3])
    # ax.set_xticklabels([100, 200, 300])
    # ax.set_yticks([25, 35, 45])
    # ax.set_yticklabels(['p1', 'p2', 'p3'])
    
    #create array of space between processors
    temp_arr = []
    temp = 25
    for i in range(len(machines)):
        temp_arr.append(temp)
        temp += 10
    ax.set_yticks(temp_arr)

    #create array of processors
    temp = []
    for i in range(1, len(machines)+1, 1):
        temp.append('p' + str(i))
    ax.set_yticklabels(temp)

    #x size of frame
    temp = 5
    for i in range(0, len(machines)):
        temp += 20
    ax.set_ylim(5, temp)

    temp = 0
    for task in tasks:
        if(task.to_ > temp):
            temp = task.to_
    ax.set_xlim(0, temp)

    ax.grid(True)
    plt.show()