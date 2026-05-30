import { useEffect, useState } from "react"

import {

  MapContainer,
  TileLayer,
  Marker,
  Popup

} from "react-leaflet"

import L from "leaflet"

import socket from "../services/websocket"

import "leaflet/dist/leaflet.css"

const icon = new L.Icon({

  iconUrl:

    "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png",

  iconSize: [25, 41]
})

function ThreatMap() {

  const [threats, setThreats] = useState([])

  useEffect(() => {

    socket.onmessage = (event) => {

      const data = JSON.parse(event.data)

      console.log("LIVE MAP ALERT:", data)

      if (data.geoip) {

        setThreats((prev) => [

          ...prev,

          data
        ])
      }
    }

  }, [])

  return (

    <div className="map-container">

      <h2>Live Global Threat Map</h2>

      <MapContainer

        center={[20, 0]}

        zoom={2}

        style={{

          height: "500px",

          width: "100%"
        }}
      >

        <TileLayer

          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        {threats.map((threat, index) => (

          <Marker

            key={index}

            position={[

              threat.geoip.lat,

              threat.geoip.lon
            ]}

            icon={icon}
          >

            <Popup>

              <strong>IP:</strong>

              {threat.src_ip}

              <br />

              <strong>Country:</strong>

              {threat.geoip.country}

              <br />

              <strong>City:</strong>

              {threat.geoip.city}

              <br />

              <strong>Threat Score:</strong>

              {threat.threat_score}

              <br />

              <strong>Alert:</strong>

              {threat.message}

            </Popup>

          </Marker>
        ))}

      </MapContainer>

    </div>
  )
}

export default ThreatMap