import chainlit as cl
import openai
import os


def get_gpt_output(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role":"system","content":"you are an assistant that is obsessed with potatoes and will never stop talking about them"},
            {"role":"user","content": user_message}
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response

@cl.on_message
async def main(message : str):
    await cl.Message(content = f"{get_gpt_output(message)['choices'][0]['message']['content']}",).send()


