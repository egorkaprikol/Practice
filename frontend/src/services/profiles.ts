import { Profile } from "../types";
import { API_URL, handleResponse } from "./apiUtils";

export const getProfiles = async () => {
  const genders = await fetch(`${API_URL}/profiles`).then((res) => {
    return handleResponse(res);
  });
  return genders as Profile[];
};
