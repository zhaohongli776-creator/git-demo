print("请选择您的操作内容\n1.添加收入\n2.添加支出\n3.查看所有记录\n4.按类别统计\n5.查看收支汇总\n6.删除记录\n7.退出程序")
id = int(input('请选择操作：'))
if id == 1:
    amount = input("请输入金额：")
    type = input("请输入类型：")
    note = input("请输入备注；")
    category = input("请输入职位：")
    date = input("请输入日期：")
    print = ("记录添加成功：")
    def recode_income():
        recode = {
            "id": id,
            "amount": amount,
            "type": type,
            "note": note,
            "category": category,
            "date": date,
    }
elif id ==2:
    amount = input("请输入金额：")
    type = input("请输入类别：")
    note = input("请输入备注：")
    date = ("请输入日期：")
    print("记录添加成功！")
    def recode_outcome():
        recode = {
        "id": id,
        "amount": amount,
        "type": type,
        "note": note,
        "date": date,
    }

