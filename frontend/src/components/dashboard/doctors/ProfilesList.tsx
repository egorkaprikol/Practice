import { useEffect, useState } from "react";

import { FaEdit, FaTrashAlt } from "react-icons/fa";
import Button from "../shared/Button";
import { useNavigate } from "react-router-dom";
import { deleteProfileById, getProfiles } from "../../../services/profiles";
import { Profile } from "../../../types";
import { twMerge } from "tailwind-merge";
import { toast } from "sonner";
import { playNotification } from "../../../utils/playNotification";
const ProfilesList = () => {
  const [data, setData] = useState<Profile[] | undefined>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [refresh, setRefresh] = useState(false);
  const navigate = useNavigate();

  const handleDeleteProfile = async (id: number) => {
    try {
      const res = await deleteProfileById(id);
      if (res) {
        setRefresh(!refresh); // Обновляем состояние, чтобы компонент перерисовался
        playNotification(3);
        toast.success("Profile removed");
      }
    } catch (error) {
      console.error("deleting profile error:", error);
    }
  };

  const handleNavigateToEdit = (id: number) => {
    navigate(`${id}/edit`, { replace: true });
  };

  const handleNavigate = () => {
    navigate("new", { replace: true });
  };
  useEffect(() => {
    const getProfilesData = async () => {
      try {
        const profilesData = await getProfiles();
        setData(profilesData);
      } catch (error) {
        alert(error);
      } finally {
        setIsLoading(false);
      }
    };
    getProfilesData();
  }, []);

  if (isLoading) return <div className=""> -- Loading -- </div>;
  return (
    <div className="h-full flex flex-col">
      <div className="pb-5 flex justify-between items-center sticky top-0 bg-white z-10">
        <p className="font-semibold text-2xl place-self-center">Profiles</p>
        <Button onClick={handleNavigate} className=" w-60 py-1 px-3 my-1 h-10">
          Add new profile
        </Button>
      </div>
      <div
        className={twMerge(
          "grid grid-cols-5 gap-3 pb-4 sticky top-[68px] bg-white z-10"
        )}
      >
        <div className="text-primary flex col-span-2">
          <div className="w-8 text-center">#</div>
          <div className="">Name</div>
        </div>
        <div className="text-primary col-span-2">Description</div>
        <div className="text-primary flex justify-self-end">Actions</div>
      </div>
      <div className={twMerge("overflow-y-auto hide-scrollbar flex-1")}>
        {data &&
          data.map((profile, index) => (
            <div
              className="grid grid-cols-5 py-4 gap-3 border-t border-gray-300"
              key={profile.id}
            >
              <div className="col-span-2 flex">
                <div className="text-primary w-8 text-center">{index + 1}</div>
                <div className="">{profile.name}</div>
              </div>
              <div className="col-span-2">{profile.description}</div>
              <div className="flex justify-end gap-5">
                <button onClick={() => handleNavigateToEdit(profile.id!)}>
                  <FaEdit className="text-teal-600" />
                </button>
                <button onClick={() => handleDeleteProfile(profile.id!)}>
                  <FaTrashAlt className="text-red-600" size={18} />
                </button>
              </div>
            </div>
          ))}
      </div>
    </div>
  );
};

export default ProfilesList;
