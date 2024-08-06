import { useEffect, useState } from "react";

import { FaEdit, FaTrashAlt } from "react-icons/fa";
import Button from "../Button";
import { useNavigate } from "react-router-dom";
import { DoctorsFilters, fetchFilteredDoctors } from "../../services/doctors";
import { useQuery } from "@tanstack/react-query";
import DoctorsListsFilters from "./DoctorsListsFilters";
import { Doctor } from "../../types";
const DoctorsList = () => {
  // const [isLoading, setIsLoading] = useState(true);
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
    <div className="">
      <div className="pb-5 flex justify-between">
        <DoctorsListsFilters
          onChange={(filters) => {
            setSearch(filters.search);
          }}
        ></DoctorsListsFilters>
        <Button onClick={handleNavigate} className="min-w-60">
          Add new doctor
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
        data.map((doctor, index) => {
          return (
            <div
              className="grid grid-cols-8 py-4 gap-3 border-t border-gray-300"
              key={doctor.doctor_phone_number}
            >
              <div className="col-span-3">
                <span className="px-4 text-primary ">{index + 1}</span>{" "}
                {doctor.doctor_name} {doctor.doctor_surname}
              </div>
              <div className="col-span-2">{doctor.doctor_phone_number}</div>
              <div className="col-span-2">{doctor.profile_name}</div>
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

export default DoctorsList;
