import React, { useCallback, useEffect, useState } from "react";
import { DoctorsFilters } from "../../../services/doctors";
import { useDebounce } from "../../../hooks/useDebounce";

type DoctorsListsFiltersProps = {
  onChange: (filters: DoctorsFilters) => void;
};
const DoctorsListsFilters = ({ onChange }: DoctorsListsFiltersProps) => {
  const [search, setSearch] = useState<DoctorsFilters["search"]>("");
  const debouncedSearch = useDebounce(search);
  useEffect(() => {
    onChange({ search: debouncedSearch });
  }, [debouncedSearch]);
  const handleChange = useCallback((e: React.ChangeEvent<HTMLInputElement>) => {
    setSearch(e.target.value);
  }, []);
  return (
    <input
      className="py-1 px-3 my-1 bg-gray-100 border border-primary/30 h-10 rounded-2xl outline-none font-bold text-black w-60"
      type="text"
      value={search}
      onChange={handleChange}
      placeholder="Search doctors"
    />
  );
};

export default DoctorsListsFilters;
