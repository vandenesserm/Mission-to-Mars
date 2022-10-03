# Import dependencies: 
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

# Set up Flask:
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Define the index route for the HTML page:
@app.route("/")
def index():
   print("===========")
   print("/")
   print("=========== \n")
   mars = mongo.db.mars.find_one()
   print("===== mars ====")
   print(mars)
   print("=========== \n")
   return render_template("index.html", mars=mars)

# Define the scrape route and function:
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()

   print("======== mars_data ===========")
   print(mars_data)
   print("=====================")

   mars.replace_one({}, mars_data, upsert=True)

   return redirect('/')

# Run Flask:
if __name__ == "__main__":
   app.run(debug=True, port=5000)