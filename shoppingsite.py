"""Ubermelon shopping application Flask server.

Provides web interface for browsing melons, seeing detail about a melon, and
put melons in a shopping cart.

Authors: Joel Burton, Christian Fernandez, Meggie Mahnken.
"""


from flask import Flask, render_template, redirect, flash, session, request
import jinja2

import model


app = Flask(__name__)

# Need to use Flask sessioning features

app.secret_key = 'this-should-be-something-unguessable'

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.

app.jinja_env.undefined = jinja2.StrictUndefined


@app.route("/")
def index():
    """Return homepage."""

    return render_template("homepage.html")


@app.route("/melons")
def list_melons():
    """Return page showing all the melons ubermelon has to offer"""

    melons = model.Melon.get_all()
    return render_template("all_melons.html",
                           melon_list=melons)


@app.route("/melon/<int:id>")
def show_melon(id):
    """Return page showing the details of a given melon.

    Show all info about a melon. Also, provide a button to buy that melon.
    """

    melon = model.Melon.get_by_id(id)
    print melon
    return render_template("melon_details.html",
                           display_melon=melon)


@app.route("/cart")
def shopping_cart():
    """Display content of shopping cart."""

    # TODO: Display the contents of the shopping cart.
    #   - The cart is a list in session containing melons added
    
    cart_list = session.get('cart',[])          # getting the value for the key 'cart' in our session dictionary, if a key has not been created (no cookies yet)we will get back an empty list
    cart = {}                                   # initializing an empty dictionary for our cart items
    order_total = 0                             # setting the order_total equal to 0
    for item in cart_list:                      # iterating over each item(id) in our cart list
        melons = cart.setdefault(item, {})      # setting variable melons equal to the value of the key 'item' in our 'cart' dictionary, if key is not there, set it to an empty dictionary
        if melons:                              # if 'melons' is not empty (i.e. we have already added this melon in)
            # import pdb; pdb.set_trace()
            melons["quantity"] += 1             # add one to the value for the quantity
    
        else:                                   # melons is not empty (i.e. we have already added a key for this item)
            melon_info = model.Melon.get_by_id(item)    # get some info from the query executed from model
            melons["name"] = melon_info.common_name     #set key "name" equal to common_name from the query
            melons["price"] = melon_info.price          # set key "price" equal to price from the query
            melons["quantity"] = 1                      # set key "quantity" equal to one
        
        melons["total"] = melons["price"] * melons["quantity"]  #set key "total" equal to the price * quantity
        order_total = order_total + melons["total"]             # update order_total
        
    cart = cart.values()                                        # set cart equal to the values of the cart dictionary (i.e. )
            
    return render_template("cart.html", cart=cart, order_total=order_total)


@app.route("/add_to_cart/<int:id>")
def add_to_cart(id):
    """Add a melon to cart and redirect to shopping cart page.

    When a melon is added to the cart, redirect browser to the shopping cart
    page and display a confirmation message: 'Successfully added to cart'.
    """

    # TODO: Finish shopping cart functionality
    #   - use session variables to hold cart list
    
    cart = session.setdefault('cart',[])              #setting the variable cart equal to the value of the dictionary key 'cart' within our session, which is an empty list if it is not already in the dictionary
    
    session['cart'].append(id)                        #appending the melon id to the cart key in our session dictionary
        
    flash("Melon was succesully added to your cart!") # Flashing this message when we add a melon
    
    return redirect("/cart")                          #redirect to the cart page

@app.route("/login", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def process_login():
    """Log user into site.

    Find the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session.
    """

    # TODO: Need to implement this!
    email = request.form.get("email")
    password = request.form.get("password")
    
    try:
        customer = model.Customer.get_by_email(email)
        if customer.password == password:
            flash("Login successful!")
            return redirect("/melons")
        else:
            flash("Incorrect password")
            return redirect("/login")
      
    except:
            flash("no such email")
            return redirect("/login")


@app.route("/checkout")
def checkout():
    """Checkout customer, process payment, and ship melons."""

    # For now, we'll just provide a warning. Completing this is beyond the
    # scope of this exercise.

    flash("Sorry! Checkout will be implemented in a future version.")
    return redirect("/melons")


if __name__ == "__main__":
    app.run(debug=True)
