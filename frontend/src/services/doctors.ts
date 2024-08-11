import { Doctor, NewDoctor } from "../types";
import { API_URL, getToken, handleResponse } from "./apiUtils";

export interface DoctorsFilters {
  gender?: "male" | "female";
  search?: string;
}

// Функция для получения всех докторов
export const fetchDoctors = async (): Promise<Doctor[] | undefined> => {
  try {
    const response = await fetch(`${API_URL}/doctors`);
    if (!response.ok) {
      throw new Error("Failed to fetch doctors");
    }
    const doctorsData: Doctor[] = await response.json();
    return doctorsData;
  } catch (error) {
    console.error("Error fetching doctors:", error);
    alert("Failed to fetch doctors");
    return undefined;
  }
};

// Функция для получения отфильтрованных докторов
export const fetchFilteredDoctors = async (
  options?: DoctorsFilters
): Promise<Doctor[] | undefined> => {
  const doctors = await fetchDoctors();
  if (!doctors) {
    return [];
  }

  let filteredDoctors = doctors;

  if (options?.search) {
    filteredDoctors = filteredDoctors.filter((doctor) => {
      return (
        doctor.doctor_name
          .toLowerCase()
          .includes(options.search!.toLowerCase()) ||
        doctor.doctor_surname
          .toLowerCase()
          .includes(options.search!.toLowerCase())
      );
    });
  }

  return filteredDoctors;
};

export const deleteDoctorById = async (id: number) => {
  try {
    const token = getToken();
    const res = await fetch(`${API_URL}/doctors?doctor_id=${id}`, {
      method: "DELETE",
      headers: { Authorization: `Bearer ${token}` },
    });
    if (!res.ok) {
      return new Error(res.statusText);
    }
    console.log("deleted profile");
  } catch (error) {
    console.error(error);
  }
};

// Функция для создания нового доктора
export const createDoctor = async ({
  ...items
}: NewDoctor): Promise<NewDoctor | undefined> => {
  const token = getToken();
  console.log(token);
  try {
    const response = await fetch(`${API_URL}/doctors`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ ...items }),
    });

    if (!response.ok) {
      throw new Error("Failed to create doctor");
    }

    return await response.json();
  } catch (error) {
    console.error("Error creating doctor:", error);
    alert("Failed to create doctor");
    return undefined;
  }
};
