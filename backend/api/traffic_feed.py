from fastapi import APIRouter

from database.connection import SessionLocal
from database.models import Packet

router = APIRouter()

# ---------------------------------------------------
# GET RECENT PACKETS
# ---------------------------------------------------

@router.get("/recent")

def get_recent_packets():

    db = SessionLocal()

    try:

        packets = (

            db.query(Packet)

            .order_by(Packet.id.desc())

            .limit(20)

            .all()
        )

        result = []

        for packet in packets:

            result.append({

                "id": packet.id,

                "src_ip": packet.src_ip,

                "dst_ip": packet.dst_ip,

                "protocol": packet.protocol,

                "packet_size": packet.packet_size
            })

        return result

    finally:

        db.close()