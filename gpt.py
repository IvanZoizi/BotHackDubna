from openai import OpenAI
from config import *


def gpt_request(message_user, promt):
    client = OpenAI(
        api_key='sk-381QmklNWpztqYYST3rcxoE0gpwNoHpP',
        base_url="https://api.proxyapi.ru/openai/v1",
    )
    #
    # df = pd.read_excel('./files/question.xlsx')
    # text = ''
    # num = 1
    # for question, url in df.values:
    #     text += f'{num}. {question} - {url}\n'
    #     num += 1

    chat_completion = client.chat.completions.create(
        model="gpt-4-turbo", messages=[{"role": "user", "content": f"""Ты бот ГосУслуг, ты должен помогать людям
{promt}\n{message_user}"""}]
    )
    return chat_completion.choices[0].message.content


if __name__ == '__main__':
    print(gpt_request('Треш'))