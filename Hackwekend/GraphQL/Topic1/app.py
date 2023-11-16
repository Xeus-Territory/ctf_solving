from flask import Flask, request, jsonify, render_template
from graph import schema
from ariadne import graphql_sync

# initialize flask app
app = Flask(__name__)

@app.route("/", methods=['GET'])
def landing_page():
    return render_template('index.html')

# Create a GraphQL Playground UI for the GraphQL schema
@app.route("/graphql", methods=["GET"])
def graphql_playground():
   # Playground accepts GET requests only.
   # If you wanted to support POST you'd have to
   # change the method to POST and set the content
   # type header to application/graphql
   return render_template("minimal.html")

# Create a GraphQL endpoint for executing GraphQL queries
@app.route("/graphql", methods=["POST"])
def graphql_server():
   data = request.get_json()
   success, result = graphql_sync(schema, data, context_value={"request": request})
   status_code = 200 if success else 400
   return jsonify(result), status_code

# Run the app
if __name__ == "__main__":
   app.run(host="0.0.0.0", port="9999", debug=False)