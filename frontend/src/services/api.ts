const API_URL = "http://127.0.0.1:8000";

export const loginAdmin = async (login: string, password: string) => {
  const res = await fetch(`${API_URL}/login`, {
    method: "POST",
    headers: {
      "Content-type": "application/json",
    },
    body: JSON.stringify({ login, password }),
  }).then((res) => {
    if (!res.ok) {
      console.log("fail");
      throw new Error("invalid data");
    }
    console.log('fine');
    return res.json();
  });
};
