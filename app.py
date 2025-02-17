from flask import (
    Flask,
    render_template,
    request,
    session,
    g,
    jsonify,
    url_for,
    make_response,
)
from main import getc
import sqlite3
import plotly.graph_objects as go


app = Flask(__name__)
app.static_folder = "static"
app.secret_key = "your_secret_key"


@app.route("/your_route")
def your_route_handler():
    response = make_response("your_response_data")
    response.headers["cache-control"] = "no-store"  # 不緩存
    return response


# 連接到資料庫
def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("city.db")
    return db


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("web.html")


@app.route("/sub", methods=["GET", "POST"])
def sub():
    num = request.form["num"]
    session["num"] = num  # 存取使用者輸入的數字
    result_data = session.get("result_data", [])  # 獲取之前保存的查詢結果列表，默認為空列表
    # print("result_data sub = " , result_data)

    # 基隆市
    if int(num) == 1:
        # print("in")
        city = '以下為"基隆市"的搜尋結果'
        num_f = "keelung"
        # city_p = '基隆市'
        # session["city_p"] = city_p
        con = get_db()
        num_c = con.cursor()
        num_c.execute("SELECT * FROM " + num_f)
        data = num_c.fetchall()
        # print(data)

        return render_template("web.html", data=data, city=city)
    # 台北市
    if int(num) == 2:
        city = '以下為"台北市"的搜尋結果'
        city_p = "台北市"
        session["city_p"] = city_p
        num_f = "taipei"
        con = get_db()
        num_c = con.cursor()
        num_c.execute("SELECT * FROM " + num_f)
        data = num_c.fetchall()
        # print(data)

        return render_template("web.html", data=data, city=city)
    # 新北市
    if int(num) == 3:
        city = '以下為"新北市"的搜尋結果'
        city_p = "新北市"
        session["city_p"] = city_p
        num_f = "new_taipei"
        con = get_db()
        num_c = con.cursor()
        num_c.execute("SELECT * FROM " + num_f)
        data = num_c.fetchall()

        return render_template("web.html", data=data, city=city)
    # 4:桃園市
    if int(num) == 4:
        city = '以下為"桃園市"的搜尋結果'
        city_p = "桃園市"
        session["city_p"] = city_p
        num_f = "taoyuan"
        con = get_db()
        num_c = con.cursor()
        num_c.execute("SELECT * FROM " + num_f)
        data = num_c.fetchall()

        return render_template("web.html", data=data, city=city)
    # 5:新竹縣
    if int(num) == 5:
        city = '以下為"新竹縣"的搜尋結果'
        city_p = "新竹縣"
        session["city_p"] = city_p
        num_f = "hsinchu_county"
        con = get_db()
        num_c = con.cursor()
        num_c.execute("SELECT * FROM " + num_f)
        data = num_c.fetchall()

        return render_template("web.html", data=data, city=city)
    # 6:新竹市
    if int(num) == 6:
        city = '以下為"新竹市"的搜尋結果'
        city_p = "新竹市"
        session["city_p"] = city_p
        num_f = "hsinchu"
        con = get_db()
        num_c = con.cursor()
        num_c.execute("SELECT * FROM " + num_f)
        data = num_c.fetchall()

        return render_template("web.html", data=data, city=city)
    # 7:苗栗縣
    if int(num) == 7:
        city = '以下為"苗栗縣"的搜尋結果'
        city_p = "苗栗市"
        session["city_p"] = city_p
        num_f = "miaoli_county"
        con = get_db()
        num_c = con.cursor()
        num_c.execute("SELECT * FROM " + num_f)
        data = num_c.fetchall()

        return render_template("web.html", data=data, city=city)
    # 8:台中市
    if int(num) == 8:
        city = '以下為"台中市"的搜尋結果'
        city_p = "台中市"
        session["city_p"] = city_p
        num_f = "taichung"
        con = get_db()
        num_c = con.cursor()
        num_c.execute("SELECT * FROM " + num_f)
        data = num_c.fetchall()

        return render_template("web.html", data=data, city=city)
    # 9:南投縣
    if int(num) == 9:
        city = '以下為"南投縣"的搜尋結果'
        city_p = "南投縣"
        session["city_p"] = city_p
        num_f = "nantou_county"
        con = get_db()
        num_c = con.cursor()
        num_c.execute("SELECT * FROM " + num_f)
        data = num_c.fetchall()

        return render_template("web.html", data=data, city=city)
    # 10:彰化縣
    if int(num) == 10:
        city = '以下為"彰化縣"的搜尋結果'
        city_p = "彰化縣"
        session["city_p"] = city_p
        num_f = "changhua_county"
        con = get_db()
        num_c = con.cursor()
        num_c.execute("SELECT * FROM " + num_f)
        data = num_c.fetchall()

        return render_template("web.html", data=data, city=city)
    # 11:雲林縣
    if int(num) == 11:
        city = '以下為"雲林縣"的搜尋結果'
        city_p = "雲林縣"
        session["city_p"] = city_p
        num_f = "yunlin_county"
        con = get_db()
        num_c = con.cursor()
        num_c.execute("SELECT * FROM " + num_f)
        data = num_c.fetchall()

        return render_template("web.html", data=data, city=city)
    # 12:嘉義縣
    if int(num) == 12:
        city = '以下為"嘉義縣"的搜尋結果'
        city_p = "嘉義縣"
        session["city_p"] = city_p
        num_f = "chiayi_county"
        con = get_db()
        num_c = con.cursor()
        num_c.execute("SELECT * FROM " + num_f)
        data = num_c.fetchall()

        return render_template("web.html", data=data, city=city)
    # 13:嘉義市
    if int(num) == 13:
        city = '以下為"嘉義市"的搜尋結果'
        city_p = "嘉義市"
        session["city_p"] = city_p
        num_f = "chiayi"
        con = get_db()
        num_c = con.cursor()
        num_c.execute("SELECT * FROM " + num_f)
        data = num_c.fetchall()

        return render_template("web.html", data=data, city=city)
    # 14:台南市
    if int(num) == 14:
        city = '以下為"台南市"的搜尋結果'
        city_p = "台南市"
        session["city_p"] = city_p
        num_f = "tainan"
        con = get_db()
        num_c = con.cursor()
        num_c.execute("SELECT * FROM " + num_f)
        data = num_c.fetchall()

        return render_template("web.html", data=data, city=city)
    # 15:高雄市
    if int(num) == 15:
        city = '以下為"高雄市"的搜尋結果'
        city_p = "高雄市"
        session["city_p"] = city_p
        num_f = "kaohsiung"
        con = get_db()
        num_c = con.cursor()
        num_c.execute("SELECT * FROM " + num_f)
        data = num_c.fetchall()

        return render_template("web.html", data=data, city=city)
    # 16:屏東縣
    if int(num) == 16:
        city = '以下為"屏東縣"的搜尋結果'
        city_p = "屏東縣"
        session["city_p"] = city_p
        num_f = "pingtung_county"
        con = get_db()
        num_c = con.cursor()
        num_c.execute("SELECT * FROM " + num_f)
        data = num_c.fetchall()

        return render_template("web.html", data=data, city=city)
    # 17:台東縣
    if int(num) == 17:
        city = '以下為"台東縣"的搜尋結果'
        city_p = "台東縣"
        session["city_p"] = city_p
        num_f = "taitung_county"
        con = get_db()
        num_c = con.cursor()
        num_c.execute("SELECT * FROM " + num_f)
        data = num_c.fetchall()

        return render_template("web.html", data=data, city=city)
    # 18:花蓮縣
    if int(num) == 18:
        city = '以下為"花蓮縣"的搜尋結果'
        city_p = "花蓮縣"
        session["city_p"] = city_p
        num_f = "hualien_county"
        con = get_db()
        num_c = con.cursor()
        num_c.execute("SELECT * FROM " + num_f)
        data = num_c.fetchall()

        return render_template("web.html", data=data, city=city)
    # 19:宜蘭縣
    if int(num) == 19:
        city = '以下為"宜蘭縣"的搜尋結果'
        city_p = "宜蘭縣"
        session["city_p"] = city_p
        num_f = "yilan_county"
        con = get_db()
        num_c = con.cursor()
        num_c.execute("SELECT * FROM " + num_f)
        data = num_c.fetchall()

        return render_template("web.html", data=data, city=city)
    # 20:澎湖縣
    if int(num) == 20:
        city = '以下為"澎湖縣"的搜尋結果'
        city_p = "澎湖縣"
        session["city_p"] = city_p
        num_f = "penghu_county"
        con = get_db()
        num_c = con.cursor()
        num_c.execute("SELECT * FROM " + num_f)
        data = num_c.fetchall()

        return render_template("web.html", data=data, city=city)
    # 21:金門縣
    if int(num) == 21:
        city = '以下為"金門縣"的搜尋結果'
        city_p = "金門縣"
        session["city_p"] = city_p
        num_f = "kinmen_county"
        con = get_db()
        num_c = con.cursor()
        num_c.execute("SELECT * FROM " + num_f)
        data = num_c.fetchall()

        return render_template("web.html", data=data, city=city)
    # 22:連江縣
    if int(num) == 22:
        city = '以下為"連江縣"的搜尋結果'
        city_p = "連江縣"
        session["city_p"] = city_p
        num_f = "lienchiang_county"
        con = get_db()
        num_c = con.cursor()
        num_c.execute("SELECT * FROM " + num_f)
        data = num_c.fetchall()

        return render_template("web.html", data=data, city=city)


