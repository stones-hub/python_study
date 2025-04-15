import time
import threading
import random
import multiprocessing
import os

# 线程任务
def thread_task(process_name, task_id):
    # print(f"进程{process_name}中线程{task_id}任务开始 !")
    thread_id = threading.get_ident()
    print(f"进程{process_name}中线程任务{task_id} id: {thread_id} 开始 !")
    for i in range(10):
        # print(f"进程{process_name}中线程{task_id}任务执行中 !")
        # 每个线程随机休眠1-3秒
        time.sleep(random.randint(1, 3))
    print(f"进程{process_name}中线程{task_id}任务结束 !")


# 进程任务, 每个进程中开N个线程
def process_task(process_name, thread_number):
    # print(f"进程{process_name}任务开始 !")
    process_id = os.getpid()
    print(f"进程{process_name} id: {process_id} 开始 !")

    parent_process_id = os.getppid()
    print(f"进程{process_name} 父进程id: {parent_process_id} !")
    threads = []
    for i in range(thread_number):
        thread = threading.Thread(target=thread_task, args=(process_name, i))
        threads.append(thread)
        thread.start()

    for thread in threads:  
        thread.join()
    print(f"进程{process_name}任务结束")
    


# 运行, 创建process_number个进程, 每个进程中创建thread_number个线程
def run(process_number, thread_number):

    processes = []
    # 创建进程
    for i in range(process_number):
        print(f"创建进程id: {i}")
        process_name = f"process_{i}"
        process = multiprocessing.Process(target=process_task, args=(process_name,thread_number))
        processes.append(process)
        process.start()


    # 等待所有进程结束
    for process in processes:
        process.join()



if __name__ == "__main__":
    run(3, 3)


