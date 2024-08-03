import React from "react";
import { twMerge } from "tailwind-merge";

interface ButtonProps {
  children: React.ReactNode;
  onClick?: () => any;
  type?: "button" | "submit";
  className?: string;
}

const Button = ({
  children,
  className,
  onClick,
  type = "button",
}: ButtonProps) => {
  return (
    <button
      className={twMerge(
        "p-2 rounded-xl text-purple-900 bg-emerald-400 font-bold flex  items-center justify-center w-20 h-10",
        className
      )}
      type={type}
      onClick={onClick}
    >
      {children}
    </button>
  );
};

export default Button;
