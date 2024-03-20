from . import db
import datetime

class Mega(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(30), default = "") 
    staff_mvp = db.Column(db.String(30), unique=True) 
    biggest_basket = db.Column(db.Integer, default=0)
    daily_earnings = db.Column(db.Integer, default=0)
    best_seller = db.Column(db.String(30), default="")
    worst_seller = db.Column(db.String(30), default="")

    # priority = db.Column(db.String, default = False)
    # category = db.Column(db.String, default = False)
