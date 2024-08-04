import React from "react";
import { twMerge } from "tailwind-merge";

interface ButtonProps {
  children: React.ReactNode;
  onClick?: () => any;
  type?: "button" | "submit";
  className?: string;
  disabled?: boolean;
}

const Button = ({
  children,
  className,
  onClick,
  disabled = false,
  type = "button",
}: ButtonProps) => {
  return (
    <button
      className={twMerge(
        "p-2 rounded-xl text-white bg-primary font-bold flex  items-center justify-center w-20 h-10",
        className
      )}
      type={type}
      disabled={disabled}
      onClick={onClick}
    >
      {children}
    </button>
  );
};

export default Button;
