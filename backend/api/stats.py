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

# ---------------------------------------------------

# THREATS BY SEVERITY

# ---------------------------------------------------

@router.get("/severity-stats")
def get_severity_stats():
    db = SessionLocal()
    try:
        results = (
            db.query(
                Alert.severity,
                func.count(Alert.severity)
            )
            .group_by(Alert.severity)
            .all()
        )
        data = []
        for severity, count in results:
            data.append({
                "severity": severity,
                "count": count
            })
        return data
    finally:
        db.close()

# ---------------------------------------------------

# THREAT TYPE STATISTICS

# ---------------------------------------------------

@router.get("/threat-types")
def get_threat_types():
    db = SessionLocal()
    try:
        results = (
            db.query(
                Alert.description,
                func.count(Alert.description)
            )
            .group_by(Alert.description)
            .order_by(
                func.count(Alert.description).desc()
            )
            .all()
        )
        data = []
        for threat_type, count in results:
            data.append({
                "threat_type": threat_type,
                "count": count
            })
        return data
    finally:
        db.close()
