const colors = require('tailwindcss/colors')
const defaultTheme = require('tailwindcss/defaultTheme')

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Roboto', ...defaultTheme.fontFamily.sans],
        'logo': 'Righteous'
      },
      backgroundImage: {
        'hero-wave': "url('/next/index/Wave.svg')",
        'talent-wave': "url('/next/index/HeroWave.svg')",
        'man-working': "url('/next/index/ManWorking.svg')",
        'woman-working': "url('/next/login/working_bg.jpg')",
      }
    },
    colors: {
      transparent: 'transparent',
      current: 'currentColor',
      black: colors.black,
      red: colors.red,
      blue: colors.blue,
      gray: colors.gray,
      white: colors.white,
      slate: colors.slate,
      'primary': '#4D6CFF',
      'secondary': {
        500: '#50CB93',
        300: '#71EFA3',
        100: '#ACFFAD'
      },
      'darktext': '#3F3D56'
    }
  },
  plugins: [],
}
