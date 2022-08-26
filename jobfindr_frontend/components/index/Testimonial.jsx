export default function Testimonial({name, role, img_src, children}) {
  return (
    <div className="bg-white border border-gray-300 rounded-2xl mb-8 mx-16 sm:mx-8">
        <div className="text-center m-4">
            <img src={img_src} alt="Testimonial profile picture" className="rounded-full w-16 m-auto my-4"/>
            <div className="font-bold text-primary">{name}</div>
            <div className="font-bold text-secondary-500">{role}</div>
        </div>
        <div className="font-medium text-justify m-4">
            {children}
        </div>
    </div>
  )
}