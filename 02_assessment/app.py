from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)
app.config.from_object("config")

pieces = {
  "era300" : {
    "name": "Era 300",
    "image": "IMAGE OF MINIMALIST SPEAKER",
    "quote": ' "The most suffisticated product Sonos has built" ',
    "quoted":"Dana Krieger, head of Sonos",
    "offerer":"Sonos",
    "dimensions": "30x20x10 cm",
    "materials": "hard case plastic and wood",
    "category":"Spatial home Audio",
    "price": " 399$"
    },
}

@app.route("/landing")
def landing():
  return render_template("01_landing.html")

@app.route("/product")
def product():
  name="Paul"
  return render_template("ppage.html", name=name)

@app.route("/product1")
def product1():
  name="Paul"
  object=pieces["era300"]

  return render_template("ppage.html", 
  name=object["name"], 
  image=object["image"],
  quote=object["quote"], 
  quoted=object["quoted"],
  offerer=object["offerer"],
  dimensions=object["dimensions"],
  materials=object["materials"],
  category=object["category"],
  price=object["price"],
  )

@app.route("/product2")
def product2():
  name="Paul"
  return render_template("ppage.html", name=name)

@app.route("/product3")
def product3():
  name="Paul"
  return render_template("ppage.html", name=name)

@app.route("/product4")
def product4():
  name="Paul"
  return render_template("ppage.html", name=name)


if __name__ == "__main__":
  app.run()