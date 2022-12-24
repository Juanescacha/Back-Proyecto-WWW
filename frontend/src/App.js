import "style.css"
import "tailwindcss/lib/css/preflight.css"
import GlobalStyles from "styles/GlobalStyles"
import { css } from "styled-components/macro" //eslint-disable-line

import { BrowserRouter as Router, Routes, Route } from "react-router-dom"

const Dev = () => {
  return <div>Test</div>
}

const App = () => {
  return (
    <>
      <GlobalStyles />
      <Router>
        <Routes>
          <Route path="/" element={<Dev />} />
        </Routes>
      </Router>
    </>
  )
}

export default App
