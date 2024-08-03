import { Route, Routes } from "react-router-dom";
import "./App.css";
import AuthAdmin from "./pages/AuthAdmin";
import AdminDashboard from "./pages/AdminDashboard";
import DashboardMain from "./components/dashboard/DashboardMain";
import VisitsList from "./components/dashboard/VisitsList";
import DoctorsList from "./components/dashboard/DoctorsList";
import NotFoundPage from "./pages/NotFoundPage";

function App() {
  return (
    <div className="bg bg-bg">
      <Routes>
        <Route path="/admin" element={<AuthAdmin />}>
          <Route path="dashboard" element={<AdminDashboard />}>
            <Route index element={<DashboardMain />}></Route>
            <Route path="visits" element={<VisitsList />}></Route>
            <Route path="doctors" element={<DoctorsList />}></Route>
          </Route>
        </Route>
        <Route path="*" element={<NotFoundPage />}></Route>
      </Routes>
    </div>
  );
}

export default App;
