import Third from "./Third";
import Second from "./Second";

function First(props) {
  return (
    <div>
      <h1>name: {props.name}</h1>
      <h1>pass: {props.pass}</h1>
      <h1>My First Component</h1>

      {/* Reusable child components with custom props */}
      <Second uname="SARThak" />
      <Second uname="Ojaswi" />
      <Second uname="Anushka" />
      <Third />
    </div>
  );
}

export default First;
