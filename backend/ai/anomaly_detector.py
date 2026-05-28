from sklearn.ensemble import IsolationForest

import numpy as np

# ---------------------------------------------------
# TRAIN MODEL
# ---------------------------------------------------

model = IsolationForest(

    contamination=0.05,

    random_state=42
)

# ---------------------------------------------------
# TRAINING DATA
# ---------------------------------------------------

training_data = np.array([

    [60],
    [62],
    [58],
    [70],
    [65],
    [72],
    [68],
    [64],
    [66],
    [63]
])

model.fit(training_data)

# ---------------------------------------------------
# DETECT ANOMALY
# ---------------------------------------------------

def detect_anomaly(packet_size):

    prediction = model.predict([

        [packet_size]
    ])

    return prediction[0]