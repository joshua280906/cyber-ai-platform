import { useEffect, useState } from "react"

import API from "../services/api"

function TopIPs() {

  const [ips, setIps] = useState([])

  useEffect(() => {

    loadTopIPs()

    const interval = setInterval(() => {

      loadTopIPs()

    }, 5000)

    return () => clearInterval(interval)

  }, [])

  async function loadTopIPs() {

    try {

      const response = await API.get(

        "/stats/top-ips"
      )

      setIps(response.data)

    } catch (error) {

      console.error(error)
    }
  }

  return (

    <div className="top-ips-container">

      <h2>Top Active IPs</h2>

      <table className="top-ips-table">

        <thead>

          <tr>

            <th>IP Address</th>
            <th>Packet Count</th>

          </tr>

        </thead>

        <tbody>

          {ips.map((ip, index) => (

            <tr key={index}>

              <td>{ip.ip}</td>

              <td>{ip.count}</td>

            </tr>
          ))}

        </tbody>

      </table>

    </div>
  )
}

export default TopIPs