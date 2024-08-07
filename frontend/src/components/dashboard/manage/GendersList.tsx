import { useEffect, useState } from "react";

import { FaEdit, FaTrashAlt } from "react-icons/fa";
import Button from "../shared/Button";
import { useNavigate } from "react-router-dom";
import { Gender } from "../../../types";
import { getGenders } from "../../../services/genders";
const GendersList = () => {
  const [data, setData] = useState<Gender[] | undefined>([]);
  const [isLoading, setIsLoading] = useState(true);
  // const [search, setSearch] = useState<gendersFilters["search"]>();
  const navigate = useNavigate();

  const handleNavigate = () => {
    navigate("new", { replace: true });
  };

  useEffect(() => {
    const getGendersData = async () => {
      try {
        const gendersData = await getGenders();
        setData(gendersData);
      } catch (error) {
        alert(error);
      } finally {
        setIsLoading(false);
      }
    };
    getGendersData();
  }, []);

  if (isLoading) return <div className=""> -- Loading -- </div>;
  return (
    <div className="">
      <div className="pb-5 flex justify-between">
        <Button onClick={handleNavigate} className="min-w-60">
          Add new gender
        </Button>
      </div>
      <div className="grid grid-cols-8 gap-3 pb-4">
        <div className="text-primary col-span-3">
          {" "}
          <span className="px-4">#</span> Name
        </div>
        <div className="text-primary col-span-2">Number</div>
        <div className="text-primary col-span-2">Profile</div>
        <div className="text-primary flex justify-self-end">Actions</div>
      </div>
      {data &&
        data.map((gender, index) => {
          return (
            <div
              className="grid grid-cols-2 py-4 gap-3 border-t border-gray-300"
              key={gender.id}
            >
              <div className="col-span-3">
                <span className="px-4 text-primary ">{index + 1}</span>{" "}
                {gender.name}
              </div>
              <div className="flex justify-end gap-5">
                <button>
                  <FaEdit className="text-teal-600" />
                </button>
                <button>
                  <FaTrashAlt className="text-red-600" size={18}></FaTrashAlt>
                </button>
              </div>
            </div>
          );
        })}
    </div>
  );
};

export default GendersList;
