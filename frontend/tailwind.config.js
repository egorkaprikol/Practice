/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#CA740D",
        primary_hover: "#ca6c0d",
        bg: "#f3f3f3",
        item: "#ffffff",
        side: "#1b1b1b",
        secondary: "#C26E09",
      },
    },
  },
  plugins: [],
};
