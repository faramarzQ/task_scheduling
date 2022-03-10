# Task scheduler
A multitask scheduler program which scedules different number of tasks with differnet instructions number, to various machines also having different MIPS. The goal is to find best solution to bind tasks to machines.

## Details
###### overview
Problem is solved using OOP containing a Task and Machine class visualized in two ways, showing graph dependency and a broken bar visualizer indicating each machine and the tasks it solved and their time to be finished.

###### input file
The details are injected into the core.py file from a txt file. the first line of file, x which is the number of the tasks,
the x next lines is a dependency matris indicating the dependency between tasks separated with a spaces, next x+2 line indicates the number of machines and
line x+3 shows each machine's power separated with spaces. a sample format is available in input.txt file.

