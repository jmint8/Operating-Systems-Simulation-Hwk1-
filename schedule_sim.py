## OS Simulation Homework 1

# has to take something as input (jobs)
class job:
    def __init__(self, id, arrival, timeNeeded):
        self.id = int(id)
        self.arrival = int(arrival)
        self.timeNeeded = int(timeNeeded)
        self.timeLeft = int(self.timeNeeded)  # timeLeft only really needed for srtf and rr
        # this is going to make these simulations so much easier to do

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
    #intialize current time, context switches, and total turnaround time
    current_time = 0
    context_switches = 0
    total_turnaround = 0
 
    #jobs is already sorted for first come first serve. 
    for job in jobs:
        if job.arrival > current_time:
            #edge case where the next job arrives after the current time
            current_time = job.arrival    
        current_time += job.timeNeeded
        total_turnaround += current_time - job.arrival
        context_switches += 1

    print("FCFS Number of Context Switches:", context_switches)
    print("FCFS Average Turnaround Time:", total_turnaround / len(jobs))
    print("\n")
    return None

def sjf(jobs):
    #shortest job first.
    current_time = 0
    context_switches = 0
    total_turnaround = 0
    available_jobs = []
    completed_jobs = []
    jobs_not_arrived = jobs.copy() # will help keep track of jobs not arrived without having to change the og jobs list. 
    while len(completed_jobs) < len(jobs):
        for job in jobs_not_arrived:
            if job.arrival <= current_time and job not in available_jobs and job not in completed_jobs:
                available_jobs.append(job) 
                jobs_not_arrived.remove(job) # this will prevent the for loop from looping the whole list everty time. lower time complexity.
                #print(job.id, job.arrival, job.timeNeeded) #testing thingy

        if len(available_jobs) > 0:
            available_jobs.sort(key=lambda x: x.timeNeeded) # sort by time needed
            curr_job = available_jobs.pop(0) # get the job with the shortest time needed bc we sort it every time. 
            current_time += curr_job.timeNeeded   
            total_turnaround +=current_time-curr_job.arrival 
            context_switches += 1 
            #print(curr_job.id, curr_job.arrival, curr_job.timeNeeded) # testing thingy
            completed_jobs.append(curr_job)
            curr_job = None # its like setting our pointers to null. 

        elif (len(available_jobs)) ==0:
            current_time += 1 # if there are no available jobs, just move to the next time unit

    print("SJF Number of Context Switches:", context_switches)
    print("SJF Average Turnaround Time:", total_turnaround / len(jobs))
    print("\n")
    return None

def srtn(jobs):
    current_time = 0
    context_switches = 0
    total_turnaround = 0
    #shortest remaining time next






    print("SRTN Number of Context Switches:", context_switches)
    print("SRTN Average Turnaround Time:", total_turnaround / len(jobs))
    print("\n")
    return None

def rr(jobs):
    current_time = 0
    context_switches = 0
    total_turnaround = 0
    #round robin 


    print("RR Number of Context Switches:", context_switches)
    print("RR Average Turnaround Time:", total_turnaround / len(jobs))
    print("\n")
    return None

def main():
    #jobs = read_data("data.txt")
    jobs = read_data("data2.txt") # for testing purposes. 

    # for job in jobs:
    #  print(job.id, job.arrival, job.timeNeeded)
    
    #fcfs(jobs) #| works |

    #sjf(jobs) #| works |

    srtn(jobs) #| TODO |

    #rr(jobs) #| TODO |

if __name__ == "__main__":    
    main()