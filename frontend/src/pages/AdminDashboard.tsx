import { Outlet } from "react-router-dom";
import DashboardSidebar from "../components/dashboard/DashboardSidebar";

const AdminDashboard = () => {
  return (
    <div className="flex h-full wf">
      <DashboardSidebar />
      <div className="flex-1 p-2">
        <Outlet />
      </div>
    </div>
  );
};

export default AdminDashboard;
