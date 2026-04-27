import datetime


# 搭建主循环和菜单
def main():
    while True:
        print("\n===== 个人日记本 =====")
        print("1. 写日记")
        print("2. 查看日记")
        print("3. 退出")
        print("4. 搜索关键字")
        print("5. 统计篇数")
        choice = input("请输入选项：")
        if choice == "1":
            write_diary()
        elif choice == "2":
            view_diary()
        elif choice == "3":
            print("退出程序")
            break
        elif choice == "4":
            k = input("请输入关键词：")
            search_diary(k)
        elif choice == "5":
            count_entries()
        else:
            print("输入无效，请重试。")


# 实现写日记功能
def write_diary():
    content = input("请输入今天的日记内容：")
    timestamp = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    try:
        with open("diary.txt", "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}]\n{content}\n---\n")

        print("日记已保存！")

    except Exception as e:
        print(f"保存失败：{e}")


# 实现查看日记功能
def view_diary():
    try:
        with open("diary.txt", "r", encoding="utf-8") as f:
            content = f.read()
            if content:
                print("\n===== 日记列表 =====")
                print(content)
            else:
                print("日记本还是空的。")

    except FileNotFoundError:
        print("记事本还是空的。")


# 搜索功能
def search_diary(keyword):
    try:
        with open("diary.txt", "r", encoding="utf-8") as f:
            entries = f.read().split("---")
            matches = [e for e in entries if keyword in e]
            if matches:
                for m in matches:
                    print(m.strip())
            else:
                print("没有找到包含该关键词的日记。")

    except FileNotFoundError:
        print("日记本还是空的。")


# 统计篇数
def count_entries():
    try:
        with open("diary.txt", "r", encoding="utf-8") as f:
            count = f.read().count("---")

        print(f"共有 {count} 篇日记。")

    except FileNotFoundError:
        print("共有 0 篇日记。")


if __name__ == "__main__":
    main()
