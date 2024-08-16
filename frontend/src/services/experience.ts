import { Experience } from "../types";
import { API_URL, getToken } from "./apiUtils";

export const addDoctorsExperienceById = async (items: Experience[]) => {
  try {
    const token = getToken();
    const res = fetch(`${API_URL}/experiences`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify(items),
    });
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const getExperienceById = async (id: string) => {
  try {
    const res = await fetch(`${API_URL}/experiences/get_by_doctor_id/${id}`);
    if (!res.ok) {
      return res.statusText;
    }
    const data = await res.json();
    return data as Experience[];
  } catch (error) {}
};
