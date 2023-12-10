from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open("database.csv", mode="a", newline='') as database:  # 'a' for append mode
        writer = csv.writer(database, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Write only if data fields exist
        if all(key in data for key in ['name', 'email', 'subject', 'message']):
            writer.writerow([data.get('name'), data.get(
                'email'), data.get('subject'), data.get('message')])


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return redirect("/thankyou.html#four")
        except:
            return "did not save to database"
    else:
        return "something went wrong. Try again!"
