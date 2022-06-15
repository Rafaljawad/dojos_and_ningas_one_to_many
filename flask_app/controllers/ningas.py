from flask_app import app
from flask import render_template,redirect,request,session, flash
from flask_app.models import ninga
from flask_app.models import dojo

@app.route('/ningas')
def ninga_form():
    all_dojos=dojo.Dojo.get_all_dojos()
    return render_template('new_ninga.html',dojos=all_dojos)


@app.route('/create/ninga',methods=['POST'])
def create_ninga():
#     I can either write data and rwquest things from form or just pass the data to method by usinf request.form
#   1-first way as a refrence  
#  # data={
    #     'dojo_id':request.form['dojo_id'],
    #     'first_name':request.form['first_name'],
    #     'last_name':request.form['last_name'],
    #     'age':request.form['age']
    # }
    #second way
    ninga.Ninga.create_new_ninga(request.form)# take all the names from form and pass them to create new ninga method in Ninga class
    return redirect ('/dojos')
    # print("mmmmmmmmmmmmmmmm",dojo.Dojo.create_new_dojo(data))
    # return render_template('index2.html',all_ninga=  ninga.Ninga.create_new_ninga(data))


