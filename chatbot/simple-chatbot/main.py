import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    # User ka input message retrieve karo
    user_message = message.content
    
    # Response generate karo
    response = f"You said: {user_message}"
    
    # Response ko user ko bhejo
    await cl.Message(content=response).send()

if __name__ == "__main__":
    cl.run()

