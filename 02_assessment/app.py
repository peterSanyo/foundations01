from flask import Flask, redirect, url_for, render_template, send_file
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
    "phantom_syntopia" : {
    "name": "Phantom Syntopia",
    "image": "IMAGE OF ELEGANT LUXURY-CAR",
    "quote": ' "a state-of-the-art experience [...] by the forces of nature." ',
    "quoted":"Iris van Herpen",
    "offerer":"Rolls Royce X Iris van Herpen",
    "dimensions": "571x214x157 cm",
    "materials": "Leather, Fabric, Steel",
    "category":"Vehicle",
    "price": "-"
    },
    "white_fromme" : {
    "name": "White Fromme Collection",
    "image": "IMAGE OF MINIMALISTIC SET OF INTERIOUR DESIGN CLASSIS",
    "quote": ' "This design was inspired by the personal story of Tom Chung." ',
    "quoted":"Petite Friture, French Design Brand",
    "offerer":"Petite Friture X Tom Chang",
    "dimensions": "-",
    "materials": "Hardwearing Aluminium",
    "category":"Exclusive Furniture",
    "price": "-"
    },
    "color_palette" : {
    "name": "2023 Color Palette",
    "image": "IMAGE OF TRANSLUCENT GLASSSTRIPES OF A PASTELL COLOUR PALETTE",
    "quote": ' "This collection allowed us to be more introspective about the meaning of colour in our lives." ',
    "quoted":"Ryan Smith, chief creative of 3form",
    "offerer":"3form",
    "dimensions": "-",
    "materials": "Varia, Chroma and Glass",
    "category":"Modular Interiour Design ",
    "price": "-"
    },
}

# Landin-page, overview and downloadable material 
@app.route("/gallery")
def landing():
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
    "phantom_syntopia" : {
    "name": "Phantom Syntopia",
    "image": "IMAGE OF ELEGANT LUXURY-CAR",
    "quote": ' "a state-of-the-art experience [...] by the forces of nature." ',
    "quoted":"Iris van Herpen",
    "offerer":"Rolls Royce X Iris van Herpen",
    "dimensions": "571x214x157 cm",
    "materials": "Leather, Fabric, Steel",
    "category":"Vehicle",
    "price": "-"
    },
    "white_fromme" : {
    "name": "White Fromme Collection",
    "image": "IMAGE OF MINIMALISTIC SET OF INTERIOUR DESIGN CLASSIS",
    "quote": ' "This design was inspired by the personal story of Tom Chung." ',
    "quoted":"Petite Friture, French Design Brand",
    "offerer":"Petite Friture X Tom Chang",
    "dimensions": "-",
    "materials": "Hardwearing Aluminium",
    "category":"Exclusive Furniture",
    "price": "-"
    },
    "color_palette" : {
    "name": "2023 Color Palette",
    "image": "IMAGE OF TRANSLUCENT GLASSSTRIPES OF A PASTELL COLOUR PALETTE",
    "quote": ' "This collection allowed us to be more introspective about the meaning of colour in our lives." ',
    "quoted":"Ryan Smith, chief creative of 3form",
    "offerer":"3form",
    "dimensions": "-",
    "materials": "Varia, Chroma and Glass",
    "category":"Modular Interiour Design ",
    "price": "-"
    },
}

  return render_template("01_landing.html", pieces=pieces)

# Exhibit 1 
@app.route("/exhibit1", methods=["GET", "WRITE"])
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

# Exhibit 2  
@app.route("/exhibit2")
def product2():
  name="Paul"
  object=pieces["phantom_syntopia"]

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

  # Exhibit 3  
@app.route("/exhibit3")
def product3():
  name="Paul"
  object=pieces["white_fromme"]

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

  # Exhibit 4   
@app.route("/exhibit4")
def product4():
  name="Paul"
  object=pieces["color_palette"]

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

# download 
@app.route("/downloads")
def exhibition():
  return send_file("static/downloads/exhibition.txt", as_attachment=True)

if __name__ == "__main__":
  app.run()