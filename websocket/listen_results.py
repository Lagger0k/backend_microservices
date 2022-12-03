import websockets
import asyncio


async def new_client_connected(
    client_socket: websockets.WebSocketClientProtocol, path: str
):
    while True:
        try:
            new_message = await client_socket.recv()
            print(new_message)
        except websockets.exceptions.ConnectionClosed as ex:
            pass


async def start_server():
    await websockets.serve(new_client_connected, "0.0.0.0", 7890)


if __name__ == "__main__":
    event_loop = asyncio.new_event_loop()
    event_loop.run_until_complete(start_server())
    event_loop.run_forever()
