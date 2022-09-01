// Built in
import Head from 'next/head'
import { useState } from 'react';

// Libraries
import { UserCircle, LockSimple, Envelope, Repeat } from 'phosphor-react'

// Icons
import GoogleIcon from "../../components/login/icons/GoogleIcon";
import FacebookIcon from "../../components/login/icons/FacebookIcon";
import LinkedinIcon from "../../components/login/icons/LinkedinIcon";

// Components
import AuthLayout from "../../components/login/AuthLayout";
import AuthHeader from "../../components/login/AuthHeader";
import InputText from "../../components/login/InputText";
import InputSubmit from "../../components/login/InputSubmit";
import UserTypeModal from "../../components/register/UserTypeModal";



export default function Register() {

    // Open or close UserTypeModal
    const [open, setOpen] = useState(true)
    
    // Type of user
    const [userType, setUserType] = useState("jobseeker")

    function handleUserType(chosenUserType = "jobseeker") {
        setUserType(chosenUserType)
    }

    function handleModalUserType(ev) {
        ev.preventDefault()
        setOpen(true)
    }

    return (
        <>
        <Head>
            <title>Register | Jobfindr</title>
        </Head>
        <div>
            <AuthLayout>
                <UserTypeModal handleUserType={handleUserType} open={open} setOpen={setOpen}/>
                <AuthHeader/>
                <h2 className='font-medium text-lg my-2 w-80 m-auto text-center'>Creating your account</h2>
                <form action="" method="post" className="w-80 m-auto">
                    <InputText 
                        icon={<UserCircle size={28} color="black" weight="fill" className='mx-4'/>} 
                        name="username"
                        id="username"
                        placeholder="Username"
                    />
                    <InputText 
                        icon={<Envelope size={28} color="black" weight="fill" className='mx-4'/>} 
                        name="email"
                        id="email"
                        type="email"
                        placeholder="Email"
                    />
                    <InputText 
                        icon={<LockSimple size={28} color="black" weight="fill" className='mx-4'/>} 
                        name="password"
                        id="password"
                        type="password"
                        placeholder="Password"
                    />
                    <InputText 
                        icon={<Repeat size={28} color="black" weight="fill" className='mx-4'/>} 
                        name="cpassword"
                        id="cpassword"
                        type="password"
                        placeholder="Confirm your password"
                    />
                    <input type="hidden" name="usertype" id="usertype" value={userType}/>
                    <div className='w-80 m-auto flex justify-between items-center rounded-full bg-gray-300 py-2 px-4 mb-6 border hover:border-primary'>
                        <div>I'm looking for: {
                            userType == 'jobseeker' ? 
                            <span className="text-primary font-medium">jobs</span> :
                            <span className="text-primary font-medium">talents</span>
                            }
                        </div>
                        <button 
                            className="block border border-primary rounded-md px-2 hover:bg-primary hover:text-white transition-colors"
                            onClick={ev => {
                                handleModalUserType(ev)
                            }}
                        >
                            Change
                        </button>
                    </div>
                    <InputSubmit value="Register" className="bg-secondary-500"/>
                </form>
                <div className='text-center mt-0 mb-10 leading-8'>
                    <p>Already have an account?
                        <a href="/login" className='text-primary font-medium ml-1'>Sign in</a>
                    </p>
                    <p>or</p>
                    <p>Register using a social network</p>
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
        </>
    )
}