from flask import Flask,request,render_template
import datetime
app = Flask(__name__)

@app.route('/')
def get_name():
    return render_template('hello_submit_form.html')

@app.route('/greet', methods = ['POST'])
def greet():
    typed_name=request.form['name']
    print(typed_name)
    return render_template('hello.html', name=typed_name)

@app.route('/add')
def add():
    first_number = request.args.get('first', '')
    second_number = request.args.get('second', '')
    if first_number and second_number:
        try:
            result = int(first_number) + int(second_number)
        except ValueError:
            return 'Invalid data'
        return f'{first_number} + {second_number} = {result}'
    else:
        return 'No arguments detected'
@app.route('/bdayform')
def bdayform():
    return render_template('bday_submit_form.html')
@app.route('/bday', methods = ['POST'])
def bday():
    dobstr=request.form['dob']
    dob = datetime.datetime.strptime(dobstr, "%Y-%m-%d").date()
    today = datetime.date.today()

    print("My date of birth is: ", dob)
    print("Today is: ", today)
    birthday_this_year = datetime.date(today.year, dob.month, dob.day)
    birthday_next_year = datetime.date(today.year+1, dob.month, dob.day)

    if birthday_this_year > today:
        next_birthday = birthday_this_year
    else:
        next_birthday = birthday_next_year

    days_to_birthday = (next_birthday - today).days
    age = (next_birthday - dob).days // 365     # Note, this doesn't take account of leap years so isn't perfect.
    return (f'Age at next birthday: {age}<br>'
    f'Days to next birthday: {days_to_birthday}<br>'
    f'Next birthday: {next_birthday}')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)