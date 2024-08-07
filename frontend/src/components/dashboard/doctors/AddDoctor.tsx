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

// Схема валидации с помощью zod
const schema = z.object({
  name: z.string().min(2, "Name is required"),
  surname: z.string().min(2, "Surname is required"),
  patronymic: z.string().min(2, "2 chars minimum").optional(),
  birth_date: z.date().min(new Date("1900-01-01")).max(new Date()),
  login: z.string().min(6, "Phone number is required"),
  gender_id: z.string().min(1, "Gender is required"), // исправлено на правильное сообщение об ошибке
  profile_id: z.string().min(1, "Profile is required"), // исправлено на правильное сообщение об ошибке
  password: z.string().min(8, "Password must be at least 8 characters long"),
});

type FormFields = z.infer<typeof schema>;

const AddDoctor = () => {
  const {
    register,
    handleSubmit,
    control,
    setError,
    formState: { errors, isSubmitting },
  } = useForm<FormFields>({
    resolver: zodResolver(schema),
  });

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
    };

    getGendersData();
    getProfilesData();
  }, []);

  const onSubmit: SubmitHandler<FormFields> = async (data) => {
    try {
      const formattedData = {
        ...data,
        birth_date: format(new Date(data.birth_date), "yyyy-MM-dd"),
      };
      const res = await createDoctor(formattedData);
      if (res) {
        navigate("/admin/dashboard/doctors");
      }
    } catch (error) {
      setError("root", {
        message: "Error submit",
      });
    }
  };

  return (
    <form
      className="flex flex-col w-full gap-4"
      onSubmit={handleSubmit(onSubmit)}
    >
      <div className="flex items-center gap-4">
        <label htmlFor="name" className="w-32 text-right">
          Name*
        </label>
        <input
          id="name"
          className="form-input"
          {...register("name")}
          placeholder="e.g., John"
        />
        {errors.name && <p className="text-red-500">{errors.name.message}</p>}
      </div>

      <div className="flex items-center gap-4">
        <label htmlFor="surname" className="w-32 text-right">
          Surname*
        </label>
        <input
          id="surname"
          className="form-input"
          {...register("surname")}
          placeholder="e.g., Doe"
        />
        {errors.surname && (
          <p className="text-red-500">{errors.surname.message}</p>
        )}
      </div>

      <div className="flex items-center gap-4">
        <label htmlFor="patronymic" className="w-32 text-right">
          Patronymic
        </label>
        <input
          id="patronymic"
          className="form-input"
          {...register("patronymic")}
          placeholder="e.g., Ivanovich"
        />
        {errors.patronymic && (
          <p className="text-red-500">{errors.patronymic.message}</p>
        )}
      </div>

      <div className="flex items-center gap-4">
        <label htmlFor="birth_date" className="w-32 text-right">
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
          <p className="text-red-500">{errors.birth_date.message}</p>
        )}
      </div>

      <div className="flex items-center gap-4">
        <label htmlFor="login" className="w-32 text-right">
          Phone Number*
        </label>
        <input
          id="login"
          className="form-input"
          {...register("login")}
          placeholder="e.g., +7 999 012 1212"
        />
        {errors.login && <p className="text-red-500">{errors.login.message}</p>}
      </div>

      <div className="flex items-center gap-4">
        <label htmlFor="gender" className="w-32 text-right">
          Gender*
        </label>
        <select id="gender" {...register("gender_id")} className="form-input">
          <option value="" disabled>
            Select Gender
          </option>
          {genders?.map((gender) => (
            <option key={gender.id} value={gender.id}>
              {gender.name}
            </option>
          ))}
        </select>
        {errors.gender_id && (
          <p className="text-red-500">{errors.gender_id.message}</p>
        )}
      </div>

      <div className="flex items-center gap-4">
        <label htmlFor="profile_id" className="w-32 text-right">
          Profile
        </label>
        <select
          id="profile_id"
          {...register("profile_id")}
          className="form-input"
        >
          <option value="" disabled>
            Select Profile
          </option>
          {profiles?.map((profile) => (
            <option key={profile.id} value={profile.id}>
              {profile.name}
            </option>
          ))}
        </select>
        {errors.profile_id && (
          <p className="text-red-500">{errors.profile_id.message}</p>
        )}
      </div>

      <div className="flex items-center gap-4">
        <label htmlFor="password" className="w-32 text-right">
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
          <p className="text-red-500">{errors.password.message}</p>
        )}
      </div>

      <Button className="w-40" disabled={isSubmitting} type="submit">
        {isSubmitting ? "Loading..." : "Add doctor"}
      </Button>
    </form>
  );
};

export default AddDoctor;
