import { useEffect, useRef, useState } from "react";

import { FaEdit, FaTrashAlt } from "react-icons/fa";
import Button from "../shared/Button";
import { useNavigate } from "react-router-dom";
import {
  DoctorsFilters,
  fetchFilteredDoctors,
} from "../../../services/doctors";
import DoctorsListsFilters from "./DoctorsListsFilters";
import { Doctor } from "../../../types";
import { twMerge } from "tailwind-merge";
const DoctorsList = () => {
  const [data, setData] = useState<Doctor[] | undefined>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [search, setSearch] = useState<DoctorsFilters["search"]>();
  const navigate = useNavigate();

  const handleNavigate = () => {
    navigate("new", { replace: true });
  };
  useEffect(() => {
    const getDoctors = async () => {
      try {
        const doctorsData = await fetchFilteredDoctors({ search });
        setData(doctorsData);
      } catch (error) {
        alert(error);
      } finally {
        setIsLoading(false);
      }
    };
    getDoctors();
  }, [search]);

  if (isLoading) return <div className=""> -- Loading -- </div>;
  return (
    <div className="h-full flex flex-col">
      <div className="pb-5 flex justify-between sticky top-0 bg-white z-10">
        <DoctorsListsFilters
          onChange={(filters) => {
            setSearch(filters.search);
          }}
        />
        <Button onClick={handleNavigate} className="min-w-60">
          Add new doctor
        </Button>
      </div>
      <div
        className={twMerge(
          "grid grid-cols-8 gap-3 pb-4 sticky top-[68px] bg-white z-10"
        )}
      >
        <div className="text-primary flex col-span-3">
          <div className="w-8 text-center">#</div>
          <div className="">Name</div>
        </div>
        <div className="text-primary col-span-2">Number</div>
        <div className="text-primary col-span-2">Profile</div>
        <div className="text-primary flex justify-self-end">Actions</div>
      </div>
      <div className={twMerge("overflow-y-auto hide-scrollbar flex-1")}>
        {data &&
          data.map((doctor, index) => (
            <div
              className="grid grid-cols-8 py-4 gap-3 border-t border-gray-300"
              key={doctor.doctor_phone_number}
            >
              <div className="col-span-3 flex">
                <div className="text-primary w-8 text-center">{index + 1}</div>
                <div className="">
                  {doctor.doctor_name} {doctor.doctor_surname}
                </div>
              </div>
              <div className="col-span-2">{doctor.doctor_phone_number}</div>
              <div className="col-span-2">{doctor.profile_name}</div>
              <div className="flex justify-end gap-5">
                <button>
                  <FaEdit className="text-teal-600" />
                </button>
                <button>
                  <FaTrashAlt className="text-red-600" size={18} />
                </button>
              </div>
            </div>
          ))}
      </div>
    </div>
  );
};

export default DoctorsList;
