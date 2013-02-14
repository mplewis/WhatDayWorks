from flask import Flask, render_template
app = Flask(__name__)

app.debug = True


test_cal = [
	[None, None, None, None, 1, 2, 3],
	[4, 5, 6, 7, 8, 9, 10],
	[11, 12, 13, 14, 15, 16, 17],
	[18, 19, 20, 21, 22, 23, 24],
	[25, 26, 27, 28, 29, 30, None]
]

@app.route('/')
def home():
    return render_template('index.html', calendar=test_cal)

if __name__ == '__main__':
    app.run()