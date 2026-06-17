import React, { useEffect, useState } from "react";

export default function Api() {
  let [product, setProduct] = useState([]);
  let getapi = async () => {
    //let record = await fetch("https://fakestoreapi.com/products/1");
    let record = await fetch("https://fakestoreapi.com/products");
    let data = await record.json();
    setProduct(data);
  };
  useEffect(() => {
    getapi();
  }, []);
  return (
    <div>
      {/* <h1>Id: {product.id}</h1>
      <h1>Title: {product.title}</h1>
      <h1>Price: {product.price}</h1>
      <p>Description: {product.description}</p>
      <img
        src={product.image}
        width="200"
        height="200"
        alt={product.title}
      ></img> */}
      {product.map((item) => (
        <div key={item.id}>
          <h2>{item.title}</h2>
          <p>{item.description}</p>
          <img src={item.image} width="200" height="200" alt={item.title}></img>
        </div>
      ))}
    </div>
  );
}
