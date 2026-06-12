import { useEffect, useState } from "react"

import {

  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend,
  ResponsiveContainer

} from "recharts"

import API from "../services/api"

const COLORS = [

  "#38bdf8",
  "#f59e0b",
  "#22c55e",
  "#ef4444"
]

function ProtocolChart() {

  const [data, setData] = useState([])

  useEffect(() => {

    loadProtocols()

  }, [])

  async function loadProtocols() {

    try {

      const response = await API.get(

        "/stats/protocols"
      )

      setData(response.data)

    } catch (error) {

      console.error(error)
    }
  }

  return (

    <div>

      <h2>Protocol Distribution</h2>

      <div
        style={{
          width: "100%",
          height: "350px",
          display: "flex",
          justifyContent: "center",
          alignItems: "center"
        }}
      >

        <ResponsiveContainer width="100%" height="100%">

          <PieChart>

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

                  key={`cell-${index}`}

                  fill={COLORS[index % COLORS.length]}
                />
              ))}

            </Pie>

            <Tooltip />

            <Legend />

          </PieChart>

        </ResponsiveContainer>

      </div>

    </div>
  )
}

export default ProtocolChart