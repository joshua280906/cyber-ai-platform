from fastapi import APIRouter

from database.connection import SessionLocal
from database.models import Alert

router = APIRouter()

# ---------------------------------------------------
# GET RECENT ALERTS
# ---------------------------------------------------

@router.get("/recent")

def get_recent_alerts():

    db = SessionLocal()

    try:

        alerts = (

            db.query(Alert)

            .order_by(Alert.id.desc())

            .limit(20)

            .all()
        )

        result = []

        for alert in alerts:

            result.append({

                "id": alert.id,

                "timestamp": alert.timestamp,

                "source_ip": alert.src_ip,

                "alert_type": alert.alert_type,

                "severity": alert.severity
            })

        return result

    finally:

        db.close()