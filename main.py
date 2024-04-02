from flask import Flask, request, jsonify

# run the Flask app
app = Flask(__name__)

# define a route
# GET api
@app.route('/api', methods = ['GET'])
# define the method that will run when
# the api is called
def returnascii():
    d = {}
    # retrieve the query from the api
    input = str(request.args['query'])
    answer = str(ord(input))
    d['output'] = answer
    return d

# run the Flask app
if __name__ == "__main__":
    app.run()    