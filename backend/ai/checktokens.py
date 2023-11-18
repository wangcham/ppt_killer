import tiktoken

class CheckTokens:
    def get_num_tokens(self,text) -> int:
        encoding = tiktoken.get_encoding("cl100k_base")
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

        num_tokens = len(encoding.encode(text))
        print(num_tokens)
        if num_tokens >= 3500:
            return 1
        else:
            return 2
        
