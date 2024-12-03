import argparse
from openai import OpenAI

client = OpenAI()

parser = argparse.ArgumentParser(
                    prog='OpenAI text generation',
                    description='This program sends input text to OpenAI and returns the completion.')
parser.add_argument('user_content')
parser.add_argument('-system_content', default="You are a helpful assistant.")

args = parser.parse_args()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": args.system_content},
        {"role": "user","content": args.user_content}
    ]
)

print(completion.choices[0].message)
