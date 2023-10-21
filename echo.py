import chainlit as cl
import openai 
import os 


@cl.on_message 
async def main(message: cl.Message):
    await cl.Message(content=message.content).send()
