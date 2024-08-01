import Cookies from "js-cookie";

const API_URL = "http://127.0.0.1:8000";

export const loginAdmin = async (login: string, password: string) => {
  const res = await fetch(`${API_URL}/login`, {
    method: "POST",
    headers: {
      "Content-type": "application/json",
    },
    body: JSON.stringify({ login, password }),
  })
    .then((res) => {
      if (!res.ok) {
        console.log("fail");
        alert("Wrong data");
      }
      return res.json();
    })
    .then((data) => {
      const token = data.access_token;
      console.log(token);
      Cookies.set("token", token, { expires: 30 });
      return token;
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
