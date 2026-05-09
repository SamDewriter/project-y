import os
import pandas as pd
from flask import Flask, request, jsonify


# Write a dummy function to simulate data processing
def routes():
    return "This is a dummy route for testing purposes."
# Create a Flask app
app = Flask(__name__)