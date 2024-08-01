import React, { useEffect, useState } from "react";
import { checkToken, loginAdmin } from "../services/api";

export const AuthForm = () => {
  const [login, setLogin] = useState("");
  const [password, setPassword] = useState("");

  useEffect(() => {
    const checkLoggedIN = async () => {
      const isToken = await checkToken().catch(() => {
        console.log("not fine");
      });
      if (isToken) {
        console.log("LOGGED IN");
      }
    };
    checkLoggedIN();
  }, []);

  const onChangeLogin = (event: React.FormEvent<HTMLInputElement>) => {
    setLogin(event.currentTarget.value);
  };
  const onChangePassword = (event: React.FormEvent<HTMLInputElement>) => {
    setPassword(event.currentTarget.value);
  };
  const onSubmit = (e: React.SyntheticEvent) => {
    e.preventDefault();
    loginAdmin(login, password);
  };

  return (
    <form className="p-4 flex justify-center" onSubmit={onSubmit}>
      <label>
        Login
        <input
          className="p-1 m-3"
          type="text"
          value={login}
          onChange={onChangeLogin}
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
