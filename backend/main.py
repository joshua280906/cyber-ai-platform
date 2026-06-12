from fastapi import FastAPI
from datetime import datetime

from api.traffic import router as traffic_router
from fastapi import WebSocket
from websocket.live_stream import connect, disconnect
from api.stats import router as stats_router
from fastapi.middleware.cors import CORSMiddleware
from api.alerts import router as alerts_router
from api.traffic_feed import router as traffic_feed_router
from api.threat_intel import router as threat_intel_router
from api.timeline import router as timeline_router

app = FastAPI(
    title="AI Threat Detection Platform",
    version="1.0.0",
    description="AI-Powered Threat Detection & Security Monitoring Platform"
)
# ---------------------------------------------------
# CORS
# ---------------------------------------------------

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
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
app.include_router(

    stats_router,

    prefix="/stats",

    tags=["Statistics"]
)
app.include_router(

    alerts_router,

    prefix="/alerts",

    tags=["Alerts"]
)
app.include_router(

    traffic_feed_router,

    prefix="/traffic",

    tags=["Traffic Feed"]
)
app.include_router(

    threat_intel_router,

    prefix="/threat-intel",

    tags=["Threat Intel"]
)
app.include_router(

    timeline_router,

    prefix="/analytics",

    tags=["Analytics"]
)

# ---------------------------------------------------
# LIVE WEBSOCKET
# ---------------------------------------------------

@app.websocket("/ws/live")

async def websocket_endpoint(websocket: WebSocket):

    await connect(websocket)

    try:

        while True:

            await websocket.receive_text()

    except:

        disconnect(websocket)