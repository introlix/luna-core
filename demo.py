from llama_cpp import Llama

llm = Llama.from_pretrained(
    repo_id="satyam998/Luna_3.2_3B_GGUF",
    filename="Luna_3.2-Q4_K_M.gguf",
)

output = llm.create_chat_completion(
    messages=[
        {"role": "system", "content": "You are Luna. Your task is to give correct answers to science questions."},
        {"role": "user", "content": "What is Newton's third law of motion?"}
    ],
    stream=True
)

for chunk in output:
    delta = chunk['choices'][0]['delta']
    if 'role' in delta:
        print(delta['role'], end=': ', flush=True)  # Flush ensures immediate output
    elif 'content' in delta:
        print(delta['content'], end='', flush=True)  # Flush ensures immediate output
