export type Doctor = {
  doctor_name: string;
  doctor_surname: string;
  doctor_phone_number: string;
  profile_name: string;
};

export type NewDoctor = {
  name: string;
  surname: string;
  patronymic?: string;
  birth_date: string; // ISO date string, e.g., "2024-08-04"
  gender_id: string; // Используем перечисление Gender
  profile_id: string; // Используем перечисление ProfileId
  login: string;
  password: string;
};

export type Gender = {
  id: string;
  name: string;
  description?: string;
};

export type Profile = {
  id: string;
  name: string;
  description?: string;
};


