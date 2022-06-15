from unittest import result
from flask_app.config.mysqlconnection import MySQLConnection,connectToMySQL
from flask_app import app


class Ninga:
    DB='dojo'

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.dojo_id=data['dojo_id']


    @classmethod
    def create_new_ninga(cls,data):
        # DOJO_ID HERE IN QUERY REPRESENTS THE VALUE OF SELECT INSIDE NINGA HTML WHICH IS THE DOJO ID value=dojo_id
        query="""INSERT INTO ningas (first_name,last_name,age,dojo_id)
        VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s)
        ;"""
        result=connectToMySQL(cls.DB).query_db(query,data)
        print("&&&&&&&&",result)
        return result

    #read get all ningas
    @classmethod
    def get_all_ningas(cls):
        query="""
        SELECT * FROM ningas
        ;"""
        result=connectToMySQL(cls.DB).query_db(query)
        ningas=[]
        for ninga in result:
            ningas.append(cls(ninga))
        return ningas
