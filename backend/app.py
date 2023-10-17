from quart import send_from_directory
from quart import  Quart,request,Blueprint
from route.getfile import getfile_app
import os
app = Quart(__name__,static_folder='./dist')
app.register_blueprint(getfile_app)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)