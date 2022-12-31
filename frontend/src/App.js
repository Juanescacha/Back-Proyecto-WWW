import "style.css"
import "tailwindcss/lib/css/preflight.css"
import GlobalStyles from "styles/GlobalStyles"
import { css } from "styled-components/macro" //eslint-disable-line

import { BrowserRouter as Router, Routes, Route } from "react-router-dom"

import LoginPage from "pages/Login"
import SignupPage from "pages/Signup"
import BlogIndexPage from "pages/BlogIndex"
import LandingPage from "pages/LandingPage"

const App = () => {
  return (
    <>
      <GlobalStyles />
      <Router>
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<SignupPage />} />
          <Route path="/blogs" element={<BlogIndexPage />} />
        </Routes>
      </Router>
    </>
  )
}

export default App
