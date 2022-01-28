from time import time
def compute_average(n):
    """Perform n appends to an empty list and return average time elaspsed"""
    data = []
    start = time()      # record the start time (in seconds)
    for k in range(n):
        data.append(None)
    end = time()
    return (end - start)/n * 1000000

if __name__ == '__main__':
    for i in range (2, 9):
        print("n: 10^ %d" %i, "time (microsecond): %.3f" % compute_average(10**i))