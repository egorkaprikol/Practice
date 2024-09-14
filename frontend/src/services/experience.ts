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

export const editDoctorsExperienceById = async (
  items: Experience[],
  id: string
) => {
  const res = await deleteDoctorsExperienceById(id).then(() =>
    addDoctorsExperienceById(items)
  );
  return res;
};

export const deleteDoctorsExperienceById = async (id: string) => {
  console.log(id);
  try {
    const token = getToken();
    const res = await fetch(`${API_URL}/experiences/doctor_id=${id}`, {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    console.log(res.statusText);
    console.log(res);
    return res;
  } catch (error) {
    console.error(error);
    return;
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
