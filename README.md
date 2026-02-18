Objective: 

There are several purposes of this homework assignment:

Give you practice creating a simulation.
Make you start to understand the power of simulation as a tool for scientists and engineers.  
As a computer scientist, you are part scientist and part engineer, but you should also begin to appreciate how helpful simulation can be for pure scientists or pure engineers, too.
Give you practice analyzing the results of the simulation, drawing conclusions, and thinking about how your simulation (which is really a scientific experiment) can be improved.  
This will exercise your critical thinking and problem solving skills.
Give you practice communicating what you have found and your ideas to others.
You’ll also get intimately familiar with some of the scheduling algorithms used in operating systems.

Task:

You will write a program (you may use Python, Java, C, or C++) to simulate scheduling the CPU of a batch system. 
In these systems, users submit their jobs and go about their business, rather than sitting around, waiting for the output.  
Although your parents may remember them from the bad old days and people may think they are gone, that’s far from the truth.  
In fact, supercomputers use a batch scheduling model.  Your program must compile and run on the computers in Olin 211 to receive credit.  
Your program will read in a data file called data.txt from the relative path “.” which means don’t open the file “/home/david.toth/data.txt” and instead open “data.txt”.  
Failure to follow this instruction will result in a 5 point deduction.  Your program will read in a data file containing three integers per line, each separated by a space.  
The first integer on a line is the job number, which will be zero for the first line, one for the second line, and so on.  This corresponds to a job number and will make your life a little easier.  
The second integer on a line tells you the time the job was submitted.  There is no unit, but if it helps you, think of it as seconds since the computer was turned on.  The third integer on a line tells you how long the job will take to complete. 
Again, there is no unit, but if you think of it as the same unit as the second integer on the line, it will be easy to figure out.  Your simulator will run the following CPU scheduling algorithms:

FCFS (first come first served)
SJF (shortest job first)
SRTN (shortest run time next)
RR (round robin) with a quantum of 1 unit of time.

Calculate the average turnaround time for the jobs with each algorithm and print that out.  Make sure your output is obvious (like FCFS: 56 rather than 56) so I don’t have to guess which algorithm resulted in which average turnaround time.  Your output should be for each algorithm – I only listed one in the previous sentence for brevity.  Also print out the number of context switches (assume that for round robin, a context switch occurs every quantum even if there’s still only one process running).  Assume that beginning the first job DOES count as a context switch and finishing the last job does NOT count as a context switch.  Make sure to test your program to make sure it works.

Once you have finished constructing your simulator, create a pdf document (think of this as a lab report!) containing your name, how to compile your program (if it’s written in Java, C, or C++), and how to run your program.  The file should also contain a summary of what you did, the results you got from running the simulation and an analysis of the results.  The analysis should contain which algorithm you think should be used and why.  You should make your argument persuasive, as you may need to explain to users of your computer why their jobs are scheduled in the way you propose, rather than the way they want it done.  It should also address the relevance of the context switches (hint: there’s obviously something to talk about here).  Finally, your file should contain a list of any shortcomings of the method we used here to determine which algorithm we should use.  For any shortcoming listed, you should explain what the issue is, why it’s an issue, and how the issue should be addressed to improve the results.
