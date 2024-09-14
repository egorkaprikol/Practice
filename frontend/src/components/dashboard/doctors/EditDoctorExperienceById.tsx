import React from "react";
import ExperienceForm from "./ExperienceForm";
import { useParams } from "react-router-dom";

const EditDoctorExperienceById = () => {
  const { id } = useParams<{ id: string }>();
  return <ExperienceForm id={id!} method="update"></ExperienceForm>;
};

export default EditDoctorExperienceById;
