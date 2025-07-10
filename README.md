# Ubermelon Shopping App
Ubermelon is a basic e-commerce web application built using Flask. It allows users to browse different types of melons, view detailed product information, add items to a shopping cart, and login to a user account. This project demonstrates fundamental web development concepts using Python, Flask, Jinja2, and session management.
## Features

-  Homepage with navigation
-  Browse all available melons
-  View details of individual melons
-  Add melons to shopping cart (session-based)
-  View and manage cart contents
-  Simple login system for users
-  Checkout placeholder for future updates

  ## Project Structure
  ubermelon/
│
├── app.py # Main Flask app
├── model.py # Melon and Customer data classes
├── templates/
│ ├── homepage.html
│ ├── all_melons.html
│ ├── melon_details.html
│ ├── cart.html
│ └── login.html
└── static/ # (Optional) For CSS/images
