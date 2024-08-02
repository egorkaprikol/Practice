import Cookies from "js-cookie";
import { useNavigate } from "react-router-dom";
import { create } from "zustand";

interface AuthState {
  isAuthenticated: boolean;
  logout: () => void;
  login: () => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  isAuthenticated: false,
  login: () => set({ isAuthenticated: true }),
  logout: () => {
    Cookies.remove("token");
    set({ isAuthenticated: false });
  },
}));
