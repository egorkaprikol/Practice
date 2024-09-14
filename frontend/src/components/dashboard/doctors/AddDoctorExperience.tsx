import React from "react";
import { useParams } from "react-router-dom";
import ExperienceForm from "./ExperienceForm";

const AddDoctorExperience = () => {
  const { id } = useParams<{ id: string }>();
  return <ExperienceForm id={id!} method="create"></ExperienceForm>;
};

export default AddDoctorExperience;
