import { Outlet } from "react-router-dom";
import DashboardSidebar from "../components/dashboard/DashboardSidebar";

const AdminDashboard = () => {
  return (
    <div className="flex h-full w-full">
      <DashboardSidebar />
      <div className="flex-1 p-3 h-full w-full">
        <div className="bg-item h-full rounded-3xl p-5 font-medium text-lg">
          <Outlet />
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;
