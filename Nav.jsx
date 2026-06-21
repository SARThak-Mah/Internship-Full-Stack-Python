import React from "react";
import "./Nav.css"; // Import the CSS file for styling
import { Link } from "react-router-dom";

export default function Nav() {
  return (
    <div className="nav">
      {/* <nav /> */}
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/about">About</Link>
        </li>
        <li>
          <Link to="/contact">Contact</Link>
        </li>
      </ul>
    </div>
  );
}
