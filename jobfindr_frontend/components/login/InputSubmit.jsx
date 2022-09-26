import { CircleNotch } from 'phosphor-react'

export default function InputSubmit({value, color, disabled}) {
  return (
    <div className={`cursor-pointer my-4 text-white bg-${color} flex rounded-full justify-center items-center ${disabled && 'transition-opacity duration-200 ease-in opacity-75'}`}>
      {disabled ? 
      <CircleNotch size="32" className='animate-spin my-1'/> :
      <input type="submit" value={value} className={`h-10 cursor-pointer w-full ${disabled && 'disabled:opacity-75'}`} disabled={disabled && "disabled"}/>
      }
    </div>
  )
}

InputSubmit.defaultProps = {
  value: '',
  color: 'primary',
  disabled: false
}