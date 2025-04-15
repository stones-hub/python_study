import logging
import threading
from queue import Queue
from threading import Lock
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# 服务器进程数量
SF_PROCESS_NUM = 20


class Funnel:
    # capacity: 管道容量, interval: 定时器间隔, handler: 处理函数
    def __init__(self, capacity, interval, handler):
        # 管道 容量
        self.capacity = capacity
        # 定时器间隔
        self.interval = interval
        # 处理函数
        self.handler = handler
        # 线程池
        self.workers = []
        # 数据队列
        self.data_queue = Queue(maxsize=capacity)
        # 线程关闭
        self.close_event = threading.Event()

        # 全局锁
        self.lock = Lock()
        # 记录线程处理的数据条
        self.record_count = 0

        self.closed = False

        self.ticker_close_event = threading.Event()

    # 启动线程池, 每个线程执行worker函数
    def start_workers(self):
        for i in range(SF_PROCESS_NUM):
            # 将每个线程加入到线程池中
            worker = threading.Thread(target=self.worker)
            worker.start()
            self.workers.append(worker)
            thread_id = threading.get_ident()
            logging.info(f"启动线程{thread_id}成功.")
            
    # 每个线程需要做的事情
    def worker(self):
        while not self.close_event.is_set() and not self.data_queue.empty():
            try :
                # 从队列中获取数据
                date = self.data_queue.get(timeout=1)
                # 处理数据
                self.do(date)
                # 处理完成
                self.data_queue.task_done()
            except Exception as e:
                logging.error(f"线程{threading.get_ident()}发生异常: {e}")
                continue

    def do(self, data):
        if self.handler is None:
            logging.error(f"处理函数为空, 无法处理数据: {data}")
            return 
        self.handler(data)
        with self.lock: # with 自动加锁和解锁
            self.record_count += 1

    # 启动定时器
    def start_timer(self, interval):
        def timer():
            while not self.close_event.is_set():
                time.sleep(interval)
                logging.info(f"已处理数据条数: {self.record_count}")
                    
        timer_thread = threading.Thread(target=timer)
        timer_thread.start()



    def close(self):
        if self.closed:
            logging.info("Funnel 已关闭, 无需重复关闭.")
            return 
        self.closed = True
        self.close_event.set()

        # 处理队列
        for _ in range(SF_PROCESS_NUM):
            self.data_queue.put(None)

        # 等待所有线程处理完成
        for worker in self.workers:
            worker.join()

        # 关闭定时器
        self.ticker_close_event.set()
        time.sleep(1)
        logging.info("Funnel 已关闭.")

            

