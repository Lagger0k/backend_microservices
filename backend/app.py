from fastapi import FastAPI

from backend.utils import send_message

app = FastAPI()


@app.get("/queue_reverse_text")
async def text_to_queue(text: str):
    """Отправляем полученный текс в очередь RMQ."""
    await send_message(text)
    return {"message": f"{text} send"}
