from flask import Flask, render_template, request
from weather_api import fetchWeather, show_weather


app = Flask(__name__)
history_list = []
@app.route('/', methods = ['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/user_request')
def process_request():
    if request.args.get('help') == "帮助":
        return render_template('help.html')
    elif request.args.get('query') == "查询":
        city = request.args.get('city')
        result = fetchWeather(city)
        weather_dic = show_weather(result)
        history_list.append(weather_dic)
        return render_template('query.html', weather_dic = weather_dic)
    elif request.args.get('history') == "历史":
        return render_template("history.html", history_list = history_list)
if __name__ == '__main__':
    app.run(debug = True)
