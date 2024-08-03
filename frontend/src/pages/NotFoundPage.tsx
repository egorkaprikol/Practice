import React from "react";
import Button from "../components/Button";
import { useNavigate } from "react-router-dom";

const NotFoundPage = () => {
  const navigate = useNavigate();
  return (
    <div className="flex flex-col items-center justify-center pt-10">
      <p className="font-bold text-2xl p-5">Page not found</p>
      <Button
        className="w-56"
        onClick={() => {
          navigate("/admin");
        }}
      >
        Back to admin page
      </Button>
    </div>
  );
};

export default NotFoundPage;
