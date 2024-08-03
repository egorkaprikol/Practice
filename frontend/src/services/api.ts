import Cookies from "js-cookie";
import { Doctor } from "../types";

const API_URL = "http://127.0.0.1:8000";
<<<<<<< HEAD
=======

export const fetchDoctors = async () => {
  const response = await fetch(`${API_URL}/doctors/get`);
  if (!response.ok) {
    alert("fail");
    return;
  }
  try {
    const doctorsData: Doctor[] = await response.json();
    return doctorsData;
  } catch (error) {
    alert(error);
    return;
  }
};
>>>>>>> frontend

export const loginAdmin = async (
  login: string,
  password: string
): Promise<string | void> => {
  return fetch(`${API_URL}/login`, {
    method: "POST",
    headers: {
      "Content-type": "application/json",
    },
    body: JSON.stringify({ login, password }),
  })
    .then((res) => {
      if (!res.ok) {
        alert("Fail");
        return Promise.reject("Response error");
      }
      return res.json();
    })
    .then((data) => {
      const token = data.access_token;
      Cookies.set("token", token, { expires: 10 });
      return token;
    })
    .catch((error) => {
      console.error("Login failed:", error);
      return;
    });
};

export const checkToken = async () => {
  const token = Cookies.get("token");
  if (!token) {
    return Promise.reject("Not authorized");
  }
  const res = await fetch(`${API_URL}/token`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  if (!res.ok) {
    return Promise.reject("Response error");
  }
  return res.json();
};
