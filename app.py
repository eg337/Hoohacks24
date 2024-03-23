from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')

    link = request.form.get('link')

    print(link)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()