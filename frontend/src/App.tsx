import { Route, Routes } from "react-router-dom";
import "./App.css";
import AuthAdmin from "./pages/AuthAdmin";
import AdminDashboard from "./pages/AdminDashboard";
import DashboardMain from "./components/dashboard/DashboardMain";
import VisitsList from "./components/dashboard/VisitsList";
import DoctorsList from "./components/dashboard/doctors/DoctorsList";
import NotFoundPage from "./pages/NotFoundPage";
import AddDoctor from "./components/dashboard/doctors/AddDoctor";
import ManageList from "./components/dashboard/manage/ManageList";
import EditDoctor from "./components/dashboard/doctors/EditDoctorById";
import { Toaster } from "sonner";

function App() {
  return (
    <div className="bg bg-bg">
      <Toaster richColors duration={2000}></Toaster>
      <Routes>
        <Route path="/admin" element={<AuthAdmin />}>
          <Route path="dashboard" element={<AdminDashboard />}>
            <Route index element={<DashboardMain />}></Route>
            <Route path="visits" element={<VisitsList />}></Route>
            <Route path="doctors" element={<DoctorsList />}></Route>
            <Route path="doctors/new" element={<AddDoctor />}></Route>
            <Route path="doctors/edit/:id" element={<EditDoctor />}></Route>
            <Route path="manage" element={<ManageList />}></Route>
          </Route>
        </Route>
        <Route path="*" element={<NotFoundPage />}></Route>
      </Routes>
    </div>
  );
}

export default App;
