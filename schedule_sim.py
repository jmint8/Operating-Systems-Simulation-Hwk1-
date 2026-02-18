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
        print(id, arrival, timeNeeded)
        jobs.append(job(id, arrival, timeNeeded))
    
        #and now we have a list of jobs that we can use for the rest of the simulation yay

    #for job in jobs:
        #print(job.id, job.arrival, job.timeNeeded)
        # im not sure whty but if this is on the readfile def it doesnt compile and doesnt print. but it does in main idk
        in_f.close()
    return jobs

def reset_sim(jobs):
    for job in jobs:
        job.timeLeft = job.timeNeeded

def fcfs(jobs):

    print("FCFS")
    return 0

def sjf(jobs):

    print("SJF")
    return 0

def srtf(jobs):

    print("SRTF")  
    return 0

def rr(jobs):

    print("RR")
    return 0


def main():
    jobs = read_data("data.txt")

    # for job in jobs:
    #     print(job.id, job.arrival, job.timeNeeded)
    
    reset_sim(jobs)
    fcfs(jobs)
    reset_sim(jobs)
    sjf(jobs)
    reset_sim(jobs)
    srtf(jobs)
    reset_sim(jobs)
    rr(jobs)

if __name__ == "__main__":    
    main()