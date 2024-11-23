from llama_cpp import Llama

model_path = "satyam998/Luna_3.2_3B_GGUF"

llm = Llama.from_pretrained(
    repo_id="satyam998/Luna_3.2_3B_GGUF",
    filename="Luna_3.2-Q4_K_M.gguf",
)

output = llm.create_chat_completion(
    messages=[
        { "role": "system", "content": f"You are luna. Your task is to give correct answers to science questions. Don't make any answer that you don't know? And use your current knowleged to give answer." },
        {
            "role": "user",
            "content": "What is different between Uniform and non uniform acceleration?"
        }
    ],
    stream=True
)

for chunk in output:
    delta = chunk['choices'][0]['delta']
    if 'role' in delta:
        print(delta['role'], end=': ')
    elif 'content' in delta:
        print(delta['content'], end='')