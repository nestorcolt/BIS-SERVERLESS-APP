from concurrent.futures import ThreadPoolExecutor, as_completed
from timeit import default_timer as timer
import multiprocessing


# task that is performed in parallel
def task():
    for itm in range(100000):
        itm * 2


# multi-threading function
def countHighFrequencyItem():
    all_tasks = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        for item_index in range(1000):
            all_tasks.append(executor.submit(task))

        # process completed tasks
        for future in as_completed(all_tasks):
            index = future.result()


def default_execution():
    all_tasks = []
    for item_index in range(1000):
        all_tasks.append(task)

    for itm in all_tasks:
        itm()


def multi_process():
    processes = []
    for item_index in range(1000):
        p = multiprocessing.Process(target=task)
        processes.append(p)

    for process in processes:
        process.start()
    for process in processes:
        process.join()


##############################################################################################
if __name__ == '__main__':
    start = timer()
    # default_execution()
    # multi_process()
    countHighFrequencyItem()
    end = timer()
    print(end - start)
