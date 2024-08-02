import React, { useMemo } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { useAuthStore } from "../store/authStore";
import Button from "./Button";
import { Box } from "./Box";
import { SidebarItem } from "./SidebarItem";

const DashboardSidebar = () => {
  const pathname = useLocation().pathname;
  const { logout } = useAuthStore();
  const navigate = useNavigate();
  const handleLogout = () => {
    logout();
    navigate("/admin");
  };
  const routes = useMemo(
    () => [
      {
        active: pathname === "/admin/dashboard",
        label: "home",
        href: "/admin/dashboard",
        // icon: HiHome,
      },
      {
        active: pathname === "/admin/dashboard/doctors",
        label: "doctors",
        href: "/admin/dashboard/doctors",
        // icon: HiHome,
      },
      {
        active: pathname === "/admin/dashboard/visits",
        label: "visits",
        href: "/admin/dashboard/visits",
        // icon: HiHome,
      },
    ],
    [pathname]
  );

  return (
    <div>
      <div className="flex flex-col p-2 gap-y-4 h-full">
        <Box className="p-3 bg-gray-200">
          {routes.map((item) => {
            return <SidebarItem key={item.label} {...item}></SidebarItem>;
          })}
        </Box>
        <Button className="" onClick={handleLogout}>
          Logout
        </Button>
      </div>
    </div>
  );
};

export default DashboardSidebar;
