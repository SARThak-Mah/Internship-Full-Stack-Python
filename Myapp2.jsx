import React from "react";
import Home from "./Home";
import About from "./About";
import Contact from "./Contact";
import Nav from "./Nav";

import { BrowserRouter, Routes, Route } from "react-router-dom";

export default function Myapp2() {
  return (
    <div>
      <BrowserRouter>
        <Nav />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}
