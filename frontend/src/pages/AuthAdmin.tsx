import { useEffect, useState } from "react";
import { AuthForm } from "../components/AuthForm";
import { checkToken } from "../services/api";
import { useAuthStore } from "../store/authStore";
import AdminDashboard from "./AdminDashboard";

const AuthAdmin = () => {
  const { login, logout, isAuthenticated } = useAuthStore();
  const [isLoading, setIsLoading] = useState(true);
  useEffect(() => {
    const checkLoggedIn = async () => {
      try {
        const isToken = await checkToken();
        if (isToken) {
          console.log("auth");
          login();
        } else {
          console.log("not auth");
          logout();
        }
      } catch (error) {
        console.log("not auth");
        logout();
      } finally {
        setIsLoading(false);
      }
    };
    checkLoggedIn();
  }, [login, logout]);

  return (
    <>
      {isLoading ? (
        " LOADING "
      ) : !isAuthenticated ? (
        <AuthForm></AuthForm>
      ) : (
        <AdminDashboard></AdminDashboard>
      )}
    </>
  );
};

export default AuthAdmin;
