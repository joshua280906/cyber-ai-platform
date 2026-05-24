from database.models import Packet

# ---------------------------------------------------
# SAVE PACKET
# ---------------------------------------------------

def save_packet(db, packet_data):

    packet = Packet(

        timestamp=packet_data["timestamp"],

        src_ip=packet_data["src_ip"],
        dst_ip=packet_data["dst_ip"],

        protocol=packet_data["protocol"],

        src_port=str(packet_data["src_port"]),
        dst_port=str(packet_data["dst_port"]),

        packet_size=packet_data["packet_size"]
    )

    db.add(packet)

    db.commit()

    db.refresh(packet)

    return packet