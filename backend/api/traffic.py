from fastapi import APIRouter

from database.connection import SessionLocal
from database.crud import save_packet

from detection.threat_detector import detect_threat

from alerts.alert_manager import save_alert

from websocket.manager import broadcast

from ai.anomaly_detector import detect_anomaly

from ai.threat_scorer import calculate_threat_score

router = APIRouter()

# ---------------------------------------------------
# RECEIVE PACKETS
# ---------------------------------------------------

@router.post("/ingest")

async def ingest_packet(packet: dict):

    db = SessionLocal()

    try:

        # --------------------------------------------
        # DETECT THREATS
        # --------------------------------------------

        alerts = detect_threat(packet)

        # --------------------------------------------
        # AI ANOMALY DETECTION
        # --------------------------------------------

        ai_result = detect_anomaly(

            packet["packet_size"]
        )

        anomaly_detected = False

        if ai_result == -1:

            anomaly_detected = True

            alerts.append(

                "AI detected anomalous traffic"
            )

        # --------------------------------------------
        # AI THREAT SCORE
        # --------------------------------------------

        threat_score = calculate_threat_score(

            packet,

            anomaly_detected
        )

        print(

            f"[AI THREAT SCORE] {threat_score}"
        )

        # --------------------------------------------
        # SAVE + BROADCAST ALERTS
        # --------------------------------------------

        for alert in alerts:

            save_alert(

                db=db,

                src_ip=packet["src_ip"],

                alert_type="Threat Detection",

                severity=f"AI SCORE: {threat_score}",

                description=alert
            )

            # ----------------------------------------
            # LIVE WEBSOCKET BROADCAST
            # ----------------------------------------

            await broadcast({

                "type": "alert",

                "src_ip": packet["src_ip"],

                "message": alert,

                "threat_score": threat_score
            })

        # --------------------------------------------
        # SAVE PACKET
        # --------------------------------------------

        save_packet(db, packet)

        print("\n[PACKET SAVED]")
        print(packet)

        return {

            "status": "saved"
        }

    finally:

        db.close()