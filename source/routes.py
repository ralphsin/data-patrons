#!/usr/bin/env python
# -*- coding: utf-8 -*-

# source/routes.py

"""This module holds all the different URLs that the application implements."""

__author__ = "Rakesh Singh"
__copyright__ = "Copyright 2023, Project Magnetar"
__version__ = "1.0"
__maintainer__ = "Rakesh Singh"
__email__ = "support@datapatrons.com"
__status__ = "Production"


# Third party library
from flask import render_template

# Custom library
from source import app

# Defining the decorators, which binds the URLs "/" and "/home" to this function
@app.route("/")
@app.route("/home")
def index():
    """
    summary: This function captures the web browser requests for either of these two URLs and going to
    pass the index.html page as return value to the browser as a response.

    Returns:
        html: index.html page from templates directory
    """
    return render_template('index.html')

# Defining the decorator, which binds the URL "/blog" to this function
@app.route("/blog")
def blog():
    """
    summary: This function captures the web browser requests for the URL and going to pass the blog.html 
    page as return value to the browser as a response.

    Returns:
        html: blog.html page from templates directory
    """
    user = {"username": "Ayaan"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('blog.html', title="Blog", user=user, posts=posts)

# Defining the decorators, which binds the URL "/courses" to this function
@app.route("/courses")
def courses():
    """
    summary: This function captures the web browser requests for the URL and going to pass the courses.html 
    page as return value to the browser as a response.

    Returns:
        html: courses.html page from templates directory
    """
    return render_template('courses.html', title="Courses")

# Defining the decorators, which binds the URL "/about" to this function
@app.route("/about")
def about():
    """
    summary: This function captures the web browser requests for the URL and going to pass the about.html 
    page as return value to the browser as a response.

    Returns:
        html: about.html page from templates directory
    """
    return render_template('about.html', title="About")
