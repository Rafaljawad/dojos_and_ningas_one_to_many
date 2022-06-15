from flask_app import app
from flask import render_template,redirect,request,session, flash
from flask_app.models import dojo
from flask_app.models import ninga

#home page which has new dojo and all dojos
@app.route('/dojos')
def index():
    return render_template('new_dojo.html',all_dojos=dojo.Dojo.get_all_dojos())

#this route for creating new dojo and the data coming from filling the form in new_dojo.html
@app.route('/create/dojo',methods=['POST'])
def create_dojo():
    data={
        'name':request.form['name']
    }
    dojo.Dojo.create_new_dojo(data)#pass this data to create new dojo method in dojo.py that will pass the data into Dojo class and use insert query for these data
    # print("mmmmmmmmmmmmmmmm",dojo.Dojo.create_new_dojo(data))
    return redirect('/dojos')

#this route for create single dojo by id to display it and get how many ningas in each dojo later
@app.route('/dojo/<int:id>')
def get_ninga_in_dojo(id):
    single_dojo=dojo.Dojo.get_dojo_that_has_ninga(id)
    # ninga_in_dojo=ninga.Ninga.get
    print("****************",single_dojo)
    return render_template ('all_ningas_in_dojo.html',single_dojo=single_dojo)




