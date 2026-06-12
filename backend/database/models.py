from sqlalchemy import Column, Integer, String

from database.connection import Base

# ---------------------------------------------------
# PACKET TABLE
# ---------------------------------------------------

class Packet(Base):

    __tablename__ = "packets"

    id = Column(Integer, primary_key=True, index=True)

    timestamp = Column(String)

    src_ip = Column(String)

    dst_ip = Column(String)

    protocol = Column(String)

    src_port = Column(String)

    dst_port = Column(String)

    packet_size = Column(Integer)

# ---------------------------------------------------
# ALERT TABLE
# ---------------------------------------------------

class Alert(Base):

    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)

    timestamp = Column(String)

    src_ip = Column(String)

    alert_type = Column(String)

    severity = Column(String)

    country = Column(String)

    description = Column(String)