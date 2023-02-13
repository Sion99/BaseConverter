from flask import Flask
from flask import request, render_template

app = Flask(__name__)


def atoi_base(number, from_base):
    sign = 1
    if '-' in number:
        sign = -1
    result = 0

    for i in number:
        current = from_base.index(i)
        result = result * 10 + current

    print('atoi_base done')
    return result * sign


def convert_base(number, to_base):
    arr = ''
    sign = 0
    if number < 0:
        sign = 1
    while True:
        arr += to_base[number % len(to_base)]
        print(arr)
        number = int(number / len(to_base))
        if number == 0:
            break
    if (sign == 1):
        arr += '-'
    arr = arr[::-1]
    print('convert_base done')
    return arr


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/convert', methods=['POST'])
def convertbase():
    from_base = int(request.form['from-base'])
    to_base = int(request.form['to-base'])
    number = str(request.form['number'])
    base = ['0', '1', '2', '3', '4', '5', '6', '7',
            '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

    frombase = base[0:from_base]
    tobase = base[0:to_base]
    print('from_base, to_base, number, frombase, tobase')
    print(from_base, to_base, number, frombase, tobase)
    result = atoi_base(number, frombase)
    converted = convert_base(result, tobase)
    print('여기까지 완료')
    return render_template('result.html', converted=converted)


if __name__ == '__main__':
    app.run()
