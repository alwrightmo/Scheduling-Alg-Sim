from job import Job

class CPU:
    def __init__(self, name : str, cycle : float) -> None:
        self.name = name
        self.cycle = cycle

        self.current_job = None
        self.jobs_completed = 0
        self.t_idle = 0
        self.graph : list[str] = []
    
    def execute(self) -> bool:
        '''Executes the job on the cpu and returns if the job has completed'''
        if self.current_job != None:
            # Add the current job to the cpu graph
            self.graph.append(self.current_job.name)
            # Add the time to job time executed
            self.current_job.t_executed += self.cycle
            # If job is finished, let the algorithm know
            if self.current_job.t_executed >= self.current_job.t_execution:
                return True
        else:
            # Add idle state to cpu graph
            self.graph.append("i")
            # Increase idle time
            self.t_idle += self.cycle
        return False

    def work_on(self, j : Job) -> None:
        self.current_job = j

    def job_completed(self) -> None:
        self.jobs_completed += 1
        self.current_job = None

    def reset(self) -> None:
        self.current_job = None
        self.jobs_completed = 0
        self.t_idle = 0
        self.graph = []