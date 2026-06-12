from fastapi import APIRouter

from database.connection import SessionLocal
from database.crud import save_packet

from detection.threat_detector import detect_threat

from alerts.alert_manager import save_alert

from websocket.manager import broadcast

from ai.anomaly_detector import detect_anomaly
from ai.threat_scorer import calculate_threat_score

from threat_intel.geoip_lookup import lookup_ip
from threat_intel.blacklist import is_blacklisted

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
        # BLACKLIST DETECTION
        # --------------------------------------------

        blacklisted = False

        if is_blacklisted(packet["src_ip"]):

            blacklisted = True

            alerts.append(
                "Blacklisted malicious IP detected"
            )

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
            anomaly_detected,
            blacklisted
        )

        print(
            f"[AI THREAT SCORE] {threat_score}"
        )

        # --------------------------------------------
        # GEOIP THREAT INTELLIGENCE
        # --------------------------------------------

        geo_data = lookup_ip(
            packet["src_ip"]
        )

        print(
            f"[GEOIP] {packet['src_ip']} → "
            f"{geo_data['country']}, "
            f"{geo_data['city']}"
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
                country=geo_data["country"],
                description=alert
            )

            # ----------------------------------------
            # LIVE WEBSOCKET BROADCAST
            # ----------------------------------------

            await broadcast({

                "type": "alert",

                "src_ip": packet["src_ip"],

                "message": alert,

                "threat_score": threat_score,

                "geoip": geo_data
            })

        # --------------------------------------------
        # SAVE PACKET
        # --------------------------------------------

        save_packet(
            db,
            packet
        )

        print("\n[PACKET SAVED]")
        print(packet)

        return {
            "status": "saved"
        }

    except Exception as e:

        print(
            f"Error processing packet: {e}"
        )

        return {

            "status": "error",

            "message": str(e)
        }

    finally:

        db.close()