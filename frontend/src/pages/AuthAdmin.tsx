import { useEffect, useState } from "react";
import { AuthForm } from "../components/dashboard/shared/AuthForm";
import { useAuthStore } from "../store/authStore";
import { Outlet, useLocation, useNavigate } from "react-router-dom";
import { checkToken } from "../services/apiUtils";

const AuthAdmin = () => {
  const { login, logout, isAuthenticated } = useAuthStore();
  const [isLoading, setIsLoading] = useState(true);
  const navigate = useNavigate();
  const location = useLocation();
  useEffect(() => {
    const checkLoggedIn = async () => {
      try {
        const isToken = await checkToken();
        if (isToken) {
          login();
          if (
            location.pathname === "/admin" ||
            location.pathname === "/admin/"
          ) {
            navigate("/admin/dashboard", { replace: true });
          }
        } else {
          logout();
          navigate("/admin");
        }
      } catch (error) {
        logout();
        navigate("/admin");
      } finally {
        setIsLoading(false);
      }
    };
    checkLoggedIn();
  }, [login, logout, navigate]);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return isAuthenticated ? <Outlet /> : <AuthForm />;
};

export default AuthAdmin;
