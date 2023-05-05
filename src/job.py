class Job:
    def __init__(self, r : float, e : float, d : float, name : str) -> None:
        self.t_release = r
        self.t_execution = e
        self.t_deadline = d
        self.name = name

        self.t_executed = 0
        self.t_finish = -1

    def calculate_slack(self, current_time : float) -> float:
        return self.t_deadline - (self.t_execution - self.t_executed) + current_time
    
    def reset(self) -> None:
        self.t_executed = 0
        self.t_finish = -1

    def __repr__(self) -> str:
        return f"{self.name}: r={self.t_release} e={self.t_execution} d={self.t_deadline}"

    def __str__(self) -> str:
        return self.name