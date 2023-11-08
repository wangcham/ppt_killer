from quart import Blueprint,request,jsonify,Quart
import db

getanswer_app = Quart('getanswer_app',__name__)

@getanswer_app.route('/getanswer',methods=['post'])
def getanswer():
    pass