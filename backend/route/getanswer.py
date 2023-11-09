from quart import Blueprint,request,jsonify,Quart
from quart_cors import cors
import db
from entities.exceptions import SqliteError

getanswer_app = Blueprint('getanswer_app',__name__)
cors(getanswer_app)
@getanswer_app.route('/olddata',methods=['post'])
async def olddata():
    data = await request.get_json()
    token = data['content']
    try:
        database = db.database()
        sql = "select type,content from info where token = ?"
        results = database.execute(sql,(token,))

        if not results:
            return jsonify({'status':'fail','message':'未查询到符合该密钥的结果'})
        else:
            data = []
            for result in results:
                type = result[0]
                content = result[1]

                item = {'type':type,'content':content}
                data.append(item)

            return jsonify(data)
    except SqliteError:
        return jsonify({'status':'fail','message':'数据库操作失败'})