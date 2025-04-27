import Login from "./components/Login"
import UserProfile from "./components/UserProfile"
import { BrowserRouter as Router, Routes, Route, Navigate, useHistory } from "react-router-dom"
import { useState } from "react";

export default function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const history = useHistory();
  console.log(history)


  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={isLoggedIn ? <UserProfile /> : <Navigate replace to="/login" />} />

          <Route path="/login" element={<Login isLoggedIn={isLoggedIn} setIsLoggedIn={setIsLoggedIn} />} />
          <Route path="/userprofile/:username" element={<UserProfile />} />
        </Routes>
      </Router>
    </>
  )
}
