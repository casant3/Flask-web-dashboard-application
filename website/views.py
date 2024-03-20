from flask import Flask, Blueprint, render_template, request, redirect, url_for, send_file
from flask_sqlalchemy import SQLAlchemy
import datetime
from .models import Mega
from . import db
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import base64
from datetime import datetime
import dateutil.parser
from collections import Counter
from sqlalchemy import func

my_view = Blueprint("my_view", __name__)

@my_view.route("/")
def home():
    mega_list = Mega.query.all()
    message = request.args.get("message", None) #Get any message or success parameter from the request URL
    success = request.args.get("success", None)
    # data = Mega.query.all()

    staff_mvp_names = [mega.staff_mvp for mega in mega_list]
    if staff_mvp_names:
        common_name = Counter(staff_mvp_names).most_common(1)[0][0]
    else:
        common_name = None

    best_item = [mega.best_seller for mega in mega_list]
    if best_item:
        common_best_seller = Counter(best_item).most_common(1)[0][0]
    else:
        common_best_seller = None

    worst_item = [mega.worst_seller for mega in mega_list]
    if worst_item:
        common_worst_seller = Counter(worst_item).most_common(1)[0][0]
    else:
        common_worst_seller = None

    best_day = [mega.daily_earnings for mega in mega_list]
    if best_day:
        best_day_object = max(mega_list, key=lambda x: str(x.daily_earnings))
        best_daily_earnings = best_day_object.daily_earnings
    else:
        best_daily_earnings = None

    biggest_basket = [mega.biggest_basket for mega in mega_list]
    if biggest_basket:
        biggest_basket_object = max(mega_list, key=lambda x: str(x.biggest_basket))
        biggest_basket_earnings = biggest_basket_object.biggest_basket
    else:
        biggest_basket_earnings = None


    days = []
    daily_earnings = []

    entries = Mega.query.all()
    for entry in entries:
        # Extract day and daily_earnings from each entry
        days.append(entry.day)
        daily_earnings.append(entry.daily_earnings)
        
    highest_day_earnings = db.session.query(Mega.day, func.max(Mega.daily_earnings)).first()
    best_daily_earnings, highest_day = highest_day_earnings

    plt.figure(figsize=(8, 6))
    plt.scatter(days, daily_earnings, marker='X')
    plt.title('Daily Earnings')
    plt.xlabel('Day')
    plt.ylabel('Earnings')

    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    graph_url = base64.b64encode(img.getvalue()).decode()
    
    all_days = []
    for mega in mega_list:
        all_days.append(mega.day)

    return render_template("index.html", mega_list=mega_list, message=message, success=success, common_name = common_name, best_daily_earnings = best_daily_earnings, biggest_basket_earnings = biggest_basket_earnings, common_best_seller = common_best_seller, common_worst_seller = common_worst_seller, graph_url = graph_url, all_days=all_days, highest_day=highest_day)

@my_view.route("/add", methods=["POST"])    #allows post methods
def add():
    if request.method == 'POST':
        try:
            day = request.form.get("day")
            staff_mvp = request.form.get("staff_mvp").title()
            biggest_basket = request.form.get("biggest_basket")
            daily_earnings = request.form.get ("daily_earnings")
            best_seller = request.form.get ("best_seller").title()
            worst_seller = request.form.get ("worst_seller").title()
            existing_entry = Mega.query.filter_by(day=day).first()
            if existing_entry:
                message = "Error adding your entry. You cannot add two entries for the same day. If you wish to delete or edit an entry then go to the 'Data' page."
                return redirect(url_for("my_view.home", message=message))
            new_mega = Mega(day = day, biggest_basket = biggest_basket, staff_mvp = staff_mvp, daily_earnings = daily_earnings, best_seller = best_seller, worst_seller = worst_seller)
            db.session.add(new_mega)   #add into db
            db.session.commit() 
            success = "Entry added successfully"    #
            return redirect(url_for("my_view.home", success = success))
        except:
            message = "Error adding your entry. You cannot add two entries for the same day. If you wish to delete or edit an entry then go to the 'Data' page." # If an error occurs during adding the task, set an error message
            return redirect(url_for("my_view.home", message = message))





@my_view.route("/page2")
def page2():
    data = Mega.query.all()
    return render_template("page2.html", data = data)

@my_view.route("/page3")
def page3():
    data = Mega.query.all()
    return render_template("page3.html", data = data)

@my_view.route("/page4")
def page4():
    data = Mega.query.all()
    return render_template("page4.html", data = data)

@my_view.route("/page5")
def page5():
    data = Mega.query.all()
    return render_template("page5.html", data = data)

@my_view.route("/page6")
def page6():
    data = Mega.query.all()
    return render_template("page6.html", data = data)

@my_view.route("/page7")
def page7():
    data = Mega.query.all()
    return render_template("page7.html", data = data)

@my_view.route("/page8")
def page8():
    data = Mega.query.all()
    return render_template("page8.html", data = data)

@my_view.route("/page9")
def page9():
    data = Mega.query.all()
    return render_template("page9.html", data = data)

@my_view.route("/delete/<mega_id>", methods =["POST"])
def delete (mega_id):
    mega = Mega.query.filter_by(id=mega_id).first() # Find the todo item by its ID
    db.session.delete(mega) # Delete the todo item from the database
    db.session.commit()
    return redirect(url_for("my_view.home"))