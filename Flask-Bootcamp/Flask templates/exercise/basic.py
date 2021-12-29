from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report')
def report():
    name = request.args.get('user_name')
    lowercase_exists = any(character.islower() for character in name)
    uppercase_exists = any(character.isupper() for character in name)
    ends_with_number = any(name.endswith(number) for number in '0123456789')
    all_good = lowercase_exists and uppercase_exists and ends_with_number
    return render_template("report.html", name=name, lowercase_exists=lowercase_exists, uppercase_exists=uppercase_exists, ends_with_number=ends_with_number, all_good=all_good)


if __name__ == "__main__":
    app.run(debug=True)
