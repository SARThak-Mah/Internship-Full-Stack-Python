import React from "react";
import "./Form.css";

export default function Form() {
  let [uname, setUname] = React.useState("");
  let [pass, setPass] = React.useState("");

  let handleClick = () => {
    console.log("Submitted credentials:", uname, pass);
  };

  return (
    <div className="container">
      <form className="form">
        <label>Username</label>
        <input
          type="text"
          name="uname"
          placeholder="Enter username"
          value={uname}
          onChange={(e) => setUname(e.target.value)}
        />
        <label>Password</label>
        <input
          type="password"
          name="pass"
          placeholder="Enter password"
          value={pass}
          onChange={(e) => setPass(e.target.value)}
        />
        <button type="button" onClick={handleClick}>
          Submit
        </button>
      </form>
    </div>
  );
}
