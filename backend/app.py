from flask import Flask
from flask_restful import Api, Resource, reqparse
import psycopg2
from config import config

app = Flask(__name__)
api = Api(app)

users = [
     {
         "name": "Nicholas",
         "age": 42,
         "occupation": "Network Engineer"
     },
     {
         "name": "Elvin",
         "age": 32,
         "occupation": "Doctor"
     },
     {
         "name": "Jass",
         "age": 22,
         "occupation": "Web Developer"
     }
 ]


def get_vendors(name):
    """ query data from the vendors table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT array_to_json(array_agg(row_to_json(users))) FROM users where name = %1", name)
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()
        user = row
        while row is not None:
            row = cur.fetchone()
        cur.close()
        return user
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

class User(Resource):
     def get(self, name):
         dbuser = get_vendors(name)
         for user in dbuser:
             if(name == user["name"]):
                 return user, 200
         return "User not found", 404

     def post(self, name):
         parser = reqparse.RequestParser()
         parser.add_argument("age")
         parser.add_argument("occupation")
         args = parser.parse_args()

         for user in users:
             if(name == user["name"]):
                 return "User with name {} already exists".format(name), 400

         user = {
             "name": name,
             "age": args["age"],
             "occupation": args["occupation"]
         }
         users.append(user)
         return user, 201

     def put(self, name):
         parser = reqparse.RequestParser()
         parser.add_argument("age")
         parser.add_argument("occupation")
         args = parser.parse_args()

         for user in users:
             if(name == user["name"]):
                 user["age"] = args["age"]
                 user["occupation"] = args["occupation"]
                 return user, 200

         user = {
             "name": name,
             "age": args["age"],
             "occupation": args["occupation"]
         }
         users.append(user)
         return user, 201

     def delete(self, name):
         global users
         users = [user for user in users if user["name"] != name]
         return "{} is deleted.".format(name), 200

api.add_resource(User, "/user/<string:name>")

app.run(debug=True)
