from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("rd_sk_prod_WN_QTfK_RPaUfmMez4vk6OT-c1J0q0J2"),
    base_url="https://api.rodiumai.io/v1",
)

response = client.chat.completions.create(
    model="anthropic/claude-sonnet-5-5",
    messages=[{"role": "user", "content": "COmment je peux me faire des sous en moin de 50jours maximum"}],
)

print(response.choices[0].message.content)
