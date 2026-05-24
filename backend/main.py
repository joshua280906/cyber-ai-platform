from fastapi import FastAPI
from datetime import datetime

from api.traffic import router as traffic_router
from fastapi import WebSocket
from websocket.live_stream import connect, disconnect

app = FastAPI(
    title="AI Threat Detection Platform",
    version="1.0.0",
    description="AI-Powered Threat Detection & Security Monitoring Platform"
)

# --------------------------------------------------
# ROOT ROUTE
# --------------------------------------------------

@app.get("/")
def root():

    return {
        "platform": "AI Threat Detection Platform",
        "status": "running",
        "time": str(datetime.now())
    }


# --------------------------------------------------
# HEALTH CHECK
# --------------------------------------------------

@app.get("/health")
def health_check():

    return {
        "healthy": True,
        "service": "backend"
    }


# --------------------------------------------------
# ROUTES
# --------------------------------------------------

app.include_router(
    traffic_router,
    prefix="/traffic",
    tags=["Traffic"]
)

# --------------------------------------------------
# LIVE WEBSOCKET
# --------------------------------------------------

@app.websocket("/ws/live")

async def websocket_endpoint(websocket: WebSocket):

    await connect(websocket)

    try:

        while True:

            await websocket.receive_text()

    except:

        disconnect(websocket)