# coding:utf-8

import requests

# 用requests的get函数获取API数据，返回字典
# API数据来源，心知天气
def fetchWeather(location):
    result = requests.get('https://api.seniverse.com/v3/weather/now.json',params = {
        'key': 'ra1uyjh2z3esaoj9',
        'location': location,
        'language': 'zh-Hans',
        'unit': 'c'
    }, timeout = 1)
    return result.json()

# 根据字典参数打印返回的数据
def show_weather(weather_dic):
    name = weather_dic['results'][0]['location']['name']
    text = weather_dic['results'][0]['now']['text']
    temp = weather_dic['results'][0]['now']['temperature']
    last_update = weather_dic['results'][0]['last_update'][:-6].replace('T', ' ')
    weather = f"""{name} 的天气为 {text}, 温度为 {temp} 摄氏度.
        \n更新时间: {last_update}\n"""
    return weather

# 开始
def play():
    history_list = []
    while True:
        try:
            user_city = input("请输入您要查询的城市： ")
            result = fetchWeather(user_city)
            user_weather = show_weather(result)
            print(user_weather)
            history_list.append(user_weather)

        except:
            if user_city in ['h','H','help','Help']:
                print('''
                    输入正确的城市名，查询该城市的天气
                    输入h,H,help,Help其中的一个，查询帮助文档
                    输入history，获取查询历史
                    输入exit，或者quit，退出天气查询系统
                    ''')
            elif user_city == 'history':
                for history in history_list:
                    print(history)
            elif user_city in ['exit','quit']:
                print('已退出！')
                exit()
            else:
                print("滴滴滴~请确认您输入的城市是否存在！输入help查看帮助")
