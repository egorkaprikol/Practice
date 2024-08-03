import React, { useMemo } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { useAuthStore } from "../../store/authStore";
import Button from "../Button";
import { Box } from "../Box";
import { SidebarItem } from "../SidebarItem";

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
        label: "Главная",
        href: "/admin/dashboard",
        // icon: HiHome,
      },
      {
        active: pathname === "/admin/dashboard/doctors",
        label: "Доктора",
        href: "/admin/dashboard/doctors",
        // icon: HiHome,
      },
      {
        active: pathname === "/admin/dashboard/visits",
        label: "Посещения",
        href: "/admin/dashboard/visits",
        // icon: HiHome,
      },
    ],
    [pathname]
  );

  return (
    <div>
      <div className="flex flex-col items-center  w-48 p-2 gap-y-4 h-full">
        <Box className="p-3 bg-gray-200 h-full flex flex-col justify-between">
          <div className="flex-1">
            {routes.map((item) => {
              return <SidebarItem key={item.label} {...item}></SidebarItem>;
            })}
          </div>

          <Button className="mb-6 mt-auto w-full" onClick={handleLogout}>
            Logout
          </Button>
        </Box>
      </div>
    </div>
  );
};

export default DashboardSidebar;
