import g4f


async def generate_answer(prompt):
    provider = g4f.Provider.Liaobots
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.gpt_4_0613,
            messages=[
                {"role": "system", "content": "Напиши суть сообщения в краткой форме, обязательно на русском"},

                {"role": "user", "content": prompt}
            ],
            provider=provider,
            timeout=10
        )
    except Exception as e:
        print(f"{provider.__name__}: ERROR", e)
        return ""

    return response
