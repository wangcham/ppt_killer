import tiktoken

class CheckTokens:
    def get_num_tokens(text) -> int:
        encoding = tiktoken.get_encoding("cl100k_base")
        encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

        num_tokens = len(encoding.encode(text))
        if num_tokens >= 4095:
            return 1
        else:
            return 2
        
