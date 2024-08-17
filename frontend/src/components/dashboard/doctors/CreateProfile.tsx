import { zodResolver } from "@hookform/resolvers/zod";
import React from "react";
import { SubmitHandler, useForm } from "react-hook-form";
import { z } from "zod";
import { createProfile } from "../../../services/profiles";
import Button from "../shared/Button";
import { toast } from "sonner";
import { useNavigate } from "react-router-dom";

const schema = z.object({
  name: z.string().min(2, "Name is required"),
  description: z.string().optional(),
});
type FormFields = z.infer<typeof schema>;

const CreateProfile = () => {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
    setError,
  } = useForm<FormFields>({
    resolver: zodResolver(schema),
  });
  const navigate = useNavigate();
  const onSubmit: SubmitHandler<FormFields> = async (data) => {
    try {
      if (data.description === undefined) {
        data.description = "";
      }
      const res = await createProfile(data);
      if (!res) {
        return;
      }
      navigate("/admin/dashboard/profiles");
      toast.success("Profile created");
    } catch (error) {
      console.error(error);
    }
  };
  return (
    <form
      className="xl:px-52 md:px-24 px-6 grid pt-16 grid-cols-2 w-full gap-x-8 gap-y-2"
      onSubmit={handleSubmit(onSubmit)}
    >
      <p className="text-2xl pb-4 font-semibold col-span-2">Create Profile</p>
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
          {isSubmitting ? "Loading..." : "Create Profile"}
        </Button>
      </div>
    </form>
  );
};

export default CreateProfile;
