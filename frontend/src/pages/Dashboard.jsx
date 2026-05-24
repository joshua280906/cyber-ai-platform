import "../styles/global.css"

function Dashboard() {

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
            <p>12,430</p>
          </div>

          <div className="card">
            <h3>Threat Alerts</h3>
            <p>37</p>
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

      </div>

    </div>
  )
}

export default Dashboard