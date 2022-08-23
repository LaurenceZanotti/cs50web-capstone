
export default function AuthLayout(props) {
  return (
    <div className="text-sm sm:text-sm sm:w-[74em] m-auto h-screen flex">
        <main className="w-full sm:block sm:w-6/12 bg-gray-200">
            {props.children}
        </main>
        <aside className="w-0 sm:block sm:w-6/12 bg-primary/[.6] bg-woman-working bg-blend-soft-light bg-cover bg-right">
        </aside>
    </div>
  )
}