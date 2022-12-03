import aio_pika

from .settings import RABBIT_HOST, RABBIT_PORT


async def send_message(text: str):
    connection = await aio_pika.connect_robust(
        host=RABBIT_HOST,
        port=RABBIT_PORT,
    )
    async with connection:
        routing_key = "text"
        channel = await connection.channel()
        await channel.default_exchange.publish(
            aio_pika.Message(body=text.encode()),
            routing_key=routing_key,
        )
