export default function InputSubmit({value, color}) {
  return (
    <div className={`cursor-pointer my-4 text-white bg-${color} flex rounded-full justify-center items-center`}>
      <input type="submit" value={value} className="h-10 cursor-pointer w-full"/>
    </div>
  )
}

InputSubmit.defaultProps = {
  value: '',
  color: 'primary'
}