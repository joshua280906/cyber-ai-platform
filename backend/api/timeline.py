from fastapi import APIRouter

from sqlalchemy import func

from database.connection import SessionLocal

from database.models import Alert

router = APIRouter()

# ---------------------------------------------------
# ATTACK TIMELINE
# ---------------------------------------------------

@router.get("/attack-timeline")

def attack_timeline():

    db = SessionLocal()

    try:

        results = (

            db.query(

                Alert.timestamp,

                func.count(Alert.id)
            )

            .group_by(Alert.timestamp)

            .order_by(Alert.timestamp.asc())

            .limit(20)

            .all()
        )

        data = []

        for timestamp, count in results:

            data.append({

                "time": timestamp,

                "count": count
            })

        return data

    finally:

        db.close()