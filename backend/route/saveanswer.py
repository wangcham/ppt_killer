from quart import Quart,request,jsonify,Blueprint
from quart_cors import cors
import db
from entities.exceptions import SqliteError
saveanswer_app = Blueprint('saveanswer_app',__name__)

cors(saveanswer_app)

@saveanswer_app.route('/saveanswer',methods=['post'])
async def saveanswer():
    data = request.get_json()
    content = data['content']
    type = data['type']
    token = data['token']

    sql1 = "select * from info where token = ?"
    database = db.database()
    result = database.execute(sql1,(token,))
    if not result:
        return jsonify({'code':'1'})
    else:
        sql2 = "INSERT INTO info (token,type,content) VALUES (?,?,?)"
        try:
            result = database.execute(sql2,(token,type,content,))
            return jsonify({'status':'success','code':'3'})
        except SqliteError:
            print("数据库插入操作失败")
            return jsonify({'status':'fail','message':'数据库插入操作失败','code':'2'})