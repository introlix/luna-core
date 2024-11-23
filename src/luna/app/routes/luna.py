from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from llama_cpp import Llama

router = APIRouter()

llm = Llama.from_pretrained(
    repo_id="satyam998/Luna_3.2_3B_GGUF",
    filename="Luna_3.2-Q4_K_M.gguf",
)

@router.post("/luna")
async def root(query: str):
    try:
        response =  []
        result = llm.create_chat_completion(
            messages=[
                {"role": "system", "content": "You are Luna. Your task is to give correct answers to science questions. Use your current knowledge to give answers."},
                {"role": "user", "content": query}
                
            ],
            stream=False
            
        )
        if 'choices' in result:
            for choice in result['choices']:
                # Extract the content from the message
                if 'message' in choice and 'content' in choice['message']:
                    response.append(choice['message']['content'])
                    
                    return {"response": response[0]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing the query: {str(e)}")
