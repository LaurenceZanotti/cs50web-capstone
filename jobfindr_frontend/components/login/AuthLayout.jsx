
export default function AuthLayout(props) {
  return (
    <div className="w-lg m-auto h-screen flex">
        <main className="w-6/12 bg-gray-200">
            {props.children}
            
        </main>
        <aside className="w-6/12 bg-primary/[.6]">
            {/* <div className="w-full h-full bg-cover bg-no-repeat bg-right bg-woman-working"></div> */}
        </aside>
    </div>
  )
}