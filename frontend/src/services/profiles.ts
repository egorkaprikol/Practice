import { toast } from "sonner";
import { Profile } from "../types";
import { API_URL, getToken, handleResponse } from "./apiUtils";

export const getProfiles = async () => {
  const profiles = await fetch(`${API_URL}/profiles`).then((res) => {
    return handleResponse(res);
  });
  return profiles as Profile[];
};
export const getProfileById = async (id: string) => {
  const profile = await fetch(`${API_URL}/profiles/${id}`).then((res) => {
    return handleResponse(res);
  });
  return profile as Profile;
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

export const editProfileById = async (id: string, data: Profile) => {
  try {
    const token = getToken();
    const res = await fetch(`${API_URL}/profiles?profile_id=${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify(data),
    });
    if (!res.ok) {
      toast.error(res.statusText);
      return;
    }
    return res;
  } catch (error) {
    console.error(error);
  }
};

export const deleteProfileById = async (id: number) => {
  try {
    const token = getToken();
    const res = await fetch(`${API_URL}/profiles?profile_id=${id}`, {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    if (!res.ok) {
      toast.error("Couldn`t remove profile");
      return;
    }
    return res;
  } catch (error) {
    console.error(error);
  }
};
