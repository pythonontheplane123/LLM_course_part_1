import chainlit as cl
import openai 
import os 


@cl.on_message 
async def main(message: cl.Message):

    response = openai.ChatCompletion.create(
        model = "gpt-4", 
        messages = [
            {"role":"system", "content":"You are helpful assistant who obsessed with Thai Bangkaew dog."}, 
            {"role":"user", "content": message.content}, 
        ], 
        temperature = 1, 
    )
    await cl.Message(content=response['choices'][0]['message']['content']).send()
