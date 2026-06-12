import { useEffect, useState } from "react"

import {

  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer

} from "recharts"

import API from "../services/api"

function AttackTimeline() {

  const [data, setData] = useState([])

  useEffect(() => {

    loadTimeline()

  }, [])

  async function loadTimeline() {

    try {

      const response = await API.get(

        "/analytics/attack-timeline"
      )

      setData(response.data)

    } catch (error) {

      console.error(error)
    }
  }

  return (

    <div>

      <h2>Attack Timeline</h2>

      <ResponsiveContainer width="100%" height={350}>

        <LineChart data={data}>

          <XAxis dataKey="time" />

          <YAxis />

          <Tooltip />

          <Line

            type="monotone"

            dataKey="count"

            stroke="#38bdf8"

            strokeWidth={3}
          />

        </LineChart>

      </ResponsiveContainer>

    </div>
  )
}

export default AttackTimeline