import openai
import pdb
import os


openai.api_key ="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"


chat_history = []
while True:
  prompt= input("***Enter a prompt: ")
  if prompt == "exit":
     break
  else:
    chat_history.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = chat_history,
        stream = True,
        max_tokens=150,

    )

    collected_messages=[]
    fully_reply_content = ''
    for chunk in response:
        chunk_message = chunk["choices"][0]["delta"].get('content','')
        collected_messages.append(chunk_message)
        fully_reply_content=''.join(collected_messages)
        print(fully_reply_content)
        print("\033[H\033[J", end="")

    chat_history.append({"role": "assistant", "content": fully_reply_content})
    
    print("-----------Historial-----------")
    for item in chat_history:
       if item["role"] == "assistant":
          print(f"GPT: {item['content']}")
       else:
          print(f"GPT: {item['content']}")
          
    print(f"GPT: {fully_reply_content}")
    
    
