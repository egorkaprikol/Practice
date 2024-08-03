import { IconType } from "react-icons";
import { Link } from "react-router-dom";
import { twMerge } from "tailwind-merge";

interface SidebarItemProps {
  icon: IconType;
  label: string;
  active?: boolean;
  href: string;
}

export const SidebarItem = ({
  icon: Icon,
  label,
  active,
  href,
}: SidebarItemProps) => {
  return (
    <Link
      to={href}
      className={twMerge(
        "flex flex-row h-auto items-center hover:text-white/70 gap-x-2 font-semibold cursor-pointer text-white transition text-lg py-2",
        active && "text-primary hover:text-primary"
      )}
    >
      <Icon size={18}></Icon>
      <p className="w-full px-1 truncate">{label}</p>
    </Link>
  );
};
