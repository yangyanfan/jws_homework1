import os
import random
from student import Student

class ExamSystem:
    def __init__(self):
        self.students = []
        self.load_students()

    def load_students(self):
        filename = "人工智能编程语言学生名单.txt"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(",")
                    if len(parts) == 2:
                        sid, name = parts
                        self.students.append(Student(sid, name))
                    else:
                        print(f"⚠️ 跳过格式错误行：{line}")
            print(f"✅ 成功读取 {len(self.students)} 名学生")
        except FileNotFoundError:
            print(f"❌ 找不到文件：{filename}")

    def find_student(self):
        sid = input("请输入要查询的学号：").strip()
        for stu in self.students:
            if stu.sid == sid:
                print(f"✅ 找到：姓名 {stu.name}，学号 {stu.sid}")
                return
        print("❌ 未找到该学号学生")

    def random_roll_call(self):
        if not self.students:
            print("❌ 暂无学生数据")
            return
        try:
            n = int(input("请输入点名人数："))
            if n <= 0 or n > len(self.students):
                print(f"❌ 人数必须在 1~{len(self.students)} 之间")
                return
            selected = random.sample(self.students, n)
            print("\n🎲 随机点名结果：")
            for i, stu in enumerate(selected, 1):
                print(f"{i}. {stu.name}（{stu.sid}）")
        except ValueError:
            print("❌ 请输入数字")

    def generate_exam_arrangement(self):
        if not self.students:
            print("❌ 暂无学生数据")
            return
        shuffled = self.students.copy()
        random.shuffle(shuffled)
        with open("考场安排表.txt", "w", encoding="utf-8") as f:
            for i, stu in enumerate(shuffled, 1):
                f.write(f"{i:02d},{stu.name},{stu.sid}\n")
        print("✅ 考场安排表.txt 已生成")

    def generate_admission_tickets(self):
        if not self.students:
            print("❌ 暂无学生数据")
            return
        os.makedirs("准考证", exist_ok=True)
        shuffled = self.students.copy()
        random.shuffle(shuffled)
        for i, stu in enumerate(shuffled, 1):
            ticket_path = os.path.join("准考证", f"{i:02d}_{stu.name}.txt")
            with open(ticket_path, "w", encoding="utf-8") as f:
                f.write(f"座位号：{i:02d}\n")
                f.write(f"姓名：{stu.name}\n")
                f.write(f"学号：{stu.sid}\n")
        print("✅ 准考证文件夹已生成")