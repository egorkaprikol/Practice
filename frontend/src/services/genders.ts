import { Gender } from "../types";
import { API_URL, handleResponse } from "./apiUtils";

export const getGenders = async () => {
  const genders = await fetch(`${API_URL}/genders`).then((res) => {
    return handleResponse(res);
  });
  return genders as Gender[];
};
