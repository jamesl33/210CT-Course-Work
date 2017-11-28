# 210CT-Course-Work
Advanced 210CT Course Work tasks

[Running the Code]
In each of the task folders there will be a 'main.py' this is the file which contains either a very simple example
of the code running or the examples from the coursework PDF. So to show that the task is completed correctly in
most cases simply run 'main.py'. Accompanying each tasks 'main.py' will be a 'unit_test.py' file which contains
the unit testing for each task. In some cases there may be several but they will be clearly labeled.

In the case of task6 there there isn't much of an example in the 'main.py' file it is all integrated in the 'unit_test.py' file.
This was because task stood out against the others due to its complexity. Therefore showing this task working was much easier
if you were to simply run the 'unit_test.py' file as it contains each example from the coursework PDF and asserts that its correctly done.

    [Linux]
    Prerequisites: You must have Python 3.5.2 or above installed.
    Each of the files has the interpreter statement at the top '#!/usr/bin/python3' therefore you simply need to make sure that the
    file is executable 'chmod +x filename_here' and then run the file './filename_here'. The output will be clearly shown in the
    terminal and often pretty printed.

    [Windows]
    Prerequisites: You must have Python 3.5.2 or above installed.
    I myself do not run Windows so I have not completely catered for Windows users (Maybe it's needed though?). Running the file on Windows
    is also just as simple. You just need to double click on the 'main.py' or 'unit_test.py' and depending of what your default applications
    are it will run the Python code in the CMD. You may find that the CMD closes instantly after running the file which can be fixed by
    added 'input()' to the very end of the file which you have run and CMD will wait for you to close it. Alternatively you can run the
    file in IDLE and you will not need to alter the code.

I also did up to task5 in C++ as well however I deleted those tasks after before I did task6 so I could commit to using Python.
You can view and run these files as well if you would like to. You will need to got to this commit
'https://github.coventry.ac.uk/leej64/210CT-Course-Work/commit/60b157e87051cf8355a009365006220efde74018' and download the files
before I removed them.

    [Linux]
    Prerequisites: You must have a C++ Compiler such as GCC and GNUMake installed.
    To run the C++ implimentations of the tasks is very simple. All of the tasks have a 'makefile' included so you simply
    need to run 'make' in the task directory and the task will be compiled. After that simply run the generated executable
    './task_executable_here'.
    This is the same with the Unit Testing which uses 'Catch'. Simply change directory into the unit testing folder and run 'make'.
    After this run the executable again './unit_testing_here'

    [Windows]
    Install WSL if you haven't already and then follow the Linux steps.

[Veto]
If this is a thing which I doubt then I would Veto task6 because thats the one I'm the least confident about (Spaghetti Code!)
