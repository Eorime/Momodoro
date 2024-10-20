import requests

from flask import redirect, session, render_template
from functools import wraps


def login_required(f): #A decorator is a fn that takes another fn and extends or alters its behavior without modifying the original fn
    @wraps(f) #preserves the original functions metadata when wrapped by another function
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function

#this decorator is typically applied to flask routes where you want to restrict access to authenticated users
