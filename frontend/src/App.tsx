import { Route, Routes } from "react-router-dom";
import "./App.css";
import AuthAdmin from "./pages/AuthAdmin";
import AdminDashboard from "./pages/AdminDashboard";
import VisitsList from "./components/dashboard/VisitsList";
import DoctorsList from "./components/dashboard/DoctorsList";
import DashboardMain from "./components/dashboard/DashboardMain";

function App() {
  return (
    <div className="bg bg-gray-100">
      <Routes>
        <Route path="/admin" element={<AuthAdmin />}>
          <Route path="dashboard" element={<AdminDashboard />}>
            <Route index element={<DashboardMain />}></Route>
            <Route path="visits" element={<VisitsList />}></Route>
            <Route path="doctors" element={<DoctorsList />}></Route>
          </Route>
        </Route>
        <Route
          path="*"
          element={<p className="text-2xl">Страницы не существует</p>}
        ></Route>
      </Routes>
    </div>
  );
}

export default App;
