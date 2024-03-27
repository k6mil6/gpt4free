from aiohttp import web
from chat_gpt import generate_answer


async def handle_prompt(request):
    data = await request.json()
    prompt = data.get('prompt', '')
    response = await generate_answer(prompt)
    return web.Response(text=response)



