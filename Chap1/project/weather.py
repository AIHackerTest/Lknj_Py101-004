# coding:utf-8
# 创建字典，把txt文件的内容添加到字典
def load_dict_from_file(filepath):
    dict = {}
    try:
        with open(filepath,'r') as dict_file:
            for line in dict_file:
                (key,value) = line.strip().split(',') 
                dict[key] = value

    except IOError as ioerr:
        print("文件%s不存在" % (filepath))

    return dict


# 输入城市名，查询当地天气情况（返回值）,输入指令，返回相应结果
def query():
    histories = ''
    while True:
        city = input("请输入你想查询的城市名： ")
        d = load_dict_from_file('weather_info.txt')
        if city in d.keys():
            weather = d[city]
            history = '%s : %s\n' % (city, weather) 
            histories = histories + history
            print("%s的天气情况为： %s" % (city,weather))
        # 这是help
        if city == 'help':
            print("    - 输入城市名，查看相应天气情况")
            print("    - 输入help，查看功能")
            print("    - 输入exit，退出程序")
            print("    - 输入history，查看查询历史")
        # 这是退出程序
        elif city == 'exit':
            return exit(0)
        # 这是历史记录
        elif city == 'history':
            print(histories)

query()



