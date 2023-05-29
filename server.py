import asyncio
import websockets

# Store all connected clients
connected_clients = set()


# Define the server's behavior when a client connects
async def handle_client(websocket, path):
    # Add the client to the set of connected clients
    connected_clients.add(websocket)

    try:
        # Send a greeting to the client
        await websocket.send("Welcome to the server!")

        # Keep the connection open to receive messages from the client
        async for message in websocket:
            # Process the received message
            print(f"Received message from client: {message}")

            # Send the message to all connected clients
            await broadcast_message(message)
    except websockets.exceptions.ConnectionClosedError:
        # Remove the client from the set of connected clients
        connected_clients.remove(websocket)
        print("Client disconnected")


# Broadcast a message to all connected clients
async def broadcast_message(message):
    for client in connected_clients:
        await client.send(message)


# Start the server
start_server = websockets.serve(handle_client, "localhost", 8765)

# Run the server indefinitely
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
