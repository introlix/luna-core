from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from llama_cpp import Llama

router = APIRouter()

# Load the model (ensure the repo_id and filename are correct)
llm = Llama.from_pretrained(
    repo_id="satyam998/Luna_3.2_3B_GGUF",
    filename="Luna_3.2-Q4_K_M.gguf",
)

# Streaming generator function
async def generate_stream(query: str):
    try:
        # Use `stream=True` to enable token-by-token generation
        result = llm.create_chat_completion(
            messages=[
                {"role": "system", "content": "You are Luna. Your task is to give correct answers to science questions. Use your current knowledge to give answers."},
                {"role": "user", "content": query}
            ],
            stream=True  # Streaming mode enabled
        )

        # Iterate over streamed tokens
        for token in result:
            if "choices" in token:
                for choice in token["choices"]:
                    if "delta" in choice and "content" in choice["delta"]:
                        # Yield the generated token
                        yield choice["delta"]["content"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during streaming: {str(e)}")

# FastAPI endpoint for streaming
@router.get("/luna")
async def root(query: str):
    try:
        result = generate_stream(query)
        return StreamingResponse(
            result,
            media_type="text/event-stream"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing the query: {str(e)}")
