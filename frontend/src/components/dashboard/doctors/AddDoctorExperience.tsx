import { useForm, useFieldArray, Controller } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import { useParams } from "react-router-dom";

// Zod Schema for validation
const experienceSchema = z.object({
  name: z.string().min(2, "Organization name is required"),
  position: z.string().min(2, "Position is required"),
  start_date: z.date({ required_error: "Start date is required" }),
  end_date: z.date({ required_error: "End date is required" }),
});

const schema = z.object({
  experiences: z
    .array(experienceSchema)
    .nonempty("At least one experience is required"),
});

type FormFields = z.infer<typeof schema>;

const AddDoctorExperience = () => {
  const { id } = useParams<{ id: string }>();
  const {
    register,
    control,
    handleSubmit,
    formState: { errors },
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
        },
      ],
    },
  });

  const { fields, append, remove } = useFieldArray({
    control,
    name: "experiences",
  });

  const onSubmit = (data: FormFields) => {
    console.log(data);
  };

  return (
    <form className="overflow-y-auto" onSubmit={handleSubmit(onSubmit)}>
      {fields.map((item, index) => (
        <div key={item.id} className="mb-4 p-4 border border-gray-300 rounded">
          <div>
            <label className="block mb-1">Organization Name</label>
            <input
              {...register(`experiences.${index}.name`)}
              className="form-input"
              placeholder="Organization name"
            />
            {errors.experiences?.[index]?.name && (
              <p className="text-red-500 text-sm">
                {errors.experiences[index]?.name?.message}
              </p>
            )}
          </div>

          <div>
            <label className="block mb-1">Position</label>
            <input
              {...register(`experiences.${index}.position`)}
              className="form-input"
              placeholder="Position"
            />
            {errors.experiences?.[index]?.position && (
              <p className="text-red-500 text-sm">
                {errors.experiences[index]?.position?.message}
              </p>
            )}
          </div>

          <div>
            <label className="block mb-1">Start Date</label>
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
            {errors.experiences?.[index]?.start_date && (
              <p className="text-red-500 text-sm">
                {errors.experiences[index]?.start_date?.message}
              </p>
            )}
          </div>

          <div>
            <label className="block mb-1">End Date</label>
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
            {errors.experiences?.[index]?.end_date && (
              <p className="text-red-500 text-sm">
                {errors.experiences[index]?.end_date?.message}
              </p>
            )}
          </div>

          <button
            type="button"
            onClick={() => remove(index)}
            className="mt-2 text-red-500"
          >
            Remove Experience
          </button>
        </div>
      ))}

      <button
        type="button"
        onClick={() =>
          append({
            name: "",
            position: "",
            start_date: new Date(),
            end_date: new Date(),
          })
        }
      >
        + Add Experience
      </button>

      <button
        type="submit"
        className="mt-4 bg-blue-500 text-white py-2 px-4 rounded"
      >
        Submit
      </button>
    </form>
  );
};

export default AddDoctorExperience;
