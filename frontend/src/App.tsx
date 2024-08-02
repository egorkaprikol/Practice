import { Route, Routes } from "react-router-dom";
import "./App.css";
import AuthAdmin from "./pages/AuthAdmin";
import AdminDashboard from "./pages/AdminDashboard";
import VisitsList from "./components/VisitsList";
import DoctorsList from "./components/DoctorsList";
import DashboardMain from "./components/DashboardMain";

function App() {
  return (
    <div className="bg ">
      <Routes>
        <Route path="/admin" element={<AuthAdmin />}>
          <Route path="dashboard" element={<AdminDashboard />}>
            <Route path="" element={<DashboardMain />}></Route>
            <Route path="visits" element={<VisitsList />}></Route>
            <Route path="doctors" element={<DoctorsList />}></Route>
          </Route>
        </Route>
      </Routes>
    </div>
  );
}

export default App;
