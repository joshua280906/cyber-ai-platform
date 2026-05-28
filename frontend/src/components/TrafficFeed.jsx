import { useEffect, useState } from "react"

import API from "../services/api"

function TrafficFeed() {

  const [packets, setPackets] = useState([])

  useEffect(() => {

  loadPackets()

  const interval = setInterval(() => {

    loadPackets()

  }, 5000)

  return () => clearInterval(interval)

}, [])

  async function loadPackets() {

    try {

      const response = await API.get(

        "/traffic/recent"
      )

      setPackets(response.data)

    } catch (error) {

      console.error(error)
    }
  }

  return (

    <div className="traffic-feed-container">

      <h2>Live Traffic Feed</h2>

      <table className="traffic-table">

        <thead>

          <tr>

            <th>Source IP</th>
            <th>Destination IP</th>
            <th>Protocol</th>
            <th>Packet Size</th>

          </tr>

        </thead>

        <tbody>

          {packets.map((packet) => (

            <tr key={packet.id}>

              <td>{packet.src_ip}</td>

              <td>{packet.dst_ip}</td>

              <td>{packet.protocol}</td>

              <td>{packet.packet_size}</td>

            </tr>
          ))}

        </tbody>

      </table>

    </div>
  )
}

export default TrafficFeed