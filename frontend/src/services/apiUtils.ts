import Cookies from "js-cookie";

export const API_URL = "http://127.0.0.1:8000";

export const getToken = () => {
  return Cookies.get("token");
};

export const handleResponse = async (res: Response) => {
  if (!res.ok) {
    const msg = await res.text();
    console.error(msg);
    return Promise.reject(new Error("Response error"));
  }

  try {
    return await res.json();
  } catch (error) {
    console.error("Error parsing JSON:", error);
    return Promise.reject(new Error("Error parsing JSON response"));
  }
};

export const uploadImage = async (data: FormData) => {
  try {
    const res = await fetch(`${API_URL}/files/upload`, {
      method: "POST",
      body: data,
    });
    if (!res.ok) {
      return res.statusText;
    }
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const loginAdmin = async (
  phone_number: string,
  password: string
): Promise<string | void> => {
  return fetch(`${API_URL}/login`, {
    method: "POST",
    headers: {
      "Content-type": "application/json",
    },
    body: JSON.stringify({ phone_number, password }),
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
      Cookies.set("token", token, { expires: 50 });
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
  const res = await fetch(`${API_URL}/check_token`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  if (!res.ok) {
    return Promise.reject("Response error");
  }
  return res.json();
};
