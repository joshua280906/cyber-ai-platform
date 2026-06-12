import { useEffect, useState } from "react"

import API from "../services/api"

import "../styles/global.css"

import AlertTable from "../components/AlertTable"
import TrafficFeed from "../components/TrafficFeed"
import TopIPs from "../components/TopIPs"
import ProtocolChart from "../components/ProtocolChart"
import ThreatMap from "../components/ThreatMap"
import TopCountries from "../components/TopCountries"
import AttackTimeline from "../components/AttackTimeline"

function Dashboard() {

  const [packetCount, setPacketCount] = useState(0)

  const [alertCount, setAlertCount] = useState(0)

  const [loading, setLoading] = useState(true)

  const [error, setError] = useState("")

  // ---------------------------------------------------
  // LOAD STATS ON START
  // ---------------------------------------------------

  useEffect(() => {

    loadStats()

  }, [])

  // ---------------------------------------------------
  // FETCH DASHBOARD STATS
  // ---------------------------------------------------

  async function loadStats() {

    try {

      setLoading(true)

      setError("")

      // --------------------------------------------
      // GET PACKET STATS
      // --------------------------------------------

      const packetResponse = await API.get(
        "/stats/packets"
      )

      setPacketCount(
        packetResponse.data.total_packets
      )

      // --------------------------------------------
      // GET ALERT STATS
      // --------------------------------------------

      const alertResponse = await API.get(
        "/stats/alerts"
      )

      setAlertCount(
        alertResponse.data.total_alerts
      )

    } catch (error) {

      console.error(error)

      setError(
        "Backend connection failed"
      )

    } finally {

      setLoading(false)
    }
  }

  // ---------------------------------------------------
  // LOADING SCREEN
  // ---------------------------------------------------

  if (loading) {

    return (

      <div className="status-screen">

        <h1>Loading Dashboard...</h1>

      </div>
    )
  }

  // ---------------------------------------------------
  // ERROR SCREEN
  // ---------------------------------------------------

  if (error) {

    return (

      <div className="status-screen">

        <h1>{error}</h1>

      </div>
    )
  }

  // ---------------------------------------------------
  // MAIN DASHBOARD
  // ---------------------------------------------------

  return (

    <div className="dashboard">

      {/* SIDEBAR */}

      <div className="sidebar">

        <h2>Cyber AI SOC</h2>

        <ul>

          <li>Dashboard</li>
          <li>Alerts</li>
          <li>Traffic</li>
          <li>Threat Intel</li>

        </ul>

      </div>

      {/* MAIN CONTENT */}

      <div className="main-content">

        <h1>AI-Powered Threat Detection Platform</h1>

        {/* TOP STATS */}

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

        </div>

        {/* MIDDLE SECTION */}

        <div className="middle-grid">

  <div className="panel large-panel">

    <AlertTable />

  </div>

  <div className="panel">

    <AttackTimeline />

  </div>

  <div className="panel">

    <ProtocolChart />

  </div>

</div>

        {/* LOWER SECTION */}

        <div className="lower-grid">

          <div className="panel">

            <TrafficFeed />

          </div>

          <div className="panel">

            <TopIPs />

          </div>

        </div>

        {/* MAP SECTION */}

        <div className="panel map-panel">

          <ThreatMap />

        </div>

      </div>
      <div className="panel">

  <TopCountries />

</div>

    </div>
  )
}

export default Dashboard