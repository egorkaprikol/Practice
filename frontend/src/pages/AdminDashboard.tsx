import { Outlet } from "react-router-dom";
import DashboardSidebar from "../components/DashboardSidebar";

const AdminDashboard = () => {
  return (
    <div className="flex">
      <DashboardSidebar />
      <div className="flex-1 p-2">
        <Outlet />
      </div>
    </div>
  );
};

export default AdminDashboard;
