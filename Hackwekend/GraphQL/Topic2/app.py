from ariadne import gql, QueryType, make_executable_schema, MutationType, graphql_sync
from flask import Flask, render_template, request, jsonify, redirect, url_for, Response
from dotenv import load_dotenv
from tinydb import TinyDB, Query
import requests
import os
import urllib
import json

# Load .env for get ENV
load_dotenv()

# Load the TinyDB
db = TinyDB("./users.json")
User = Query()

# Define function to Login and Register
def login(*_,username, password):
    user = db.search(User.username == username and User.password == password)
    if user != []:
        return True
    return False

def register_beta_user(*_,username,password):
    try:
        db.insert({'username': username, 'password': password})
        return True
    except:
        return False


# Define type definitions (schema) using SDL
type_defs = gql(
    """
    type Query {
        isAuthentication: Boolean
    }
    
    type Mutation {
        login(username: String!, password: String!): Boolean!
        register_beta_user(username: String!, password: String!): Boolean!
    }
   """
)

app = Flask(__name__)

# Initialize mutation
mutations = MutationType()
queries = QueryType()

# Define resolvers
mutations.set_field("login", login)
mutations.set_field("register_beta_user", register_beta_user)
schema = make_executable_schema(type_defs, [queries, mutations])

# Define a route for Flask
@app.route("/", methods=['GET'])
def index():
    return render_template('login.html')

@app.route("/graphql", methods=['POST'])
def graphql():
    try:
        data = request.get_json()
    except:
        data = json.loads(request.args.get('query'))
    success, result = graphql_sync(schema, data, context_value={"request": request}, introspection = True)
    status_code = 200 if success else 400
    if "login" in result['data']:
        if result['data']['login']:
            return render_template("gatcha.html", flag=os.getenv("FLAG"))
        else:
            return render_template("login.html", message="Your username or password is wrong")

    if "register_beta_user" in result['data']:
        if result['data']['register_beta_user']:
            return render_template("login.html", message="Successfully registered your account")
        if result['data']['register_beta_user']:
            return render_template("login.html", message="Unsuccessfully registered your account")

    if "__schema" in result['data']:
        return jsonify(result), status_code

@app.route("/handle_login", methods=['POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']

    query = {"query": "mutation {\n    login(username: \"" + str(username) + "\", password: \"" + str(password) + "\")\n}"}
    
    return redirect("/graphql?query=" + json.dumps(query), 307)
    
app.run(host="0.0.0.0", port="8888", debug=False)