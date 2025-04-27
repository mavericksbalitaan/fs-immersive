import { useParams } from "react-router-dom"

export default function UserProfile() {
  const params = useParams();
  // console.log(params);
  const { username } = params;

  return (
    <>
      <h1>User Profile Component</h1>
      <h2>Welcome,  { username } !</h2>
    </>
  )
}
