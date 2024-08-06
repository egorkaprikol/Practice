import React, { useCallback, useEffect, useState } from "react";
import { DoctorsFilters } from "../../services/doctors";
import { useDebounce } from "../../hooks/useDebounce";

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
      type="text"
      value={search}
      //   onChange={(e) => setSearch(e.target.value)}
      onChange={handleChange}
      placeholder="text"
    />
  );
};

export default DoctorsListsFilters;
