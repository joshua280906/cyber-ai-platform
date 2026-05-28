import { useEffect, useState } from "react"

import {

  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend

} from "recharts"

import API from "../services/api"

function ProtocolChart() {

  const [data, setData] = useState([])

  useEffect(() => {

  loadProtocolData()

  const interval = setInterval(() => {

    loadProtocolData()

  }, 5000)

  return () => clearInterval(interval)

}, [])

  // --------------------------------------------------
  // LOAD PROTOCOL DATA
  // --------------------------------------------------

  async function loadProtocolData() {

    try {

      const response = await API.get(

        "/stats/protocols"
      )

      setData(response.data)

    } catch (error) {

      console.error(error)
    }
  }

  const COLORS = [

    "#38bdf8",
    "#ef4444",
    "#22c55e",
    "#f59e0b"
  ]

  return (

    <div className="chart-container">

      <h2>Protocol Distribution</h2>

      <PieChart width={400} height={300}>

        <Pie

          data={data}

          dataKey="count"

          nameKey="protocol"

          cx="50%"

          cy="50%"

          outerRadius={100}

          label
        >

          {data.map((entry, index) => (

            <Cell

              key={index}

              fill={COLORS[index % COLORS.length]}
            />
          ))}

        </Pie>

        <Tooltip />

        <Legend />

      </PieChart>

    </div>
  )
}

export default ProtocolChart