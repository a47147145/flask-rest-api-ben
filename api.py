from tkinter.font import names
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI']='sqlite://sqlite.db'
db =SQLAlchemy(app)


dos = {
   1: {"name": "Ben", "gender": "M"},
  2: {"name": "Ivana", "gender": "F"},
   3: {"name": "Vincent", "gender": "M"}
}

task_post_args = reqparse.RequestParser()
task_post_args.add_argument("name", type=str, help="it is required", required=True )
task_post_args.add_argument("gender", type=str, help="it is required", required=True )

task_update_args = reqparse.RequestParser()
task_update_args.add_argument("name", type=str)
task_update_args.add_argument("gender", type=str)

resource_fields={
    'id': fields.Integer,
    'name': fields.String,
    'gender': fields.String,

}

#class HelloWorld(Resource):
#    def get(self):
#        return{'data':'Hello World!'}


#class HelloName(Resource):
#    def get(self, name):
#       return{'data':'Hello World, {}'.format(name)}


class Do(Resource):
   
    def get(self, do_id):
      
        return dos[do_id]

    
    def post(self, do_id):
        args = task_post_args.parse_args()
      

        if do_id in dos:
            abort(409, "ID is already taken")
        dos[do_id]={"name": args["name"], "gender": args["gender"]}

  
    def put(self, do_id):
        args = task_update_args.parse_args()


        if do_id not in dos:
           abort(404, message="DNE, cant update")
        if args['name']:
            dos[do_id]['name']=args['name']
        if args['gender']:
            dos[do_id]['gender']=args['gender']

    def delete(self, do_id):
       

        del dos[do_id]
        return dos

class DoList(Resource):
    def get(self):
       
        return dos

#api.add_resource(HelloWorld, '/hellow')
#api.add_resource(HelloName, '/hello/<string:name>')
api.add_resource(Do, '/dos/<int:do_id>')
api.add_resource(DoList, '/dos')

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello!</h1>"

@app.route("/test1", methods=['GET'])
def test():
    return "this is for testing"

@app.route("/data1", methods=['POST','GET'])
def data1():
    req = request.get_json()
    print(type(req))
    print(req)
    return "json", 200


app.run()

