import { Doctor } from "../types";
import { API_URL, getToken, handleResponse } from "./apiUtils";

export interface DoctorsFilters {
  gender?: "male" | "female";
  search?: string;
}

// Функция для получения всех докторов
export const getDoctors = async (): Promise<Doctor[] | undefined> => {
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

export const getDoctorById = async (
  id: string
): Promise<Doctor | undefined> => {
  try {
    const res = await fetch(`${API_URL}/doctors/:id?doctor_id=${id}`);
    if (!res.ok) {
      return undefined;
    }

    const data = await res.json();

    // Предположим, что `data` — это массив, содержащий один объект `doctor`.
    if (Array.isArray(data) && data.length > 0) {
      return data[0] as Doctor;
    }

    return undefined;
  } catch (error) {
    console.error("Error fetching doctor by ID:", error);
    return undefined;
  }
};

// Функция для получения отфильтрованных докторов
export const getFilteredDoctors = async (
  options?: DoctorsFilters
): Promise<Doctor[] | undefined> => {
  const doctors = await getDoctors();
  if (!doctors) {
    return [];
  }

  let filteredDoctors = doctors;

  if (options?.search) {
    filteredDoctors = filteredDoctors.filter((doctor) => {
      return (
        doctor.name.toLowerCase().includes(options.search!.toLowerCase()) ||
        doctor.surname.toLowerCase().includes(options.search!.toLowerCase())
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
      console.error(res.statusText);
      return false;
    }
    return true;
  } catch (error) {
    console.error(error);
    return false;
  }
};

export const editDoctorById = async (id: string, { ...items }: Doctor) => {
  const token = getToken();
  try {
    const res = await fetch(`${API_URL}/doctors?doctor_id=${id}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ ...items }),
    });
    if (!res.ok) {
      throw new Error("Failed to edit doctor");
    }
    return await res.json();
  } catch (error) {
    console.error("Error creating doctor:", error);
    alert("Failed to create doctor");
    return undefined;
  }
};

// Функция для создания нового доктора
export const createDoctor = async ({
  ...items
}: Doctor): Promise<Doctor | undefined> => {
  const token = getToken();
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
    return await response.json().then((data) => data.Doctor.id);
  } catch (error) {
    console.error("Error creating doctor:", error);
    alert("Failed to create doctor");
    return undefined;
  }
};
