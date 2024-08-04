export type Doctor = {
  doctor_info: string;
  doctor_phone_number: string;
  profile_name: string;
};

export type NewDoctor = {
  name: string;
  surname: string;
  patronymic: string;
  birth_date: string; // ISO date string, e.g., "2024-08-04"
  phone_number: string;
  gender: Gender; // Используем перечисление Gender
  profile_id: ProfileId; // Используем перечисление ProfileId
  login: string;
  password: string;
};

// Перечисление для gender
export enum Gender {
  Male = "male",
  Female = "female",
}

// Перечисление для profile_id
export enum ProfileId {
  Surgeon = "surgeon",
  Rapper = "raper",
  Oxxy = "oksi",
}