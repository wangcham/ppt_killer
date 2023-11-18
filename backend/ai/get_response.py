from . import checktokens
import os
import traceback
import openai
from quart import jsonify
from entities.exceptions import ChatgptGenerateError
from . import setaiconfig
class response:
    def __init__(self, text):
        self.text = text

    async def complete(self):
        try:
           
            setaiconfig.setconfig()
            
            check = checktokens.CheckTokens()
            type = check.get_num_tokens(self.text)
            if type == 1:
                used_model = "gpt-3.5-turbo-16k"
                print("调用gpt16k")
            if type == 2:
                used_model = "gpt-3.5-turbo"
                print("调用gpt3.5turbo接口")

            completion = openai.ChatCompletion.create(
                model=used_model,
                messages=[
                    {"role": "system", "content": "你是一个帮助人们总结内容的助手"},
                    {"role": "user", "content": "请给我总结这些内容，我给你的文本的内容是乱的，请你认真思考一下，把他整理清楚，给出我中文的回复，不允许省略回复，以分层标题等的形式生成大纲，另外，生成的回答必须是markdown格式,记得写成垂直方向的换行，也就是需要你加换行的标志，让他形式好看一点，并且请翻译成中文：" + self.text}
                ]
            )
            self.result = completion.choices[0].message['content']
            print(self.result)
            return jsonify({'status':'success','result':self.result})
        except Exception as e:
            print(traceback.format_exc())
            self.result = "#### chatgpt响应异常,异常是" + str(e) + "请稍后使用网站~"
            return jsonify({'status':'fail','result':self.result})

    async def get_generated_answer(self,ques_text):

        setaiconfig.setconfig()

        check = checktokens.CheckTokens()
        type = check.get_num_tokens(ques_text)

        if type == 1:
            used_model = "gpt-3.5-turbo-16k"
        if type == 2:
            used_model = "gpt-3.5-turbo"
        
        try:
            completion = openai.ChatCompletion.create(
                model=used_model,
                messages=[
                    {"role": "system", "content": "你是一个帮助人们理解PPT的助手"},
                    {"role": "user", "content": "请将这些杂乱的文本整理清楚，然后依据这些内容生成大约二三十道问题，并且在最后给出答案，然后必须以markdown的形式发送给我，文本内容是：" + ques_text}
                ]
            )
            result = completion.choices[0].message['content']
            return jsonify({'status':'success','result':result})
        except ChatgptGenerateError:
            return jsonify({'status':'fail','message':'chatgpt生成内容失败'})