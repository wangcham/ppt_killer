import os
from typing import IO
from . import methods
from  quart import jsonify

ALLOWED_EXTENSIONS = {'ppt','pptx'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class handle_file:
    def __init__(self,file:IO):
        self.file = file     

    async def checkext(self):
        #在这里检查文件格式
        if not allowed_file(self.file.filename):
            return jsonify({'status':'fail','message':'不是允许的文件类型'})            

        ext = os.path.splitext(self.file.filename)[1]
        print('接受到的文件拓展名:'+ext)
        self.ext = ext

    async def handle(self):
        if self.file:
            print("文件存在")

        method = methods.GetText(self.file)
        
        if(self.ext == '.pptx'):
            print("进入pptx文件使用")
            result =await method.pptx_method()
        elif(self.ext == '.ppt'):
            result =await method.ppt_method()

        return result


    @classmethod
    async def create(cls,file:IO):
        instance = cls(file)
        await instance.checkext()
        return instance
           
        






    




