import traceback
from quart import request,Blueprint,jsonify
from quart_cors import cors
import service.handle_service as hs
getfile_app = Blueprint('getfile_app',__name__)
cors(getfile_app)

@getfile_app.route('/getfile',methods=['post'])
async def getfile():
    try:
        files = await request.files
        file = files.get('file', None)
        
        if file:
            print('后端接受到文件')
            file_handler =await hs.handle_file.create(file)
            response = await file_handler.handle()
            print("进行操作,得到ppt")
            return response
        else:
            return jsonify({'status':'fail','message':'接受文件失败'})
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'status':'fail','message':'抛出异常'})


