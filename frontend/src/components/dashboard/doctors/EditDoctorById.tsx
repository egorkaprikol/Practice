import React, { useEffect, useState } from "react";
import { Controller, SubmitHandler, useForm } from "react-hook-form";
import { z } from "zod";
import { zodResolver } from "@hookform/resolvers/zod";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { format, parseISO } from "date-fns";
import { Doctor, Gender, Profile } from "../../../types";
import { useNavigate, useParams } from "react-router-dom";
import { editDoctorById, getDoctorById } from "../../../services/doctors";
import { getGenders } from "../../../services/genders";
import { getProfiles } from "../../../services/profiles";
import Button from "../shared/Button";
import { toast } from "sonner";
import { playNotification } from "../../../utils/playNotification";

const schema = z.object({
  name: z.string().min(2, "Name is required"),
  surname: z.string().min(2, "Surname is required"),
  patronymic: z.string().optional(),
  birth_date: z.date().min(new Date("1900-01-01")).max(new Date()),
  gender_id: z.string().min(1, "Gender is required"),
  profile_id: z.string().min(1, "Profile is required"),
});

type FormFields = z.infer<typeof schema>;

const EditDoctor = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const [genders, setGenders] = useState<Gender[]>();
  const [profiles, setProfiles] = useState<Profile[]>();
  const [doctor, setDoctor] = useState<Doctor>();

  const {
    register,
    handleSubmit,
    control,
    setError,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormFields>({
    resolver: zodResolver(schema),
    defaultValues: async () => {
      return {
        name: "",
        surname: "",
        patronymic: "",
        birth_date: new Date(),
        gender_id: "",
        profile_id: "",
      };
    },
  });

  const handleNavigateToExperience = () => {
    navigate(`/admin/dashboard/doctors/${id}/experience`);
  };

  useEffect(() => {
    const getData = async () => {
      try {
        const [gendersData, profilesData, doctorData] = await Promise.all([
          getGenders(),
          getProfiles(),
          getDoctorById(id!),
        ]);

        setGenders(gendersData);
        setProfiles(profilesData);
        setDoctor(doctorData);
        const foundedGender = gendersData.find(
          (gender) => gender.name === doctorData?.gender
        );
        const foundedProfile = profilesData.find(
          (profile) => profile.name === doctorData?.profile_name
        );
        if (doctorData) {
          reset({
            name: doctorData.name,
            surname: doctorData.surname,
            patronymic: doctorData.patronymic,
            birth_date: doctorData.birth_date
              ? parseISO(doctorData.birth_date)
              : undefined,
            gender_id: foundedGender?.id,
            profile_id: String(foundedProfile?.id),
          });
        }
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
    getData();
  }, [id, reset]);

  const onSubmit: SubmitHandler<FormFields> = async (data) => {
    try {
      const formattedData: Doctor = {
        name: data.name,
        surname: data.surname,
        patronymic: data.patronymic,
        birth_date: data.birth_date
          ? format(new Date(data.birth_date), "yyyy-MM-dd")
          : undefined,
        gender_id: data.gender_id,
        profile_id: data.profile_id,
      };
      const res = await editDoctorById(id!, formattedData);
      if (res) {
        navigate("/admin/dashboard/doctors");
        playNotification();
        toast.success(`Profile edited`);
      }
    } catch (error) {
      toast.error("Error");
      setError("root", {
        message: "Error submit",
      });
    }
  };

  return (
    <form
      className="grid xl:px-52 md:px-24 px-6 pt-20 grid-cols-2 w-full gap-x-8 gap-y-2"
      onSubmit={handleSubmit(onSubmit)}
    >
      <p className="text-2xl pb-4 font-semibold col-span-2">
        Edit Doctor's profile
      </p>
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
          <p className=" form-label text-sm text-red-500">
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
      <div className="flex flex-col ">
        <label htmlFor="gender" className="form-label pr-4">
          Gender*
        </label>
        <div className="flex gap-4 h-full items-center">
          {genders?.map((gender) => (
            <div key={gender.id} className="flex gap-2 font-light">
              <input
                type="radio"
                value={gender.id}
                defaultChecked={gender.name === doctor?.gender}
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
          <p className="form-label form-label text-sm text-red-500">
            {errors.profile_id.message}
          </p>
        )}
      </div>
      <Button className=" mt-3 w-full" disabled={isSubmitting} type="submit">
        {isSubmitting ? "Loading..." : "Edit doctor"}
      </Button>
      <Button
        onClick={handleNavigateToExperience}
        className="w-full mt-3 bg-slate-500 hover:bg-slate-600"
      >
        Edit experience →
      </Button>
    </form>
  );
};

export default EditDoctor;
