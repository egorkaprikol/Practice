import { zodResolver } from "@hookform/resolvers/zod";
import React, { useEffect, useState } from "react";
import { SubmitHandler, useForm } from "react-hook-form";
import { z } from "zod";
import { createProfile, editProfileById } from "../../../services/profiles";
import Button from "../shared/Button";
import { toast } from "sonner";
import { useNavigate } from "react-router-dom";
import { Profile } from "../../../types";

const schema = z.object({
  name: z.string().min(2, "Name is required"),
  description: z.string().optional(),
});
type FormFields = z.infer<typeof schema>;

interface ProfileFormProps {
  redirectURL?: string;
  method: "create" | "update";
  id?: string;
  defaultData?: Profile;
}

const ProfileForm = ({ defaultData, method, id }: ProfileFormProps) => {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormFields>({
    resolver: zodResolver(schema),
  });
  const [isLoading, setIsLoading] = useState(true);
  useEffect(() => {
    if (method === "update" && id !== undefined && defaultData) {
      reset(defaultData);
      setIsLoading(false);
    } else if (method === "create") setIsLoading(false);
  }, [id, defaultData, reset, method, isLoading]);
  const navigate = useNavigate();
  const handleSucess = (res?: boolean) => {
    if (res) {
      navigate("/admin/dashboard/profiles");
      toast.success(`Profile ${method === "update" ? "updated" : "created"}`);
    } else toast.error("Failed");
  };
  const onSubmit: SubmitHandler<FormFields> = async (data) => {
    try {
      if (data.description === undefined) {
        data.description = "";
      }
      switch (method) {
        case "create":
          {
            const res = await createProfile(data);
            handleSucess(res?.ok);
          }
          break;
        case "update":
          if (id) {
            const res = await editProfileById(id, data);
            handleSucess(res?.ok);
          }
          break;
        default:
          break;
      }
    } catch (error) {
      console.error(error);
    }
  };
  if (isLoading) {
    return <div className="">loading</div>;
  }
  return (
    <form
      className="xl:px-52 md:px-24 px-6 grid pt-16 grid-cols-2 w-full gap-x-8 gap-y-2"
      onSubmit={handleSubmit(onSubmit)}
    >
      <p className="text-2xl pb-4 font-semibold col-span-2">
        {method === "create" ? "Create Profile" : "Edit Profile"}
      </p>
      <div className="flex flex-col">
        <label htmlFor="name" className="form-label">
          Profile name*
        </label>
        <input
          id="name"
          className="form-input"
          {...register("name")}
          placeholder="profile"
        />
        {errors.name && (
          <p className="form-label text-sm text-red-500">
            {errors.name.message}
          </p>
        )}
      </div>
      <div className="flex flex-col">
        <label htmlFor="description" className="form-label">
          Profile's description*
        </label>
        <input
          id="description"
          className="form-input"
          {...register("description")}
          placeholder="profile's description"
        />
        {errors.description && (
          <p className="form-label text-sm text-red-500">
            {errors.description.message}
          </p>
        )}
      </div>
      <div className="flex items-end justify-center">
        <Button
          className="w-full mt-3 my-1"
          disabled={isSubmitting}
          type="submit"
        >
          {isSubmitting
            ? "Loading..."
            : method === "create"
            ? "Create Profile"
            : "Update Profile"}
        </Button>
      </div>
    </form>
  );
};

export default ProfileForm;
