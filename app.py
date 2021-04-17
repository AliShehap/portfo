from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/<page_name>")
def html_page(page_name):
    return render_template(page_name)

# save to a txt file


def save_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

# save to a csv file


def save_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(
            database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        save_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong. Try again!'


app.run(host='0.0.0.0', port=5000)
