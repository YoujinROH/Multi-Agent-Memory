from openai import OpenAI

def chat_with_gpt(user_prompt, system_prompt, model='gpt-4o-mini'):
    
    client = OpenAI()
    
    completion = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    )

    return completion.choices[0].message.content
