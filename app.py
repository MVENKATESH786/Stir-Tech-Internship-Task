from flask import Flask, render_template, jsonify
import scrape_twitter

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run_script', methods=['GET'])
def run_script():
    data = scrape_twitter.scrape_trends()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
