import React, { useEffect, useState } from "react";
import { useAuthStore } from "../store/authStore";
import { useNavigate } from "react-router-dom";
import { twMerge } from "tailwind-merge";
import Button from "./Button";
import { loginAdmin } from "../services/apiUtils";

export const AuthForm = () => {
  const [username, setusername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const { login } = useAuthStore();
  const onChangeUsername = (event: React.FormEvent<HTMLInputElement>) => {
    setusername(event.currentTarget.value);
  };
  const onChangePassword = (event: React.FormEvent<HTMLInputElement>) => {
    setPassword(event.currentTarget.value);
  };
  const onSubmit = async (e: React.SyntheticEvent) => {
    e.preventDefault();
    const isAuth = await loginAdmin(username, password);
    if (isAuth) {
      login();
      navigate("/admin/dashboard");
    }
  };

  return (
    <form
      className="p-4 pt-8 flex flex-col w-full justify-center font-semibold items-center text-teal-200"
      onSubmit={onSubmit}
    >
      <div className="w-1/4 flex flex-col mb-3 items-center">
        <input
          className="p-1 my-1 bg-gray-300 border-none h-10 rounded-md outline-none font-bold text-purple-900 w-full"
          type="text"
          value={username}
          placeholder="Login"
          required
          onChange={onChangeUsername}
        />
      </div>
      <div className="w-1/4 flex flex-col mb-3 items-center">
        <input
          className="bg-gray-300 border-none outline-none my-1 p-1 h-10 rounded-md font-bold text-purple-900 w-full"
          type="password"
          value={password}
          placeholder="Password"
          required
          onChange={onChangePassword}
        />
      </div>
      <Button
        type="submit"
        className={twMerge(
          "w-1/4 rounded-md",
          password && username ? "" : "opacity-75 "
        )}
      >
        Log in
      </Button>
    </form>
  );
};
