# 导入系统类
from exam_system import ExamSystem

# 主函数：菜单交互逻辑
def main():
    # 实例化系统对象，自动加载学生数据
    system = ExamSystem()
    # 循环展示菜单
    while True:
        # 打印标准菜单
        print("\n===== 学生信息与考场管理系统 =====")
        print("1. 查询学生信息")
        print("2. 随机点名")
        print("3. 生成考场安排表")
        print("4. 生成准考证文件")
        print("+--------------------------------------------------------------------------")
        print("0. 退出系统")
        choice = input("请输入功能编号：").strip()

        # 判断输入是否为数字
        if not choice.isdigit():
            print("功能编号不存在，请正确输入功能编号（0~4）：")
            continue
        choice = int(choice)

        # 根据编号调用对应功能
        if choice == 0:
            print("感谢使用，系统已退出。再见！")
            break
        elif choice == 1:
            system.find_student()
        elif choice == 2:
            system.random_roll_call()
        elif choice == 3:
            system.generate_exam_arrangement()
        elif choice == 4:
            system.generate_admission_tickets()
        else:
            # 编号不在0-4范围内，提示错误
            print("功能编号不存在，请正确输入功能编号（0~4）：")

# 程序入口
if __name__ == "__main__":
    main()