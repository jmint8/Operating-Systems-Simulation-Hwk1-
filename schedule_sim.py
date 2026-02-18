## OS Simulation Homework 1
import sys

# has to take something as input (jobs)

class job:
    def __init__(self, id, arrival, timeNeeded):
        self.id = id
        self.arrival = arrival
        self.timeNeeded = timeNeeded
        self.timeLeft = timeNeeded

def read_data(filename): 
    jobs = []
    #this should iniitialize the list of jobs taken from the data file. 

    # some stuff happens here 

    return jobs


def reset_sim(jobs):
    for job in jobs:
        job.timeLeft = job.timeNeeded

def fcfs(jobs):
    return 0

def sjf(jobs):
    return 0

def srtf(jobs):
    return 0

def rr(jobs):
    return 0


def main():
    jobs = read_data("data.txt")

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