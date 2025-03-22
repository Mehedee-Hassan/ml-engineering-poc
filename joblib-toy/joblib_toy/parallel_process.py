from joblib import Parallel, delayed



def compute_square(number):
    # square
    return number ** 2

def get_number_of_cores():
    import os
    available_cores = os.cpu_count()

    print(available_cores)
    return available_cores

def run ():
    cores = get_number_of_cores()
    # 1. faster
    results = Parallel(n_jobs=cores)(delayed(compute_square)(i) for i in range(10))

    # 2. slower than 1
    # results = Parallel(n_jobs=100)(delayed(compute_square)(i) for i in range(10))

    # slower than 2
    # results = Parallel(n_jobs=400)(delayed(compute_square)(i) for i in range(10))
    print(results)

    # using 4 core parallely


    """
    Context Switching: When you run more processes or threads than the number of available CPU cores,
      the operating system has to perform context switching. Context switching happens when the OS switches between processes,
        saving the state of one and loading the state of another.

    High n_jobs Relative to Available Cores: If you have 100 or 400 parallel tasks but only a few CPU cores, 
    context switching can consume significant time and resources. For example, your CPU might be idle while the OS is switching between tasks, 
    which leads to less overall progress.


    """