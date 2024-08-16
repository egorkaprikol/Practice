import { Route, Routes } from "react-router-dom";
import "./App.css";
import AuthAdmin from "./pages/AuthAdmin";
import AdminDashboard from "./pages/AdminDashboard";
import DashboardMain from "./components/dashboard/DashboardMain";
import VisitsList from "./components/dashboard/VisitsList";
import DoctorsList from "./components/dashboard/doctors/DoctorsList";
import NotFoundPage from "./pages/NotFoundPage";
import ManageList from "./components/dashboard/manage/ManageList";
import EditDoctor from "./components/dashboard/doctors/EditDoctorById";
import { Toaster } from "sonner";
import AddDoctorExperience from "./components/dashboard/doctors/AddDoctorExperience";
import CreateDoctorProfile from "./components/dashboard/doctors/CreateDoctorProfile";

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
            <Route path="doctors/new" element={<CreateDoctorProfile />}></Route>
            <Route path="doctors/:id/edit/" element={<EditDoctor />}></Route>
            <Route
              path="doctors/:id/experience/"
              element={<AddDoctorExperience />}
            ></Route>
            <Route path="manage" element={<ManageList />}></Route>
          </Route>
        </Route>
        <Route path="*" element={<NotFoundPage />}></Route>
      </Routes>
    </div>
  );
}

export default App;
