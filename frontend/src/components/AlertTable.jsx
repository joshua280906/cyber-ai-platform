import { useEffect, useState } from "react"

import API from "../services/api"

import socket from "../services/websocket"

function AlertTable() {

  const [alerts, setAlerts] = useState([])

  // --------------------------------------------------
  // LOAD ALERTS
  // --------------------------------------------------

  useEffect(() => {

  loadAlerts()

  socket.onmessage = (event) => {

  const data = JSON.parse(event.data)

  console.log("LIVE ALERT:", data)

  loadAlerts()
}

  const interval = setInterval(() => {

    loadAlerts()

  }, 5000)

  return () => clearInterval(interval)

}, [])

  // --------------------------------------------------
  // FETCH ALERTS
  // --------------------------------------------------

  async function loadAlerts() {

    try {

      const response = await API.get(

        "/alerts/recent"
      )

      setAlerts(response.data)

    } catch (error) {

      console.error(error)
    }
  }

  return (

    <div className="alert-table-container">

      <h2>Recent Threat Alerts</h2>

      <table className="alert-table">

        <thead>

          <tr>

            <th>Severity</th>
            <th>Source IP</th>
            <th>Threat Type</th>
            <th>Timestamp</th>

          </tr>

        </thead>

        <tbody>

          {alerts.map((alert) => (

            <tr key={alert.id}>

              <td>{alert.severity}</td>

              <td>{alert.source_ip}</td>

              <td>{alert.alert_type}</td>

              <td>{alert.timestamp}</td>

            </tr>
          ))}

        </tbody>

      </table>

    </div>
  )
}

export default AlertTable