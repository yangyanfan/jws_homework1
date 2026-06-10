

# 定义学生实体类，存储学号和姓名信息
class Student:
    # 构造方法：初始化学号、姓名
    def __init__(self, sid, name):
        # 去除字符串首尾空格，避免数据异常
        self.sid = sid.strip()
        self.name = name.strip()

    # 重写字符串方法，方便打印学生信息
    def __str__(self):
        return f"学号：{self.sid}，姓名：{self.name}"