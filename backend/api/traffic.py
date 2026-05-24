from fastapi import APIRouter

from database.connection import SessionLocal
from database.crud import save_packet
from detection.threat_detector import detect_threat
from alerts.alert_manager import save_alert


router = APIRouter()

# ---------------------------------------------------
# RECEIVE PACKETS
# ---------------------------------------------------

@router.post("/ingest")

def ingest_packet(packet: dict):

    db = SessionLocal()

    try:
        alerts = detect_threat(packet)
        for alert in alerts:
            save_alert(

        db=db,

        src_ip=packet["src_ip"],

        alert_type="Threat Detection",

        severity="HIGH",

        description=alert
    )
            

        save_packet(db, packet)

        print("\n[PACKET SAVED]")
        print(packet)

        return {
            "status": "saved"
        }

    finally:

        db.close()