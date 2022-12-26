import "style.css"
import "tailwindcss/lib/css/preflight.css"
import GlobalStyles from "styles/GlobalStyles"
import { css } from "styled-components/macro" //eslint-disable-line

import { BrowserRouter as Router, Routes, Route } from "react-router-dom"

import LoginPage from "pages/Login"
import SignupPage from "pages/Signup"
import BlogIndexPage from "pages/BlogIndex"

const Dev = () => {
  return (
    <div>
      <a href="/login">Login</a> <br />
      <a href="/signup">Signup</a> <br />
      <a href="/blogs">Blogs</a> <br />
    </div>
  )
}

const App = () => {
  return (
    <>
      <GlobalStyles />
      <Router>
        <Routes>
          <Route path="/" element={<Dev />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/signup" element={<SignupPage />} />
          <Route path="/blogs" element={<BlogIndexPage />} />
        </Routes>
      </Router>
    </>
  )
}

export default App
