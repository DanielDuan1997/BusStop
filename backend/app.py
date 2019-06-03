from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app, supports_credentials=True, resources=r'/*')

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response

def get_special_days(date):
    return None

@app.route('/', methods=["POST"])
def get_schedule():
    post_data = request.form.to_dict()
    place_from = post_data.get("from")
    place_to = post_data.get("to")
    start_date = datetime.strptime(post_data.get("date"), "%Y-%m-%d")

    sp_check = get_special_days(start_date)
    if sp_check != None:
        return make_response(jsonify({'schedule': sp_check[0], 'explanation': sp_check[1]}), 200)

    weekday = start_date.weekday()
    notice = ""
    schedule = []
    if place_from == r"张江":
        if place_to == r"邯郸": # ZhangJiang -> HanDan
            notice = r"Ⅰ期图书馆西侧（近足球场一侧人行道）"
            if weekday < 5:
                schedule = ['07:15', '08:00', '08:40', '09:00', '10:00', '11:50',
                            '12:15', '12:40', '14:15', '15:20', '16:00', '16:10',
                            '16:20', '16:40', '17:00', '17:20', '18:30', '21:30']
            else:
                schedule = ['9:20', '17:30']
        elif place_to == r"枫林": # ZhangJiang -> FengLin
            notice = r"Ⅱ期1号门卫室东侧"
            if weekday < 5:
                schedule = ['7:50', '12:15', '15:00', '17:00', '19:00']
            else:
                schedule = []
        elif place_to == r"上科大":
            notice = r"图书馆西侧（近足球场一侧人行道）"
            if weekday < 5:
                schedule = ['12:30', '18:00', '21:30', '22:00']
            else:
                schedule = ['17:20', '21:00']
    elif place_from == r"邯郸":
        if place_to == r"张江": # HanDan -> ZhangJiang
            notice = r"日月西路近理科图书馆"
            if weekday < 5:
                schedule = ['07:10', '07:40', '08:00', '08:30', '09:00', '10:00',
                            '11:50', '12:30', '12:45', '14:30', '15:30', '16:15',
                            '17:20', '18:30', '20:20', '20:30', '21:00', '21:20']
            else:
                schedule = ['8:30', '16:30']
        elif place_to == r"江湾": # HanDan -> JiangWan
            notice = r"日月西路近理科图书馆"
            if weekday < 5:
                schedule = ['07:30', '07:40', '08:00', '08:30', '09:00', '09:30',
                            '10:00', '10:20', '11:00', '11:30', '11:45', '12:00',
                            '12:30', '13:00', '13:30', '14:00', '14:30', '15:00',
                            '15:30', '16:00', '16:15', '16:20', '16:30', '17:00',
                            '17:15', '17:25', '17:35', '17:45', '18:00', '18:30',
                            '20:00', '20:20', '20:30', '20:50', '21:00', '21:20',
                            '21:40', '22:00', '22:15', '22:30']
            else:
                schedule = ['08:20', '08:40', '09:00', '09:20', '09:40', '17:00',
                            '20:15', '21:00', '21:45', '22:30']
        elif place_to == r"枫林": # HanDan -> FengLin
            notice = r"老化学楼东侧"
            if weekday < 5:
                schedule = ['06:55', '07:10', '08:15', '09:15', '10:15', '11:00',
                            '12:30', '13:00', '14:00', '15:30', '16:00', '16:55',
                            '17:10', '18:00', '19:30', '20:20', '21:25']
            else:
                schedule = ['08:00', '16:30']
    elif place_from == r"枫林":
        if place_to == r"邯郸": # FengLin -> HanDan
            notice = r"西苑（近8号楼）"
            if weekday < 5:
                schedule = ['07:10', '07:20', '08:15', '09:15', '11:00', '11:45',
                            '12:15', '13:00', '14:00', '14:30', '15:30', '16:00',
                            '16:55', '17:10', '17:25', '18:20', '20:20', '21:15',
                            '21:50']
            else:
                schedule = ['09:00', '17:30']
        elif place_to == r"张江": # FengLin -> ZhangJiang
            notice = r"西苑（近8号楼）"
            if weekday < 5:
                schedule = ['07:00', '07:30', '09:00', '12:15', '13:30', '16:30',
                            '19:00']
    elif place_from == r"江湾":
        if place_to == r"邯郸": # JiangWan -> HanDan
            notice = r"校区宣传栏"
            if weekday < 5:
                schedule = ['07:10', '07:20', '07:30', '07:40', '07:50', '08:00',
                            '08:15', '08:30', '08:45', '09:00', '09:15', '09:30',
                            '10:00', '10:30', '11:10', '11:40', '12:00', '12:15',
                            '12:30', '12:40', '13:00', '13:30', '14:00', '15:00',
                            '15:15', '15:30', '16:00', '16:30', '16:55', '17:00',
                            '17:10', '17:30', '18:00', '19:00', '20:00', '20:30',
                            '21:00', '21:20', '21:45', '22:10']
            else:
                schedule = ['07:40', '08:00', '08:20', '08:40', '09:00', '09:20',
                            '09:40', '10:20', '17:30', '20:40', '21:20', '22:10']
    elif place_from == r"上科大":
        if place_to == r"张江": # ShangKeDa -> ZhangJiang
            notice = r"上科大学生宿舍区内"
            if weekday < 5:
                schedule = ['07:30', '08:00', '08:30', '09:00', '13:00', '14:15', '17:30']
            else:
                schedule = ['09:00', '12:00', '17:00']
    return make_response(jsonify({'schedule': schedule, 'notice': notice}), 200)

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', debug=True, port=5001)
