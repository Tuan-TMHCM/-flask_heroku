from flask import Flask, render_template, redirect, url_for, request
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def welcome():
    return redirect('/login')


@app.route('/home')
def home():
    return 'Khai Báo Thành Công'

@app.route('/About')
def About():
    return redirect('/About')

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    giohientai = datetime.now().strftime("%H:%M:%S")
    ngayhientai = datetime.now().strftime("%d/%m/%Y")
    if request.method == 'POST':
        if request.form['MaNV'] == 'admin' and request.form['Ten'] == 'admin':
            if request.method == 'POST':
                with open("list.csv", "r+") as f:
                    mydatalist = f.readline()
                    namelist = []
                    for line in mydatalist:
                        entry = line.split(",")
                        namelist.append(entry[0])
                    f.writelines(f"\n{ngayhientai}, {giohientai}, {request.form['MaNV']}, {request.form['Ten']}, "
                                 f"{request.form['depart']}, {request.form.get('Id')}")
            return redirect(url_for('home'))
        elif request.form['username'] == 'admin' and request.form['password'] == 'admin123':
            return render_template('test.html')
        else:
            error = 'Thông Tin Đăng Nhập Bị Sai, Vui Lòng Đăng Nhập Lại.'
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)