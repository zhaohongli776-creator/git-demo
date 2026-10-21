import finance
print("请选择您的操作内容\n1.添加收入\n2.添加支出\n3.查看所有记录\n4.按类别统计\n5.查看收支汇总\n6.删除记录\n7.退出程序")
id = int(input('请选择操作：'))
if id == 1:
    amount = input("请输入金额：")
    type = input("请输入类型：")
    note = input("请输入备注；")
    category = input("请输入职位：")
    date = input("请输入日期：")
    print("记录添加成功！")
elif id ==2:
    amount = input("请输入金额：")
    type = input("请输入类别：")
    note = input("请输入备注：")
    date = input("请输入日期：")
    print("记录添加成功！")
elif id == 3:
    print("查看所有记录")
    print("id\t金额\t类型\t备注\t类别\t日期")
elif id == 4:
    print("按类别统计")
    print("类别\t总金额")
elif id == 5:
    print("查看收支汇总")
    print("总收入\t总支出")
elif id == 6:
    print("删除记录")
    record_id = int(input("请输入要删除的记录id："))
    print("记录删除成功！")
elif id == 7:
    print("退出程序")
