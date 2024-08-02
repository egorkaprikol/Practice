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
    <div
      className={twMerge(
        "p-2 rounded-xl text-purple-900 bg-emerald-400 font-bold flex  items-center justify-center w-20 h-10",
        className
      )}
    >
      <button type={type} onClick={onClick}>
        {children}
      </button>
    </div>
  );
};

export default Button;
