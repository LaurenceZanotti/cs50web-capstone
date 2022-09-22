export default function InputText({icon, type, name, id, placeholder, handleChange, value}) {
  value={value}
  return (
    <div className='my-6 bg-gray-300 flex rounded-full justify-center items-center border hover:border-primary'>
        {icon && icon}
        <input 
            type={type}
            name={name}
            id={id}
            className="
                font-medium
                text-darktext
                w-full
                border-none
                rounded-full
                rounded-l-none
                h-10
                bg-gray-300
                placeholder:text-darktext
                placeholder:font-normal
                outline-none
            " 
            placeholder={placeholder}
            onChange={handleChange}
            value={value}
        />
    </div>
  )
}

