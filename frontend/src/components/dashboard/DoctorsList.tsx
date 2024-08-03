import React, { useEffect, useState } from "react";
import { fetchDoctors } from "../../services/api";
import { Doctor } from "../../types";

const DoctorsList = () => {
  const [isLoading, setIsLoading] = useState(true);
  const [doctors, setDoctors] = useState<Doctor[] | undefined>([]);
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
  return (
    <div>
      {isLoading
        ? " loading "
        : doctors!.map((doctor) => {
            return (
              <div className="" key={doctor.doctor_info}>
                {doctor.doctor_info}
                {doctor.profile_name}
              </div>
            );
          })}
    </div>
  );
};

export default DoctorsList;
