/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
    colors: {
      'primary': '#4D6CFF',
      'secondary': {
        500: '#50CB93',
        300: '#71EFA3',
        100: '#ACFFAD'
      }
    }
  },
  plugins: [],
}