@app.route("/search", methods=["GET", "POST"])
def search():
    num_a = request.form["num_a"]
    num = session.get("num")  # 獲取num
    result = getc(num, num_a)  # 爬蟲

    result_tem_date = [result[i] for i in range(2)]

    result_data = session.get("result_data", [])
    print("result_data = ", result_data)
    print("result_data_len = ", len(result_data))

    if len(result_data) == 4:
        result_data.pop(0)  # 移除舊的資料
        result_data.pop(0)

    session["result_data"] = result_data + result_tem_date  # 合併新舊資料

    result_data = session.get("result_data")

    print("num =", num)
    print("num_a =", num_a)

    all_temperatures_first = []
    all_dates_first = []
    all_temperatures_second = []
    all_dates_second = []
    temperatures = []
    dates = []

    if len(result_data) == 4:
        # print("in")
        for i in range(
            4
        ):  # result_data = [[溫度] , [[日期] , [日期]] ... , [溫度] , [[日期] , [日期] ...]
            if i == 0 or i == 2:
                temperatures = [int(temp) for temp in result_data[i]]
                if i == 0:
                    all_temperatures_first.extend(temperatures)
                else:
                    all_temperatures_second.extend(temperatures)
            else:
                dates = [date[0] for date in result_data[1]]
                if i == 1:
                    all_dates_first.extend(dates)
                else:
                    all_dates_second.extend(dates)

    else:
        # print("in else")
        temperatures = [int(temp) for temp in result_data[0]]
        dates = [date[0] for date in result_data[1]]
        all_temperatures_first.extend(temperatures)
        all_dates_first.extend(dates)

    session["all_temperatures_first"] = all_temperatures_first
    session["all_temperatures_second"] = all_temperatures_second
    session["all_dates_first"] = all_dates_first
    session["all_dates_second"] = all_dates_second

    print("all_temperatures_first = ", all_temperatures_first)
    print("all_temperatures_second = ", all_temperatures_second)
    print("all_dates_first = ", all_dates_first)
    print("all_dates_second = ", all_dates_second)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=all_dates_first,
            y=all_temperatures_first,
            mode="lines+markers",
            name="first",
            line=dict(width=3),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=all_dates_second,
            y=all_temperatures_second,
            mode="lines+markers",
            name="second",
            line=dict(width=3),
        )
    )

    fig.update_layout(
        title="溫度變化折線圖",
        xaxis_title="日期",
        yaxis_title="溫度",
        # plot_bgcolor='rgba(0,0,0,0)',  # 設定折線圖區域的背景顏色為透明
        paper_bgcolor="rgba(0,0,0,0)",  # 設定整個圖表的背景顏色為透明
        autosize=False,  # 停用自動調整大小
        width=800,  # 設定圖表寬度
        height=600,  # 設定圖表高度
        xaxis=dict(
            title="日期",
            title_font=dict(size=25),  # 設定 x 軸標題的字體大小
            tickfont=dict(color="black"),  # 設定 x 軸刻度標籤的字體顏色
            linewidth=2,  # 設定 x 軸線的寬度
            gridwidth=2,  # 設定 x 軸格線的寬度
        ),
        yaxis=dict(
            title="溫度",
            title_font=dict(size=25),  # 設定 y 軸標題的字體大小
            tickfont=dict(color="black"),  # 設定 y 軸刻度標籤的字體顏色
            linewidth=2,  # 設定 y 軸線的寬度
            gridwidth=2,  # 設定 y 軸格線的寬度
        ),
        title_font=dict(color="black"),  # 設定標題的字體顏色
    )
    plot_html = fig.to_html(full_html=False)

    today_weather_first = all_temperatures_first
    today_weather_second = all_temperatures_second
    today_date_first = all_dates_first
    today_date_second = all_dates_second

    if len(today_weather_second) == 0 and len(today_date_second) == 0:
        today_weather_first = all_temperatures_first[0]
        today_date_first = all_dates_first[0]
        text_d = "日期 = " + today_date_first
        # print(text_d)
        text_t = "溫度 = " + str(today_weather_first) + " ℃"
        text_tm = ""
    else:
        today_weather_first = all_temperatures_first[0]
        today_weather_second = all_temperatures_second[0]
        today_date_first = all_dates_first[0]
        today_date_second = all_dates_second[0]
        text_d = "日期 = " + today_date_second
        text_t = (
            "溫度(1) = "
            + str(today_weather_first)
            + " ℃"
            + " 溫度(2) = "
            + str(today_weather_second)
            + " ℃"
        )
        text_tm = "2地溫差為 = " + str(
            abs(int(today_weather_first) - int(today_weather_second))
        )

    return render_template(
        "web.html", plot_html=plot_html, text_d=text_d, text_t=text_t, text_tm=text_tm
    )


@app.route("/jsd", methods=["GET", "POST"])
def jsd():
    print("in js_d")
    all_temperatures_first = session.get("all_temperatures_first")
    all_temperatures_second = session.get("all_temperatures_second")
    all_dates_first = session.get("all_dates_first")
    all_dates_second = session.get("all_dates_second")

    data = {
        "all_temperatures_first": all_temperatures_first,
        "all_temperatures_second": all_temperatures_second,
        "all_dates_first": all_dates_first,
        "all_dates_second": all_dates_second,
    }

    js_url = url_for("static", filename="event.js")
    response = jsonify(data)
    response.headers["Location"] = js_url

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


# ans = getc(2 , 6)
# print(ans)
