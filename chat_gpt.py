import g4f


async def generate_answer(prompt):
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.gpt_4,
            messages=[
                {"role": "system", "content": "Напиши суть сообщения в краткой форме, обязательно на русском"},
                {"role": "user", "content": prompt}
            ],
            provider=g4f.Provider.GeekGpt,
            timeout=10
        )
    except Exception as e:
        print(f"{g4f.Provider.GeekGpt.__name__}: ERROR", e)
        return ""

    return response
