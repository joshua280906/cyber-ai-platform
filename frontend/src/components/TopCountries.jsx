import { useEffect, useState } from "react"

import API from "../services/api"

function TopCountries() {

  const [countries, setCountries] = useState([])

  useEffect(() => {

    loadCountries()

  }, [])

  async function loadCountries() {

    try {

      const response = await API.get(

        "/threat-intel/top-countries"
      )

      setCountries(response.data)

    } catch (error) {

      console.error(error)
    }
  }

  return (

    <div>

      <h2>Top Threat Countries</h2>

      <table>

        <thead>

          <tr>

            <th>Country</th>

            <th>Threat Count</th>

          </tr>

        </thead>

        <tbody>

          {countries.map((country, index) => (

            <tr key={index}>

              <td>{country.country}</td>

              <td>{country.count}</td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  )
}

export default TopCountries