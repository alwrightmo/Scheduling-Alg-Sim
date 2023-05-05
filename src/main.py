from scheduler import Scheduler

try:
    from terminaltables import AsciiTable
except:
    print("Please install the terminaltables addon with `pip install terminaltables`")
    print("or whatever you use to install python modules")
    exit(1)

try:
    import matplotlib.pyplot as plt
except:
    print("Somehow you don't have matplotlib, please install with `pip install matplotlib`")
    print("or whatever you use to install python modules")
    exit(1)

def main():
    n_cpus = 3
    n_jobs = 20
    n_runs = 10

    scheduler = Scheduler(n_cpus)

    edf_misses = [0] * n_runs
    sjf_misses = [0] * n_runs
    lst_misses = [0] * n_runs
    fcfs_misses = [0] * n_runs
    for run in range(n_runs):
        print(f"Run {run + 1} \\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/")
        # Results saved in a graph for each algorithm
        edf_results : list[list[str]] = []
        sjf_results : list[list[str]] = []
        lst_results : list[list[str]] = []
        fcfs_results : list[list[str]] = []
        # Generate random jobs for every run
        scheduler.generate_semi_random_jobs(n_jobs=n_jobs)

        print(f"Jobs: {scheduler.jobs}")

        print("EDF")
        edf_misses[run] += scheduler.algorithm_edf()
        for i, cpu in enumerate(scheduler.cpus):
            edf_results.append([f"cpu-{i}"])
            edf_results[i].extend(cpu.graph)
        scheduler.reset_state() 

        print("SJF")
        sjf_misses[run] += scheduler.algorithm_sjf()
        for i, cpu in enumerate(scheduler.cpus):
            sjf_results.append([f"cpu-{i}"])
            sjf_results[i].extend(cpu.graph)
        scheduler.reset_state()

        print("LST")
        lst_misses[run] += scheduler.algorithm_lst()
        for i, cpu in enumerate(scheduler.cpus):
            lst_results.append([f"cpu-{i}"])
            lst_results[i].extend(cpu.graph)
        scheduler.reset_state()

        print("FCFS")
        fcfs_misses[run] += scheduler.algorithm_fcfs()
        for i, cpu in enumerate(scheduler.cpus):
            fcfs_results.append([f"cpu-{i}"])
            fcfs_results[i].extend(cpu.graph)
        scheduler.reset_state()

        print("\nvvv RESULTS vvv\n")

        print("EDF RESULTS")
        table = AsciiTable(edf_results)
        table.inner_row_border = True
        print(table.table)

        print("SJF RESULTS")
        table = AsciiTable(sjf_results)
        table.inner_row_border = True
        print(table.table)

        print("LST RESULTS")
        table = AsciiTable(lst_results)
        table.inner_row_border = True
        print(table.table)

        print("FCFS RESULTS")
        table = AsciiTable(fcfs_results)
        table.inner_row_border = True
        print(table.table)
    
    print("\nVVV MISSES VVV\n")

    print("AVG EDF MISSES")
    print(sum(edf_misses) / n_runs)

    print("AVG SJF MISSES")
    print(sum(sjf_misses) / n_runs)

    print("AVG LST MISSES")
    print(sum(lst_misses) / n_runs)

    print("AVG FCFS MISSES")
    print(sum(fcfs_misses) / n_runs)

    # Output misses to a graph
    runs = range(1, n_runs + 1)
    plt.plot(runs, edf_misses, label="EDF Misses")
    plt.plot(runs, sjf_misses, label="SJF Misses")
    plt.plot(runs, lst_misses, label="LST Misses")
    plt.plot(runs, fcfs_misses, label="FCFS Misses")
    plt.ylabel("Number of misses")
    plt.xlabel("Run")
    plt.xticks(runs)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
