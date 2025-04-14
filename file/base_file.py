# 1. 文件操作
print("文件操作示例：")
try:
    with open("test.txt", "w", encoding="utf-8") as file:
        file.write("这是一个测试文件内容。")
    with open("test.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("文件未找到，请检查文件路径。")
except Exception as e:
    print(f"发生错误: {e}")

# 2. 数据库连接（以 SQLite 为例）
import sqlite3
print("\n数据库连接示例：")
try:
    with sqlite3.connect("test.db") as conn:
        cursor = conn.cursor()
        # 创建表
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
        # 插入数据
        cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
        # 查询数据
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
except sqlite3.Error as e:
    print(f"数据库操作出错: {e}")

# 3. 线程锁
import threading
print("\n线程锁示例：")
shared_variable = 0
lock = threading.Lock()

def increment():
    global shared_variable
    with lock:
        for _ in range(100000):
            shared_variable += 1

threads = []
for _ in range(2):
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"共享变量的值: {shared_variable}")

# 4. 自定义上下文管理器
class MyContextManager:
    def __enter__(self):
        print("进入上下文管理器")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("退出上下文管理器")
        if exc_type is not None:
            print(f"发生异常: {exc_type}, {exc_value}")
        return True

print("\n自定义上下文管理器示例：")
with MyContextManager() as cm:
    print("在上下文管理器内部执行操作")
    