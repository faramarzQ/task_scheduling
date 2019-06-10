# Multitask-scheduling
a multitask scheduler program with task dependency.tasks are being solved using multimachines which each task has an instruction number in Million-Instructions unit and each machine has a power number in Milllion-instruction-per-seconds unit.
## details
###### overview
problem is solved using OOP containing a Task and Machine class.
the program start point is the start() method in Main class, being called at the EOF.
the problem is visualized in two ways, showing graph dependency and a broken bar visualizer indicating each machine and the tasks it solved and
their time to be finished.
###### input file
the details are injected into the core.py file from a txt file. the first line of file, x which is the number of the tasks,
the x next lines is a dependency matris indicating the dependency between tasks separated with a spaces, next x+2 line indicates the number of machines and
line x+3 shows each machine's power separated with spaces. a sample format is available in input.txt file.

