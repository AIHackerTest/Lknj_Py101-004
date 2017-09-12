# coding:utf-8

import requests

# 用requests的get函数获取API数据，返回字典
# API数据来源，心知天气
def fet_weather(location,unit):
    result = requests.get('https://api.seniverse.com/v3/weather/daily.json',params = {
        'key': 'ra1uyjh2z3esaoj9',
        'location': location,
        'language': 'zh-Hans',
        'unit': unit
        }, timeout = 20)
    return result.json()

# 根据字典参数打印返回的数据
def show_up_weather(weather_dict,day):
    date = weather_dict['results'][0]['daily'][day]['date']
    name = weather_dict['results'][0]['location']['name']
    text_day = weather_dict['results'][0]['daily'][day]['text_day']
    text_night = weather_dict['results'][0]['daily'][day]['text_night']
    high = weather_dict['results'][0]['daily'][day]['high']
    low = weather_dict['results'][0]['daily'][day]['low']
    wind_direction = weather_dict['results'][0]['daily'][day]['wind_direction']
    last_update = weather_dict['results'][0]['last_update'][:-6].replace('T', ' ')
    
    weather = f'''{date}: {name} 白天到夜里的天气为: {text_day}转{text_night},
温度：{low}~{high}, 风向：{wind_direction}\n更新时间： {last_update}'''
    return weather

# 开始
def play():
    history_list = []
    unit = 'c' # 默认为‘c’
    day = 0 #默认查询当天天气
    while True:
        try:
            user_city = input("请输入您想要查询的城市： ")
            result = fet_weather(user_city,unit)
            user_weather_new = show_up_weather(result,day)
            print(user_weather_new)
            history_list.append(user_weather_new)

        except:
             if user_city in ['h','H','help','Help']:
                print('''
                    输入正确的城市名，查询该城市的天气
                    输入h,H,help,Help其中的一个，查询帮助文档
                    输入history，获取查询历史
                    输入c,f,转换温度单位（摄氏度，华氏度）
                    输入数字0,1,2，改变查询日期
                    输入数字3，可查询近三天的天气！
                    输入exit，或者quit，退出天气查询系统
                    ''')
             elif user_city == 'history':
                 for history in history_list:
                     print(history)
             elif user_city in ['c','f']:
                 unit = user_city
                 print("已转换为您所要的温度单位！")
             elif user_city in ['0', '1', '2']:
                 day = int(user_city)
                 print("已转换日期！")
             elif user_city == '3':
                 print("您正在查询近三天的天气！")
                 user = input("请输入： ")
                 for d in [0,1,2]:                     
                     result = fet_weather(user,unit)
                     user_weather_new = show_up_weather(result,d)
                     print(user_weather_new)
                     history_list.append(user_weather_new)
             elif user_city in ['exit','quit']:
                 print('感谢使用，已退出！')
                 exit()
             else:
                 print("滴滴滴~请确认您输入的城市是否存在！输入help查看帮助")
            
            
play()


