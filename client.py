import asyncio
import websockets


async def connect_to_server():
    # Connect to the server
    async with websockets.connect("ws://localhost:8765") as websocket:
        # Receive the greeting from the server
        greeting = await websocket.recv()
        print(f"Server says: {greeting}")

        while True:
            # Get user input
            message = input("Enter a message: ")

            # Send the message to the server
            await websocket.send(message)

            # Wait for a response from the server
            response = await websocket.recv()
            print(f"server says: {response}")


asyncio.get_event_loop().run_until_complete(connect_to_server())
