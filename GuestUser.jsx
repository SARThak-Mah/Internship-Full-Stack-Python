import React from "react";

export default function GuestUser(props) {
  return (
    <div>
      <h1>Welcome User: {props.name}</h1>
      <button onClick={props.data}>Login</button>
    </div>
  );
}
