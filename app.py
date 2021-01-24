from flask import Flask

from flask import render_template, request, redirect
import csv
static_folder = 'static'
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/review", methods=["GET","POST"])
def review():
    
    if request.method == "POST":
        req = request.form
        print(req)
        return redirect(request.url)

    return render_template("review.html")


@app.route("/database")
def index():
  with open('Reviews_database.csv') as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    first_line = True
    reviews = []
    for row in data:
      if not first_line:
        reviews.append({
          "name": row[0],
          "product": row[1],
          "review": row[2]
        })
      else:
        first_line = False
  return render_template("review.html", reviews=reviews)

     
if __name__ == "__main__":
    app.run(debug=True)