import React, { useEffect, useState } from "react";
import { Controller, SubmitHandler, useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { format } from "date-fns";
import { Gender, Profile } from "../../../types";
import { useNavigate } from "react-router-dom";
import { createDoctor } from "../../../services/doctors";
import { getGenders } from "../../../services/genders";
import { getProfiles } from "../../../services/profiles";
import Button from "../shared/Button";
import { toast } from "sonner";
import { profile } from "console";
import { playNotification } from "../../../utils/playNotification";

// Схема валидации с помощью zod
const schema = z.object({
  name: z.string().min(2, "Name is required"),
  surname: z.string().min(2, "Surname is required"),
  patronymic: z.string().optional(),
  birth_date: z.date().min(new Date("1900-01-01")).max(new Date()),
  login: z.string().min(6, "Phone number is required"),
  gender_id: z.string().min(1, "Gender is required"), // исправлено на правильное сообщение об ошибке
  profile_id: z.string().min(1, "Profile is required"), // исправлено на правильное сообщение об ошибке
  password: z.string().min(8, "Password must be at least 8 characters long"),
});

type FormFields = z.infer<typeof schema>;

const AddDoctor = () => {
  const navigate = useNavigate();
  const [genders, setGenders] = useState<Gender[]>();
  const [profiles, setProfiles] = useState<Profile[]>();

  useEffect(() => {
    const getGendersData = async () => {
      const data = await getGenders();
      setGenders(data);
    };

    const getProfilesData = async () => {
      const data = await getProfiles();
      setProfiles(data);
      if (data) {
        reset({
          profile_id: String(data[0].id),
        });
      }
    };

    getGendersData();
    getProfilesData();
  }, []);
  const {
    register,
    handleSubmit,
    control,
    setError,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormFields>({
    resolver: zodResolver(schema),
    defaultValues: {
      profile_id: "",
    },
  });

  const onSubmit: SubmitHandler<FormFields> = async (data) => {
    try {
      const formattedData = {
        ...data,
        birth_date: format(new Date(data.birth_date), "yyyy-MM-dd"),
      };
      const res = await createDoctor(formattedData);
      if (res) {
        navigate("/admin/dashboard/doctors");
        playNotification(2);
        toast.success(
          `Doctor ${data.surname} ${data.name} has been successfully added`
        );
      }
    } catch (error) {
      setError("root", {
        message: "Error submit",
      });
    }
  };

  return (
    <div className="px-44">
      <form
        className="grid pt-20 grid-cols-2 w-full gap-x-8 gap-y-2"
        onSubmit={handleSubmit(onSubmit)}
      >
        <div className="flex flex-col">
          <label htmlFor="name" className="font-light">
            First Name*
          </label>
          <input
            id="name"
            className="form-input"
            {...register("name")}
            placeholder="e.g., John"
          />
          {errors.name && (
            <p className="form-label form-label text-sm text-red-500">
              {errors.name.message}
            </p>
          )}
        </div>

        <div className="flex flex-col">
          <label htmlFor="surname" className="form-label">
            Surname*
          </label>
          <input
            id="surname"
            className="form-input"
            {...register("surname")}
            placeholder="e.g., Doe"
          />
          {errors.surname && (
            <p className="form-label form-label text-sm text-red-500">
              {errors.surname.message}
            </p>
          )}
        </div>

        <div className="flex flex-col">
          <label htmlFor="patronymic" className="form-label">
            Patronymic
          </label>
          <input
            id="patronymic"
            className="form-input"
            {...register("patronymic")}
            placeholder="e.g., Ivanovich"
          />
          {errors.patronymic && (
            <p className="form-label form-label text-sm text-red-500">
              {errors.patronymic.message}
            </p>
          )}
        </div>

        <div className="flex flex-col">
          <label htmlFor="birth_date" className="form-label">
            Birth Date*
          </label>
          <Controller
            name="birth_date"
            control={control}
            render={({ field }) => (
              <DatePicker
                selected={field.value}
                onChange={field.onChange}
                dateFormat="yyyy-MM-dd"
                placeholderText="yyyy-MM-dd"
                className="form-input"
              />
            )}
          />
          {errors.birth_date && (
            <p className="form-label form-label text-sm text-red-500">
              {errors.birth_date.message}
            </p>
          )}
        </div>

        <div className="flex flex-col">
          <label htmlFor="login" className="form-label">
            Phone Number*
          </label>
          <input
            id="login"
            className="form-input"
            {...register("login")}
            placeholder="e.g., +7 999 012 1212"
          />
          {errors.login && (
            <p className="form-label form-label text-sm text-red-500">
              {errors.login.message}
            </p>
          )}
        </div>
        <div className="flex flex-col ">
          <label htmlFor="gender" className="form-label pr-4">
            Gender*
          </label>
          <div className="flex gap-4 h-full items-center">
            {genders?.map((gender, index) => (
              <div key={gender.id} className="flex gap-2 font-light">
                <input
                  type="radio"
                  value={gender.id}
                  defaultChecked={index === 0}
                  {...register("gender_id")}
                />
                <label>{gender.name}</label>
              </div>
            ))}
          </div>
          {errors.gender_id && (
            <p className="form-label form-label text-sm text-red-500">
              {errors.gender_id.message}
            </p>
          )}
        </div>

        <div className="flex flex-col">
          <label htmlFor="profile_id" className="form-label">
            Profile
          </label>
          <select
            id="profile_id"
            {...register("profile_id")}
            className="form-input"
          >
            <option disabled value="">
              Select Profile
            </option>
            {profiles?.map((profile) => (
              <option key={profile.id} value={profile.id}>
                {profile.name}
              </option>
            ))}
          </select>
          {errors.profile_id && (
            <p className="form-label form-label text-sm text-red-500">
              {errors.profile_id.message}
            </p>
          )}
        </div>

        <div className="flex flex-col">
          <label htmlFor="password" className="form-label">
            Password*
          </label>
          <input
            id="password"
            type="password"
            className="form-input"
            {...register("password")}
            placeholder="e.g., password123"
          />
          {errors.password && (
            <p className="form-label form-label text-sm text-red-500">
              {errors.password.message}
            </p>
          )}
        </div>

        <Button className="w-40 mt-3" disabled={isSubmitting} type="submit">
          {isSubmitting ? "Loading..." : "Add doctor"}
        </Button>
      </form>
    </div>
  );
};

export default AddDoctor;
