import React, { useEffect, useState } from "react";
import { checkToken, loginAdmin } from "../services/api";
import { useAuthStore } from "../store/authStore";

export const AuthForm = () => {
  const [username, setusername] = useState("");
  const [password, setPassword] = useState("");
  const { login } = useAuthStore();
  const onChangeusername = (event: React.FormEvent<HTMLInputElement>) => {
    setusername(event.currentTarget.value);
  };
  const onChangePassword = (event: React.FormEvent<HTMLInputElement>) => {
    setPassword(event.currentTarget.value);
  };
  const onSubmit = async (e: React.SyntheticEvent) => {
    e.preventDefault();
    const isAuth = await loginAdmin(username, password);
    if (isAuth) login();
  };

  return (
    <form className="p-4 flex justify-center" onSubmit={onSubmit}>
      <label>
        username
        <input
          className="p-1 m-3"
          type="text"
          value={username}
          onChange={onChangeusername}
        />
      </label>
      <label>
        Password
        <input
          className="p-1 m-3"
          type="password"
          value={password}
          onChange={onChangePassword}
        />
      </label>
      <input type="submit" />
    </form>
  );
};
