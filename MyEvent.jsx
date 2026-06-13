import React from "react";

export default function MyEvent() {
  let handleClick = (a) => {
    // alert("Button Clicked");
    console.log("Button Clicked", a);
  };
  /* let handleEvent = (a) => {
        handleClick(100);
    } */
  return (
    <div>
      {/* <button onClick={() => handleClick(100)}>MyEvent</button> */}
      <h1>MyEvent</h1>
      <button onClick={() => handleClick(100)}>Click Me</button>
    </div>
  );
}
