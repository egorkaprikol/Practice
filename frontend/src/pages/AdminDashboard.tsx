import React from "react";
import Button from "../components/Button";
import { useAuthStore } from "../store/authStore";

const AdminDashboard = () => {
  const { logout } = useAuthStore();
  return (
    <div>
      <p>Admin Dashboard</p>
      <Button onClick={logout}>Logout</Button>
    </div>
  );
};

export default AdminDashboard;
