import React from "react";

export default function List() {
  let arr = [56, 78, 98, 76, 54, 34];
  let data = [
    { uname: "Sarthak", age: 20, marks: 90 },
    { uname: "Ojaswi", age: 18, marks: 85 },
    { uname: "Anushka", age: 18, marks: 98 },
  ];
  /*arr.forEach((a) => {
            console.log(a);
        })*/
  console.log(data);
  let newarr = arr.map((a, i) => {
    return <li key={i}>{a}</li>;
  });
  return (
    <div>
      <ul>{newarr}</ul>
      <hr />
      <ul>
        {arr.map((a, i) => {
          return <li key={i}>{a}</li>;
        })}
      </ul>
      <hr />
      <ul>
        {data.map((a, i) => {
          return (
            <li key={i}>
              <h1>Name: {a.uname}</h1>
              <h1>Age: {a.age}</h1>
              <h1>Marks: {a.marks}</h1>
            </li>
          );
        })}
      </ul>
    </div>
  );
}
