from datetime import datetime

from database.models import Alert

# ---------------------------------------------------
# SAVE ALERT
# ---------------------------------------------------

def save_alert(

    db,

    src_ip,

    alert_type,

    severity,

    country,

    description
):

    alert = Alert(

        timestamp=str(datetime.now()),

        src_ip=src_ip,

        alert_type=alert_type,

        severity=severity,
        
        country=country,

        description=description
    )

    db.add(alert)

    db.commit()

    db.refresh(alert)

    return alert