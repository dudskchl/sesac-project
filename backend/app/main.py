from fastapi import FastAPI
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


responses = {
    "안녕": "안녕하세요!",
    "넌 뭐하는 애니?": "제가 뭘 어쨌다구요?",
    "내가 너 때문에 미치겠다.": "그러시던가요",
    "안녕히 계세요": "안녕히 가세요!",
}


@app.get("/chat")
async def chat(user_input: Optional[str] = None):
    if user_input is None:
        return {"message": "입력된 메시지가 없습니다."}
    return {"User": user_input, "도봉이": responses.get(user_input, "뭔 소리에요?")}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)