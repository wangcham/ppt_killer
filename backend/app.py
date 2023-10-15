from quart import  Quart,request,Blueprint
from route.getfile import getfile_app
app = Quart(__name__)
app.register_blueprint(getfile_app)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)