import os
import random

class ExamSys:
    def __init__(self):
        self.students = []
        self.load_students()

    def load_students(self):
        """读取学生名单，自动跳过空行和格式错误行"""
        filename = "人工智能编程语言学生名单.txt"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    # 跳过空行
                    if not line:
                        continue
                    parts = line.split(",")
                    # 必须是 学号,姓名 两部分
                    if len(parts) == 2:
                        sid, name = parts
                        self.students.append({
                            "sid": sid.strip(),
                            "name": name.strip()
                        })
                    else:
                        print(f"⚠️ 跳过格式错误行：{line}")
            print(f"✅ 成功读取 {len(self.students)} 名学生")
        except FileNotFoundError:
            print(f"❌ 找不到文件：{filename}，请把名单放在同一目录下！")

    def find_student(self):
        """按学号查询学生"""
        sid = input("请输入要查询的学号：").strip()
        for stu in self.students:
            if stu["sid"] == sid:
                print(f"✅ 找到：姓名 {stu['name']}，学号 {stu['sid']}")
                return
        print("❌ 未找到该学号学生")

    def random_roll_call(self):
        """随机点名 n 人"""
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
                print(f"{i}. {stu['name']}（{stu['sid']}）")
        except ValueError:
            print("❌ 请输入数字")

    def generate_exam_arrangement(self):
        """生成考场安排表（打乱顺序）"""
        if not self.students:
            print("❌ 暂无学生数据")
            return
        shuffled = self.students.copy()
        random.shuffle(shuffled)
        with open("考场安排表.txt", "w", encoding="utf-8") as f:
            for i, stu in enumerate(shuffled, 1):
                f.write(f"{i:02d},{stu['name']},{stu['sid']}\n")
        print("✅ 考场安排表.txt 已生成")

    def generate_admission_tickets(self):
        """每人生成一个准考证文件，座位号随机"""
        if not self.students:
            print("❌ 暂无学生数据")
            return
        os.makedirs("准考证", exist_ok=True)
        shuffled = self.students.copy()
        random.shuffle(shuffled)
        for i, stu in enumerate(shuffled, 1):
            ticket_path = os.path.join("准考证", f"{i:02d}_{stu['name']}.txt")
            with open(ticket_path, "w", encoding="utf-8") as f:
                f.write(f"座位号：{i:02d}\n")
                f.write(f"姓名：{stu['name']}\n")
                f.write(f"学号：{stu['sid']}\n")
        print("✅ 准考证文件夹已生成")

    def run(self):
        """主菜单循环"""
        while True:
            print("\n" + "="*12 + "学生信息与考场管理系统" + "="*12)
            print("1. 查询学生信息")
            print("2. 随机点名")
            print("3. 生成考场安排表")
            print("4. 生成准考证文件")
            print("-"*50)
            print("0. 退出系统")

            choice = input("请输入功能编号：").strip()
            if not choice.isdigit():
                print("❌ 请输入数字编号（0~4）")
                continue
            choice = int(choice)

            if choice == 0:
                print("👋 退出系统，感谢使用！")
                break
            elif choice == 1:
                self.find_student()
            elif choice == 2:
                self.random_roll_call()
            elif choice == 3:
                self.generate_exam_arrangement()
            elif choice == 4:
                self.generate_admission_tickets()
            else:
                print("❌ 功能编号不存在，请输入 0~4")


if __name__ == "__main__":
    app = ExamSys()
    app.run()1
