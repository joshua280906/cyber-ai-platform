import { useEffect, useState } from "react"

import API from "../services/api"

import "../styles/global.css"

import AlertTable from "../components/AlertTable"

import ProtocolChart from "../components/ProtocolChart"

import TrafficFeed from "../components/TrafficFeed"

import TopIPs from "../components/TopIPs"

function Dashboard() {

  const [packetCount, setPacketCount] = useState(0)

  const [alertCount, setAlertCount] = useState(0)

  // --------------------------------------------------
  // LOAD DASHBOARD DATA
  // --------------------------------------------------

  useEffect(() => {

  loadStats()

  const interval = setInterval(() => {

    loadStats()

  }, 5000)

  return () => clearInterval(interval)

}, [])

  // --------------------------------------------------
  // FETCH STATS
  // --------------------------------------------------

  async function loadStats() {

    try {

      // --------------------------------------------
      // PACKETS
      // --------------------------------------------

      const packetResponse = await API.get(

        "/stats/packets"
      )

      setPacketCount(

        packetResponse.data.total_packets
      )

      // --------------------------------------------
      // ALERTS
      // --------------------------------------------

      const alertResponse = await API.get(

        "/stats/alerts"
      )

      setAlertCount(

        alertResponse.data.total_alerts
      )

    } catch (error) {

      console.error(error)
    }
  }

  return (

    <div className="dashboard">

      <div className="sidebar">

        <h2>Cyber AI SOC</h2>

        <ul>

          <li>Dashboard</li>
          <li>Alerts</li>
          <li>Traffic</li>
          <li>Threat Intel</li>

        </ul>

      </div>

      <div className="main-content">

        <h1>AI-Powered Threat Detection Platform</h1>

        <div className="stats-grid">

          <div className="card">

            <h3>Total Packets</h3>

            <p>{packetCount}</p>

          </div>

          <div className="card">

            <h3>Threat Alerts</h3>

            <p>{alertCount}</p>

          </div>

          <div className="card">

            <h3>Active Connections</h3>

            <p>128</p>

          </div>

          <div className="card">

            <h3>Blocked IPs</h3>

            <p>12</p>

          </div>

          <AlertTable />

          <ProtocolChart />

          <TrafficFeed />

          <TopIPs />

        </div>

      </div>

    </div>
  )
}

export default Dashboard