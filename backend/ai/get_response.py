
import os
import traceback
import openai
import config
class response:
    def __init__(self, text):
        self.text = ""
        self.text = text

    async def complete(self):
        try:
            openai.proxy = "http://127.0.0.1:7890"
            openai.api_key = config.openai_api_key
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-16k",
                messages=[
                    {"role": "system", "content": "你是一个助手"},
                    {"role": "user", "content": "请给我总结这些内容，我给你的文本的内容是乱的，请你认真思考一下，把他整理清楚，给出我中文的回复，以大小标题等的形式生成大纲，另外，生成的回答必须是markdown格式,记得写成垂直方向的换行，也就是需要你加换行的标志，让他形式好看一点，并且请翻译成中文：" + self.text}
                ]
            )
            self.result = completion.choices[0].message['content']
            print(self.result)
            return self.result
        except Exception as e:
            print(traceback.format_exc())
            self.result = "chatgpt响应异常,异常是" + str(e) + "，请稍后使用网站~"
            return self.result

        
