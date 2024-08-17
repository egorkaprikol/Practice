import { toast } from "sonner";
import { Profile } from "../types";
import { API_URL, getToken, handleResponse } from "./apiUtils";

export const getProfiles = async () => {
  const genders = await fetch(`${API_URL}/profiles`).then((res) => {
    return handleResponse(res);
  });
  return genders as Profile[];
};

export const createProfile = async (data: Profile) => {
  const token = getToken();
  try {
    const res = await fetch(`${API_URL}/profiles`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify(data),
    });
    if (!res.ok) {
      toast.error("Couldn`t create profile");
      console.error(res.statusText);
      return;
    }
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const deleteProfileById = async (id: number) => {
  try {
    const res = await fetch(`${API_URL}/prodfiles?profile_id=${id}`);
    if (!res.ok) {
      toast.error("Couldn`t remove profile");
      return;
    }
    return res;
  } catch (error) {
    console.error(error);
  }
};
