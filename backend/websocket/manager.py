from fastapi import WebSocket

# ---------------------------------------------------
# ACTIVE CONNECTIONS
# ---------------------------------------------------

active_connections = []

# ---------------------------------------------------
# CONNECT CLIENT
# ---------------------------------------------------

async def connect(websocket: WebSocket):

    await websocket.accept()

    active_connections.append(websocket)

# ---------------------------------------------------
# DISCONNECT CLIENT
# ---------------------------------------------------

def disconnect(websocket: WebSocket):

    active_connections.remove(websocket)

# ---------------------------------------------------
# BROADCAST MESSAGE
# ---------------------------------------------------

async def broadcast(message):

    for connection in active_connections:

        await connection.send_json(message)