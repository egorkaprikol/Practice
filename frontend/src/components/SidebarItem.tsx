import { IconType } from "react-icons";
import { Link } from "react-router-dom";
import { twMerge } from "tailwind-merge";

interface SidebarItemProps {
  //   icon: IconType;
  label: string;
  active?: boolean;
  href: string;
}

export const SidebarItem = ({
  //   icon: Icon,
  label,
  active,
  href,
}: SidebarItemProps) => {
  return (
    <Link
      to={href}
      className={twMerge(
        "flex bg-gray-300 flex-row h-auto items-center gap-x-4 font-semibold cursor-pointer hover:text-white transition text-lg text-neutral-400 py-2",
        active && "text-red-700"
      )}
    >
      {/* <Icon size={26}></Icon> */}
      <p className="w-full px-3 ">{label}</p>
    </Link>
  );
};
