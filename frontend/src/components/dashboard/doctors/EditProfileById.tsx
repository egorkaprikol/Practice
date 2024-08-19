import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { Profile } from "../../../types";
import { getProfileById } from "../../../services/profiles";
import { toast } from "sonner";
import ProfileForm from "./ProfileForm";

const EditProfileById = () => {
  const { id } = useParams<{ id: string }>();
  const [profile, setProfile] = useState<Profile>();

  useEffect(() => {
    const getData = async () => {
      const profile = await getProfileById(id!);
      if (profile) {
        setProfile(profile);
      } else {
        toast.message("Profile not found");
      }
    };
    getData();
  }, [id]);

  return (
    <ProfileForm method="update" id={id} defaultData={profile}></ProfileForm>
  );
};

export default EditProfileById;
