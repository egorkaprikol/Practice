import React from "react";

const SearchBar = (
  value: any,
  onChange: (e: React.ChangeEvent<HTMLInputElement>) => void
) => {
  return (
    <input
      type="text"
      onChange={onChange}
      value={value}
      name=""
      id=""
      placeholder="search"
    />
  );
};

export default SearchBar;
