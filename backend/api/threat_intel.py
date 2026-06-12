from fastapi import APIRouter

from sqlalchemy import func

from database.connection import SessionLocal

from database.models import Alert

router = APIRouter()

# ---------------------------------------------------
# TOP THREAT COUNTRIES
# ---------------------------------------------------

@router.get("/top-countries")

def top_countries():

    db = SessionLocal()

    try:

        results = (

            db.query(

                Alert.country,

                func.count(Alert.id)
            )

            .group_by(Alert.country)

            .order_by(

                func.count(Alert.id).desc()
            )

            .limit(10)

            .all()
        )

        data = []

        for country, count in results:

            data.append({

                "country": country,

                "count": count
            })

        return data

    finally:

        db.close()