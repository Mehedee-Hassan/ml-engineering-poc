from joblib import Parallel, delayed

def compute_square(number):
    # square
    return number ** 2

results = Parallel(n_jobs=4)(delayed(compute_square)(i) for i in range(10))

print(results)
