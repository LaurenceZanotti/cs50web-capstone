
export default function AuthLayout(props) {
  return (
    <div className="text-sm sm:text-sm sm:w-[74em] m-auto h-screen flex">
        <main className="w-full sm:block sm:w-6/12 bg-gray-200">
            {props.children}
        </main>
        <aside className="w-0 sm:block sm:w-6/12 bg-primary/[.6]">
            {/* <div className="w-full h-full bg-cover bg-no-repeat bg-right bg-woman-working"></div> */}
        </aside>
    </div>
  )
}