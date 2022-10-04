// Libraries
import { UserCircle, List} from "phosphor-react"
import { useEffect, useState } from "react"

// Global components
import DropdownMenu from "../DropdownMenu"

export default function Header(props) {
    const [user, setUser] = useState(null)

    useEffect(() => {
        fetch('/api/user')
            .then(res => res.json())
            .then(({user}) => setUser(user))
    }, [])
    
    return (
        <nav className="bg-blue-700 flex items-center justify-between h-12 py-1">
            {/* Mobile menu */}
            <div className="sm:hidden" id="mobile-menu">
                <DropdownMenu
                    icon={<List size={20} color={"#71EFA3"} />}
                    list_options={["Log in", "Sign up"]}
                    list_hrefs={["login", "register"]}
                />
            </div>
            {/* Logo */}
            <div className="sm:block border-solid sm:border-r-2 sm:border-r-secondary-300" id="logo">
                <h1 className='font-logo text-primary text-4xl mx-3'>
                Job
                <span className='text-secondary-500'>findr</span>
                </h1>
            </div>
            <div className="hidden sm:block" id="nav-options">
                {props.children}
            </div>
            <div className="flex items-center border-solid border-l-2 border-l-secondary-300 h-full" id="nav-account">
                <div className="mx-2" id="avatar-container">
                    <UserCircle size={32} color="white" />
                    {/* TODO: Use profile picture if user has one */}
                </div>
                <div className="text-white mr-2" id="account-username">
                    {user && user.username}
                </div>
            </div>
        </nav>
    )
}