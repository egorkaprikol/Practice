import { twMerge } from "tailwind-merge";

interface BoxProps {
  children: React.ReactNode;
  className?: string;
}

export const Box = ({ children, className }: BoxProps) => {
  return (
    <div className={twMerge("bg-neutral-300 h-fit w-full", className)}>
      {children}
    </div>
  );
};
