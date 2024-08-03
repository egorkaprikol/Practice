import React, { useEffect, useState } from "react";
import { fetchDoctors } from "../../services/api";
import { Doctor } from "../../types";
import { twMerge } from "tailwind-merge";
import { FaEdit, FaTrashAlt } from "react-icons/fa";
import Button from "../Button";
import { Link, useNavigate } from "react-router-dom";
const DoctorsList = () => {
  const [isLoading, setIsLoading] = useState(true);
  const [doctors, setDoctors] = useState<Doctor[] | undefined>([]);
  const navigate = useNavigate();
  const handleNavigate = () => {
    navigate("new", { replace: true });
  };
  useEffect(() => {
    const getDoctors = async () => {
      try {
        const doctorsData = await fetchDoctors();
        setDoctors(doctorsData);
      } catch (error) {
        alert(error);
      } finally {
        setIsLoading(false);
      }
    };
    getDoctors();
  }, []);
  if (isLoading) return <div className="">Loading</div>;
  return (
    <div className="bg-item h-full rounded-3xl p-5 font-medium text-lg">
      <div className="pb-5 flex justify-between">
        Search
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
      {doctors?.map((doctor, index) => {
        return (
          <div
            className="grid grid-cols-8 py-4 gap-3 border-t border-gray-300"
            key={doctor.doctor_info}
          >
            <div className="col-span-3">
              <span className="px-4 text-primary ">{index + 1}</span>{" "}
              {doctor.doctor_info}
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
