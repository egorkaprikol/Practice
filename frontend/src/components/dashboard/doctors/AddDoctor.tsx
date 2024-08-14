import { useNavigate } from "react-router-dom";
import CreateDoctorProfile from "./CreateDoctorProfile";
import { useState } from "react";

const AddDoctor = () => {
  const navigate = useNavigate();
  const [isAdding, setIsAdding] = useState(true);

  return (
    <div className="px-44">
      <CreateDoctorProfile></CreateDoctorProfile>
    </div>
  );
};

export default AddDoctor;
