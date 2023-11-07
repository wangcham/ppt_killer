import traceback
from quart import request,Blueprint,jsonify
from quart_cors import cors
import service.handle_service as hs
from entities.exceptions import GetContentError,EmptyFileError


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
            return jsonify({'status':'fail','message':'接受文件失败','code':'0'})
    except EmptyFileError:
        print(traceback.format_exc())
        return jsonify({'status':'fail','message':'抛出异常'})

@getfile.route('/getques',methods=['post'])
async def getques():
    try:
        data = request.get_json()
        content = data['content']
        #编写逻辑
        if content:
            pass
        else:
            return jsonify({'status':'fail','message':'获得的内容为空'})

    except GetContentError as e:
        return jsonify({'status':'fail','message':'获得内容失败'})

    


