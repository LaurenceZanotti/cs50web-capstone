// Libraries
import { UserCircle, LockSimple } from 'phosphor-react'

// Icons
import GoogleIcon from "../components/login/icons/GoogleIcon";
import FacebookIcon from "../components/login/icons/FacebookIcon";
import LinkedinIcon from "../components/login/icons/LinkedinIcon";

// Components
import AuthLayout from "../components/login/AuthLayout";
import AuthHeader from "../components/login/AuthHeader";
import InputText from "../components/login/InputText";
import InputSubmit from "../components/login/InputSubmit";

export default function Login() {
  return (
    <div>
        <AuthLayout>
            <AuthHeader/>
            <form action="" method="post" className="w-80 m-auto">
                <InputText 
                    icon={<UserCircle size={28} color="black" weight="fill" className='mx-4'/>} 
                    name="username"
                    id="username"
                    placeholder="Username"
                />
                <InputText 
                    icon={<LockSimple size={28} color="black" weight="fill" className='mx-4'/>} 
                    name="password"
                    id="password"
                    type="password"
                    placeholder="Password"
                />
                <InputSubmit value="Log in"/>
            </form>
            <div className='text-center mt-0 mb-10 leading-8'>
                <p>I forgot my <a href="" className="text-primary font-medium">password</a></p>
                <p>Don't have an account?
                    <a href="" className='text-secondary-500 font-medium ml-1'>Create one</a>
                </p>
                <p>or</p>
                <p>Continue with a social network</p>
            </div>
            <div className='flex justify-center gap-x-14'>
                <a href="">
                    <GoogleIcon />
                </a>
                <a href="">
                    <FacebookIcon />
                </a>
                <a href="">
                    <LinkedinIcon />
                </a>
            </div>
        </AuthLayout>
    </div>
  )
}