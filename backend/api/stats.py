from fastapi import APIRouter

from sqlalchemy import func

from database.connection import SessionLocal
from database.models import Packet, Alert

router = APIRouter()

# ---------------------------------------------------
# TOTAL PACKETS
# ---------------------------------------------------

@router.get("/packets")

def get_packet_count():

    db = SessionLocal()

    try:

        count = db.query(Packet).count()

        return {
            "total_packets": count
        }

    finally:

        db.close()

# ---------------------------------------------------
# TOTAL ALERTS
# ---------------------------------------------------

@router.get("/alerts")

def get_alert_count():

    db = SessionLocal()

    try:

        count = db.query(Alert).count()

        return {
            "total_alerts": count
        }

    finally:

        db.close()

# ---------------------------------------------------
# PROTOCOL DISTRIBUTION
# ---------------------------------------------------

@router.get("/protocols")

def get_protocol_stats():

    db = SessionLocal()

    try:

        results = (

            db.query(

                Packet.protocol,
                func.count(Packet.protocol)

            )

            .group_by(Packet.protocol)

            .all()
        )

        protocol_data = []

        for protocol, count in results:

            protocol_data.append({

                "protocol": protocol,
                "count": count
            })

        return protocol_data

    finally:

        db.close()
        
# ---------------------------------------------------
# TOP SOURCE IPS
# ---------------------------------------------------

@router.get("/top-ips")

def get_top_ips():

    db = SessionLocal()

    try:

        results = (

            db.query(

                Packet.src_ip,
                func.count(Packet.src_ip)

            )

            .group_by(Packet.src_ip)

            .order_by(

                func.count(Packet.src_ip).desc()
            )

            .limit(10)

            .all()
        )

        top_ips = []

        for ip, count in results:

            top_ips.append({

                "ip": ip,
                "count": count
            })

        return top_ips

    finally:

        db.close()