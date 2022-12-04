import asyncio
import aio_pika
import websockets

from settings import RABBIT_HOST, RABBIT_PORT, WEB_SERVER_HOST, WEB_SERVER_PORT


async def send_message(message: str) -> None:
    async with websockets.connect(
        f"ws://{WEB_SERVER_HOST}:{WEB_SERVER_PORT}"
    ) as websocket:
        await websocket.send(message)


async def process_message(
    message: aio_pika.abc.AbstractIncomingMessage,
) -> None:
    async with message.process():
        input_message = message.body.decode("utf-8")
        output_message = "".join(list(input_message)[::-1])
        await send_message(f"input: {input_message}\noutput: {output_message}\n")


async def main() -> None:
    connection = await aio_pika.connect_robust(host=RABBIT_HOST, port=RABBIT_PORT)
    queue_name = "text"
    channel = await connection.channel()
    queue = await channel.declare_queue(queue_name, auto_delete=True)
    await queue.consume(process_message)
    try:
        await asyncio.Future()
    finally:
        await connection.close()


if __name__ == "__main__":
    asyncio.run(main())
