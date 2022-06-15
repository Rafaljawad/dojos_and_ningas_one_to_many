from flask_app.config.mysqlconnection import MySQLConnection,connectToMySQL
from flask_app import app
from flask_app.models import ninga
class Dojo:
    #create a class attribute for database name to use it later in our class methods (instead of writing a whole database name we make it short when we define in as aclass attribute)
    DB='dojo'
#create dojo constructor 
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ningas=[]# this one for associate Ninga class with Dojo class(dojo has many (list)of ningas)


    #running crud
    #model create
    #create new dojo by using query (insert) and the values by using prepared statemant
    @classmethod
    def create_new_dojo(cls,data):
        query="""INSERT INTO dojos (name)
        VALUES (%(name)s)
        ;"""
        result=connectToMySQL(cls.DB).query_db(query,data)#this will connect to db and insert the values in data base table
        # print("&&&&&&&&",result)#for test what output will get
        return result

    #model read
    #here will create method for getting all the dojos from the table in db and in this case we do not need data to pass in because we need all of them
    #using select * query will get them all
    @classmethod
    def get_all_dojos(cls):
        query="""
       SELECT * FROM dojos
        ;"""
        result=connectToMySQL(cls.DB).query_db(query)# this will return a list of dictionaries 
        # print("^^^^^^^^^^^^^^^^",result)
        dojos=[]# create an empty list to create instances of users and append them here to use our methods on them
        for dojo in result:# this means each row in result (each row of dictionary)
            dojos.append(cls(dojo))# append to dojos empty list dojo wich is the dictionary with keys and values and the cls here for creating instance of this boject so go to dojo class and pass all the keys and valuse and append them to dojos list and return it

        print("^^^^^^^^^^^^^^^^",dojos)
        return dojos# after taking all the dictionaries and creating these instances so return the list of these instances to use them later


    #model get on dojo by using spescific id .
    @classmethod
    def get_dojo_by_id(cls,id):# we need the id and we get this id from the data dictionary
        data={
            "id":id
        }
        query="SELECT * FROM users WHERE id=(%(id)s);"
        result=connectToMySQL(cls.DB).query_db(query,data)
        # print("&&&&&&&&&&&&&&&&&&&&",result)
        return cls(result[0])# we need the first row 

    #get one dojo with many ninjas . here we will get all the ninga in spesfic dojo and we can not do that without using join 
    @classmethod
    def get_dojo_that_has_ninga(cls,id):
        data={
            "id":id
        }
        query="""SELECT * FROM dojos
        LEFT JOIN 
        ningas
        ON dojos.id=ningas.dojo_id
        WHERE dojos.id=(%(id)s)
        ;"""
        result=connectToMySQL(cls.DB).query_db(query,data)# this will return a long list of dictionaries .this will give us just the dojo attributes and to get the ningas as well will create a loop and create data 
        print("&&&&&&&&&&&&&&&&&&&&",result)
        this_dojo= cls(result[0])#
        for this_ninga in result:#this ninga here means the dictonary which has the dojos key plus ningas key but we have just dojos instances that we made using Dojo class
            #and to create ningas instances we need data to pass them to Ninga class and get the values to append them together with dojos instances.below are the data to create ninga instances:
            data={
                'first_name':this_ninga['first_name'],
                'last_name':this_ninga['last_name'],
                'age':this_ninga['age'],
                'id':this_ninga['ningas.id'],# here we have to make sure this id is for ninga thats why we wrote ningas.id and same thing with created at and updated at
                'created_at':this_ninga['ningas.created_at'],
                'updated_at':this_ninga['ningas.updated_at']
            }
            this_dojo.ningas.append(ninga.Ninga(data))# after creating ningas instances so we need to aapend them to ningas list in Dojo class self.ningas=[]
        return this_dojo
