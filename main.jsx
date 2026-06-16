import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
// import App from "./App.jsx";
// import First from "./First.jsx";
//import MyHooks from "./MyHooks.jsx";
// import MyEvent from "./MyEvent.jsx";
// import List from "./List.jsx";
import LoginPage from "./LoginPage.jsx";

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

createRoot(document.getElementById("root")).render(<LoginPage />);
