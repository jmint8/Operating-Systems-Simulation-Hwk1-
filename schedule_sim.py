## OS Simulation Homework 1
import sys

# has to take something as input (jobs)

class job:
    def __init__(self, id, arrival, timeNeeded):
        self.id = int(id)
        self.arrival = int(arrival)
        self.timeNeeded = int(timeNeeded)
        self.timeLeft = int(self.timeNeeded) 
        # timeLeft only really needed for srtf and rr

def read_data(filename): 
    jobs = []
    #this should iniitialize the list of jobs taken from the data file. 
    in_f = open(filename, "r")
    for line in in_f:
        id = int(line.split()[0])
        arrival = int(line.split()[1])
        timeNeeded = int(line.split()[2])
        #print(id, arrival, timeNeeded) # this works tho, the print code found below doesnt tho. 
        jobs.append(job(id, arrival, timeNeeded))
    
        #and now we have a list of jobs that we can use for the rest of the simulation yay

    #for job in jobs:
        #print(job.id, job.arrival, job.timeNeeded)
        # im not sure whty but if this is on the readfile def it doesnt compile and doesnt print. but it does in main idk
    in_f.close()

    return jobs

def fcfs(jobs):
    current_time = 0
    context_switches = 0
    total_turnaround = 0

    #simulate the first come first serve scheduling algorithm here.
    #calculate turnaround time
 
    for job in jobs:
        if job.arrival > current_time:
            current_time = job.arrival    
        current_time += job.timeNeeded
        total_turnaround += current_time - job.arrival
        context_switches += 1
        
    print("FCFS Number of Context Switches:", context_switches)
    print("FCFS Average Turnaround Time:", total_turnaround / len(jobs))
    print("\n")
    return None

def sjf(jobs):
    current_time = 0
    context_switches = 0
    total_turnaround = 0
    #have a list of jobs that have arrived but not yet completed, and sort it by time needed.



    print("SJF")
    print("\n")
    return None

def srtf(jobs):
    current_time = 0
    context_switches = 0
    total_turnaround = 0
    #shortest remaining time first


    print("SRTF")
    print("\n")
    return None

def rr(jobs):
    current_time = 0
    context_switches = 0
    total_turnaround = 0
    #round robin 


    print("RR")
    print("\n")
    return None

def main():
    jobs = read_data("data.txt")

    # for job in jobs:
    #     print(job.id, job.arrival, job.timeNeeded)
    
    fcfs(jobs)

    sjf(jobs)

    srtf(jobs)

    rr(jobs)

if __name__ == "__main__":    
    main()