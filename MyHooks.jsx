import React from "react";

export default function MyHooks() {
  let [value, setValue] = React.useState(100);
  let [name, setName] = React.useState("Sarthak");
  let [data, setData] = React.useState([5, 7, 9, 8, 6]);
  let [count, setCount] = React.useState(0);
  let handleClick = () => {
    setValue(200);
    setName("Ojaswi");
  };
  let increment = () => {
    if (count < 6) {
      setCount(count + 1);
    }
  };
  let decrement = () => {
    if (count > 0) {
      setCount(count - 1);
    }
  };
  return (
    <div>
      <h1>Value: {value}</h1>
      <h1>Name: {name}</h1>
      <button onClick={handleClick}>Change Value and Name</button>
      <p>Count: {count}</p>
      <div>
        {data.map((a) => {
          return <p key={a}>{a}</p>;
        })}
      </div>
      <button onClick={increment}>+</button>
      {count}
      <button onClick={decrement}>-</button>
    </div>
  );
}
