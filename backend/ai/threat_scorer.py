# ---------------------------------------------------
# AI THREAT SCORING ENGINE
# ---------------------------------------------------

def calculate_threat_score(

    packet,

    anomaly_detected,

    blacklisted=False

):

    score = 0

    # --------------------------------------------
    # PACKET SIZE ANALYSIS
    # --------------------------------------------

    if packet["packet_size"] > 1000:

        score += 30

    # --------------------------------------------
    # SUSPICIOUS PORTS
    # --------------------------------------------

    suspicious_ports = [

        22,
        23,
        3389,
        445
    ]

    if packet["dst_port"] in suspicious_ports:

        score += 25

    # --------------------------------------------
    # PROTOCOL ANALYSIS
    # --------------------------------------------

    if packet["protocol"] == "ICMP":

        score += 15

    # --------------------------------------------
    # AI ANOMALY BONUS
    # --------------------------------------------

    if anomaly_detected:

        score += 40

    # --------------------------------------------
    # THREAT REPUTATION BONUS
    # --------------------------------------------

    if blacklisted:

        score += 50

    # --------------------------------------------
    # LIMIT SCORE
    # --------------------------------------------

    if score > 100:

        score = 100

    return score