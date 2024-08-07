import { useMemo } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { useAuthStore } from "../../store/authStore";
import Button from "./shared/Button";
import { Box } from "./shared/Box";
import { SidebarItem } from "./shared/SidebarItem";
import { FaListUl } from "react-icons/fa6";
import { FaNotesMedical } from "react-icons/fa";
import { FaUserDoctor } from "react-icons/fa6";
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
        label: "Main",
        href: "/admin/dashboard",
        icon: FaListUl,
      },
      {
        active: pathname.startsWith("/admin/dashboard/doctors"),
        label: "Doctors",
        href: "/admin/dashboard/doctors",
        icon: FaUserDoctor,
      },
      {
        active: pathname.startsWith("/admin/dashboard/manage"),
        label: "Manage",
        href: "/admin/dashboard/manage",
        icon: FaUserDoctor,
      },
      {
        active: pathname === "/admin/dashboard/visits",
        label: "Visits",
        href: "/admin/dashboard/visits",
        icon: FaNotesMedical,
      },
    ],
    [pathname]
  );

  return (
    <div>
      <div className="flex flex-col  items-center w-52 gap-y-4 h-full">
        <Box className=" bg-side py-6 h-full flex flex-col justify-between">
          <div className="flex-1 px-5">
            {routes.map((item) => {
              return <SidebarItem key={item.label} {...item}></SidebarItem>;
            })}
          </div>

          <Button
            className="rounded-none mt-auto w-full"
            onClick={handleLogout}
          >
            Logout
          </Button>
        </Box>
      </div>
    </div>
  );
};

export default DashboardSidebar;
