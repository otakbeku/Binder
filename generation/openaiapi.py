 
# # TODO: Fix this module
# def _call_openai_api(
#             self,
#             engine: str,
#             prompt: Union[str, List],
#             max_tokens,
#             temperature: float,
#             top_p: float,
#             n: int,
#             stop: List[str],
#             is_chat=True
#     ):
#         start_time = time.time()
#         result = None
#         while result is None:
#             try:
#                 key = self.keys[self.current_key_id]
#                 self.current_key_id = (self.current_key_id + 1) % len(self.keys)
#                 print(f"Using openai api key: {key}")

#                 if is_chat:
#                     choices = []
#                     if isinstance(prompt, str):
#                         prompt = [prompt]
#                     for prompt_item in prompt:
#                         re = openai.ChatCompletion.create(
#                             model=engine,
#                             messages=[
#                                 {"role": "system",
#                                  "content": "I will give you some x-y examples followed by a x, you need to give me the y, and no other content."},
#                                 {"role": "user", "content": prompt_item},
#                             ],
#                             api_key=key,
#                             max_tokens=max_tokens,
#                             temperature=temperature,
#                             top_p=top_p,
#                             n=n,
#                             stop=stop,
#                         )
#                         choices += re["choices"]
#                     result = {"choices": choices}
#                     print('Openai api inference time:', time.time() - start_time)
#                     return result

#                 else:
#                     choices = []
#                     if isinstance(prompt, str):
#                         prompt = [prompt]
#                     for prompt_item in prompt:
#                         re = openai.Completion.create(
#                             engine=engine,
#                             prompt=prompt_item,
#                             api_key=key,
#                             max_tokens=max_tokens,
#                             temperature=temperature,
#                             top_p=top_p,
#                             n=n,
#                             stop=stop,
#                             logprobs=1
#                         )
#                         choices += re["choices"]
#                     result = {"choices": choices}
#                     print('Openai api inference time:', time.time() - start_time)
#                     return result
#             except openai.error.InvalidRequestError as e:
#                 # fixme: hardcoded, fix when refactoring
#                 if "This model's maximum context length is" in str(e):
#                     print(e)
#                     print("Set a place holder, and skip this example")
#                     result = {"choices": [{"message": {"content": "PLACEHOLDER"}}]} if is_chat \
#                         else {"choices": [{"text": "PLACEHOLDER"}]}
#                     print('Openai api inference time:', time.time() - start_time)
#                 else:
#                     print(e, 'Retry.')
#                     time.sleep(3)
#             except Exception as e:
#                 print(e, 'Retry.')
#                 time.sleep(3)