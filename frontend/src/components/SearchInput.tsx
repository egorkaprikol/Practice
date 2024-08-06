import React from "react";

interface SearchInputProps {
  value: string;
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

const SearchInput = ({ onChange, value }: SearchInputProps) => {
  return (
    <div>
      <input type="text" value={value} onChange={onChange} />
    </div>
  );
};

export default SearchInput;
