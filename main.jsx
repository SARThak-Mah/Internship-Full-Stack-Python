import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import MyApp from "./MyApp.jsx";
import App from "./App.jsx";
import First from "./First.jsx";
import MyHooks from "./MyHooks.jsx";
import MyEvent from "./MyEvent.jsx";
import List from "./List.jsx";
import LoginPage from "./LoginPage.jsx";
import Api from "./Api.jsx";
import MyApi from "./MyApi.jsx";
import MyApp from "./MyApp.jsx";
import Myapp2 from "./Myapp2.jsx";
import Form from "./Form.jsx";

/*createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
*/

// The main render block passing the initial props
// createRoot(document.getElementById("root")).render(<First />);
// props: createRoot(document.getElementById("root")).render(
//   <First name="Sarthak Mahurkar" pass="1234" />,
// );

// createRoot(document.getElementById("root")).render(<List />);

// createRoot(document.getElementById("root")).render(<MyEvent />);

//createRoot(document.getElementById("root")).render(<MyHooks />);

//createRoot(document.getElementById("root")).render(<LoginPage />);

// createRoot(document.getElementById("root")).render(<Api />);

// createRoot(document.getElementById("root")).render(<MyApi />);

createRoot(document.getElementById("root")).render(<Myapp2 />);

// createRoot(document.getElementById("root")).render(<Form />);
