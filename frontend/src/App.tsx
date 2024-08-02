import { Route, Routes } from "react-router-dom";
import "./App.css";
import AuthAdmin from "./pages/AuthAdmin";

function App() {
  return (
    <Routes>
      <Route path="/admin" element={<AuthAdmin />}></Route>
    </Routes>
  );
}

export default App;
