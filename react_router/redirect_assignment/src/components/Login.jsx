import { useNavigate } from "react-router-dom"
import { useEffect } from "react";

export default function Login({ isLoggedIn, setIsLoggedIn }) {
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();

    const username = e.target[0].value;
    const password = e.target[1].value;

    if (username === "John" && password === "1234") {
      setIsLoggedIn(true)
      console.log('User John is logged in')
      navigate(`/userprofile/${username}`)
    } else {
      navigate('/')
    }
  }

  useEffect(() => {
    if (!isLoggedIn) {
      console.log("User is not logged in")
    }
  }, [])

  return (
    <>
      <h1>Login Component</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="username">Username:</label>
        <input type="text" placeholder="Input username" />
        <br />
        <label htmlFor="password">Password:</label>
        <input type="password" placeholder="Input password" />
        <br />
        <button type="submit">Login</button>
      </form>
    </>
  )
}
