import React from "react";
import { twMerge } from "tailwind-merge";

interface ButtonProps {
  children: React.ReactNode;
  onClick: () => any;
}

const Button = ({ children, onClick }: ButtonProps) => {
  return (
    <button
      className={twMerge("bg-cyan-500 p-2 text-white w-20 h-10")}
      onClick={onClick}
    >
      {children}
    </button>
  );
};

export default Button;
