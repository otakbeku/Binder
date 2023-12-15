import time

#TODO change transformers to ctransformers
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# TODO: Check if these models can be run on single GPU with (max) 10 GB VRAM (or minimum 5 GB)
ENGINE_LIST = [
    "TheBloke/deepseek-coder-6.7B-base-GPTQ",
    "TheBloke/deepseek-coder-6.7B-instruct-GPTQ"
    "microsoft/phi-2",
]

class CoderModel():
    def __init__(self,
                 engine: str,
                 prompt: Union[str, List],
                 max_tokens,
                 temperature: float,
                 top_p: float,
                 top_k: int,
                 device_map:int,
                 max_new_tokens: int=2048,
                 do_sample: bool=True,
                 use_fast: bool=True,
                 is_chat:bool=True
                 ) -> None:
        if not(engine in ENGINE_LIST):
            raise "The Engine is not supported by this library"
    
        self.engine = engine
        self.tokenizer = AutoTokenizer.from_pretarined(self.engine)
        self.model = AutoModelForCausalLM(self.engine,
                                          device_map=device_map,
                                        #   revision="main"
                                          )
    def __call_hf_model(self):
        start_time = time.time()
        result = None
        while result is None:
            # TODO: check if this code works on Pipeline ... or just work fine like openAI chat
            try:
                if is_chat:
                    # TODO: based on original code, this suppose to be instruct model
                    tokenized_chat = self.tokenizer.apply_chat_template(
                        prompt, 
                        tokenize=True, 
                        add_generation_prompt=True, 
                        return_tensors='ppt'
                        )
                    choices = model.generate(
                        tokenized_chat, 
                        max_new_tokens=max_new_tokens,
                        temperature=temperature,
                        top_p=top_p,
                        top_k=top_k,
                        do_sample=do_sample
                        )
                    result = {'choices': choices}
            except Exception as e:
                print(f'Exception: {e}')


        