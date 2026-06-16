import React from "react";

export default function PrimeUser(props) {
  return (
    <div>
      <h1>Welcome User: {props.name}</h1>
      <button onClick={props.data}>Logout</button>
    </div>
  );
}
