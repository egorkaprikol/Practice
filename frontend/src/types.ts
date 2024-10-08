export type Doctor = {
  id?: number;
  name: string;
  surname: string;
  patronymic?: string;
  birth_date?: string; // ISO e.g., "2024-08-04"
  gender?: string;
  profile_name?: string;
  phone_number?: string;
  password?: string;
  gender_id?: string;
  profile_id?: string;
};

export type Gender = {
  id: string;
  name: string;
  description?: string;
};

export type Profile = {
  id?: number;
  name: string;
  description?: string;
};

export type Experience = {
  name: string;
  id?: number;
  position: string;
  start_date: string | Date;
  end_date: string | Date;
  doctor_id: number;
};
