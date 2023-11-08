from quart import Blueprint,request,jsonify,Quart
import db

getanswer_app = Blueprint('getanswer_app',__name__)

@getanswer_app.route('/getanswer',methods=['post'])
async def getanswer():
    pass