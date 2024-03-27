from fastapi import FastAPI
from pydantic import BaseModel
from chat_gpt import generate_answer

app = FastAPI()


class Prompt(BaseModel):
    prompt: str


@app.post("/prompt")
async def handle_prompt(prompt: Prompt):
    response = await generate_answer(prompt.prompt)
    return response
