'''--------------------------------------Question 1 Ans-----------------------------------------'''
'''

    Flask is a micro web framework written in Python. It is designed to be lightweight, modular, and
easy to use. Flask allows developers to build web applications quickly and efficiently by providing
tools and libraries for common tasks such as handling HTTP requests, rendering templates, and managing
database connections.

Advantages of Flask Framework include:

Lightweight and flexible:
     Flask is a micro-framework that is lightweight and easy to use. It allows developers to pick and
choose the components they need for their project, which makes it flexible.

Easy to learn and use:
     Flask has a simple and intuitive syntax that makes it easy to learn and use for developers who are
new to web development.

Modular design:
     Flask is designed with a modular structure, which means that developers can easily add or remove
components as needed.

Large community:
     Flask has a large and active community of developers who contribute to its development and provide
support to others. This makes it easy to find resources and solutions to problems.

Extensible:
     Flask is extensible, which means that developers can easily add custom functionality to their
applications using Flask extensions.

Built-in development server:
     Flask comes with a built-in development server, which makes it easy to test and debug applications
locally.

Flask is compatible with a wide range of libraries and tools: Flask can work with many third-party
libraries and tools, which means developers have a lot of flexibility when it comes to building web
applications.

'''

'''--------------------------------------Question 2 Ans-----------------------------------------'''

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()



'''--------------------------------------Question 3 Ans-----------------------------------------'''
'''

    In Flask, app routing refers to the process of mapping URL paths to the functions that handle them.
This is done using the @app.route() decorator, which is used to associate a function with a specific URL
path.

To map URL paths to functions:
     App routing allows us to map specific URL paths to functions in our Flask application. This makes
it easy to create different views (or pages) of our application and handle different HTTP requests
(such as GET and POST) for each view.

To create a navigable website:
     App routing helps us create a navigable website by defining different URL paths for each page of
our application. This allows users to easily navigate between different views of our application using
hyperlinks.

To handle dynamic URLs:
     App routing allows us to handle dynamic URLs, where the URL path contains variables that need to be
passed to the function that generates the view. For example, we can define a URL path like /user/
<username> to handle requests for different user profiles.

To create RESTful APIs:
     App routing is also used to create RESTful APIs (Application Programming Interfaces) that allow
external applications to interact with our Flask application. By defining different URL paths and HTTP
methods (such as GET, POST, PUT, DELETE), we can create a web service that exposes data and functionality
to other applications.

'''

'''--------------------------------------Question 4 Ans-----------------------------------------'''
from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'Welcome to ABC Corporation'

@app.route('/')
def index():
    company_name = 'ABC Corporation'
    location = 'India'
    contact_detail = '999-999-9999'
    return f'Company Name: {company_name}<br>Location: {location}<br>Contact Detail: {contact_detail}'

if __name__ == '__main__':
    app.run()

'''--------------------------------------Question 5 Ans-----------------------------------------'''
''' 
    The url_for() function is used in Flask for URL building. It is a built-in function that generates
a URL for a given endpoint, taking into account the current URL scheme, hostname, and port number.
    
    Here's an example Flask application that demonstrates the working of the url_for() In this example,
we define two routes: / and /welcome. The / route uses the url_for() function to generate a URL for the
welcome endpoint, which is defined by the /welcome route. The generated URL is then returned as part of
the response.

    When you run this Flask application and access the / route in your browser, you should see the
following output: 
'''
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    # Generate a URL for the 'welcome' endpoint
    welcome_url = url_for('welcome')
    return f'Welcome URL: {welcome_url}'

@app.route('/welcome')
def welcome():
    return 'Welcome to ABC Corporation'

if __name__ == '__main__':
    app.run()
