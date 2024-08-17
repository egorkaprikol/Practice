import React, { useEffect, useState } from "react";
import { useForm, useFieldArray, Controller } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { useNavigate, useParams } from "react-router-dom";
import { format } from "date-fns";
import { playNotification } from "../../../utils/playNotification";
import { toast } from "sonner";
import Button from "../shared/Button";
import { FaPlusCircle, FaTrashAlt } from "react-icons/fa";
import {
  addDoctorsExperienceById,
  getExperienceById,
} from "../../../services/experience";

// Zod schema for validation
const experienceSchema = z.object({
  name: z.string().min(2, "Organization name is required"),
  position: z.string().min(2, "Position is required"),
  start_date: z
    .date({ required_error: "Start date is required" })
    .max(new Date()),
  end_date: z.date({ required_error: "End date is required" }).max(new Date()),
  doctor_id: z.number(),
});

const schema = z.object({
  experiences: z
    .array(experienceSchema)
    .nonempty("At least one experience is required"),
});

type FormFields = z.infer<typeof schema>;

const AddDoctorExperience = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const [dataLoaded, setDataLoaded] = useState(false);
  const {
    register,
    control,
    handleSubmit,
    formState: { errors, isSubmitting, isSubmitted },
    getValues,
    reset,
  } = useForm<FormFields>({
    resolver: zodResolver(schema),
    defaultValues: {
      experiences: [
        {
          name: "",
          position: "",
          start_date: new Date(),
          end_date: new Date(),
          doctor_id: Number(id),
        },
      ],
    },
  });

  const { fields, append, insert, remove } = useFieldArray({
    control,
    name: "experiences",
  });
  const handleDelete = (i: number) => {
    if (getValues().experiences.length > 1) {
      remove(i);
    } else if (i === 0 && getValues().experiences.length <= 1) {
      remove(0);
      insert(0, {
        name: "",
        position: "",
        start_date: new Date(),
        end_date: new Date(),
        doctor_id: Number(id),
      });
    }
  };
  const onSubmit = async (data: FormFields) => {
    try {
      const formattedData = data.experiences.map((item) => ({
        ...item,
        start_date: format(new Date(item.start_date), "yyyy-MM-dd"),
        end_date: format(new Date(item.end_date), "yyyy-MM-dd"),
      }));
      const res = await addDoctorsExperienceById(formattedData);
      if (res) {
        playNotification(2);
        navigate(`/admin/dashboard/doctors`);
        toast.success("Experience has been successfully added");
      }
    } catch (error) {
      console.error("Error adding doctor experience", error);
    }
  };

  useEffect(() => {
    if (!dataLoaded) {
      const getData = async () => {
        const experience = await getExperienceById(id!);
        if (Array.isArray(experience)) {
          const formattedData = experience.map((data) => ({
            ...data,
            start_date: new Date(data.start_date),
            end_date: new Date(data.end_date),
          }));
          reset({ experiences: formattedData });
          setDataLoaded(true);
        }
      };
      getData();
    }
  }, [id, dataLoaded, reset]);

  return (
    <form
      className="pt-16 xl:px-52 md:px-24 px-6 w-full overflow-y-auto h-full"
      onSubmit={handleSubmit(onSubmit)}
    >
      <p className="text-2xl pb-4 font-semibold">Edit Doctor's experience</p>
      {fields.map((item, index) => (
        <div
          key={item.id}
          className="grid grid-cols-2 border-b py-4 border-gray-300 w-full gap-x-8 gap-y-2"
        >
          <div className="flex flex-col">
            <label className="form-label">Organization Name</label>
            <input
              {...register(`experiences.${index}.name`)}
              className="form-input"
              placeholder="Organization name"
            />
            {isSubmitted && errors.experiences?.[index]?.name && (
              <p className="form-label text-sm text-red-500">
                {errors.experiences[index]?.name?.message}
              </p>
            )}
          </div>

          <div className="flex flex-col">
            <label className="form-label">Position</label>
            <input
              {...register(`experiences.${index}.position`)}
              className="form-input"
              placeholder="Position"
            />
            {isSubmitted && errors.experiences?.[index]?.position && (
              <p className="form-label text-sm text-red-500">
                {errors.experiences[index]?.position?.message}
              </p>
            )}
          </div>

          <div className="flex flex-col">
            <label className="form-label">Start Date</label>
            <Controller
              control={control}
              name={`experiences.${index}.start_date`}
              render={({ field }) => (
                <DatePicker
                  selected={field.value}
                  onChange={field.onChange}
                  className="form-input"
                />
              )}
            />
            {isSubmitted && errors.experiences?.[index]?.start_date && (
              <p className="form-label text-sm text-red-500">
                {errors.experiences[index]?.start_date?.message}
              </p>
            )}
          </div>

          <div className="flex flex-col">
            <label className="form-label">End Date</label>
            <Controller
              control={control}
              name={`experiences.${index}.end_date`}
              render={({ field }) => (
                <DatePicker
                  selected={field.value}
                  onChange={field.onChange}
                  className="form-input"
                />
              )}
            />
            {isSubmitted && errors.experiences?.[index]?.end_date && (
              <p className="form-label text-sm text-red-500">
                {errors.experiences[index]?.end_date?.message}
              </p>
            )}
          </div>

          <div className="flex gap-x-3 pt-4">
            <button
              type="button"
              onClick={() =>
                append({
                  name: "",
                  position: "",
                  start_date: new Date(),
                  end_date: new Date(),
                  doctor_id: Number(id),
                })
              }
            >
              <FaPlusCircle size={22} className="text-teal-600" />
            </button>
            <button
              type="button"
              className="place-self-end"
              onClick={() => handleDelete(index)}
            >
              <FaTrashAlt className="text-red-600" size={22} />
            </button>
          </div>
        </div>
      ))}
      <div className="w-full flex justify-end pt-10">
        <Button type="submit" className="w-1/2">
          {isSubmitting ? "Loading..." : "Submit"}
        </Button>
      </div>
    </form>
  );
};

export default AddDoctorExperience;
