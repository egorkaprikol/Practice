import { useEffect, useState } from "react";
import { AuthForm } from "../components/AuthForm";
import { checkToken } from "../services/api";
import { useAuthStore } from "../store/authStore";
import { Outlet, useLocation, useNavigate } from "react-router-dom";

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
          console.log("auth");
          login();
          if (location.pathname === "/admin") {
            // Перенаправление только если путь - "/admin"
            navigate("/admin/dashboard");
          }
        } else {
          console.log("not auth");
          logout();
          navigate("/admin");
        }
      } catch (error) {
        console.log("not auth");
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
