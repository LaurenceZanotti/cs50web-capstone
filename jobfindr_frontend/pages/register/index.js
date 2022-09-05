// Built in
import Head from 'next/head'
import { useState } from 'react';

// Libraries
import { UserCircle, LockSimple, Envelope, Repeat } from 'phosphor-react'
import { useFormik } from 'formik';

// Icons
import GoogleIcon from "../../components/login/icons/GoogleIcon";
import FacebookIcon from "../../components/login/icons/FacebookIcon";
import LinkedinIcon from "../../components/login/icons/LinkedinIcon";

// Components
import AuthLayout from "../../components/login/AuthLayout";
import AuthHeader from "../../components/login/AuthHeader";
import InputSubmit from "../../components/login/InputSubmit";
import UserTypeModal from "../../components/register/UserTypeModal";
import FormErrorMessage from "../../components/auth/FormErrorMessage";


export default function Register() {

    // Open or close UserTypeModal
    const [open, setOpen] = useState(true)

    function handleUserType(chosenUserType = "jobseeker") {
        formik.setFieldValue('usertype', chosenUserType, false)
    }

    function handleModalUserType(ev) {
        ev.preventDefault()
        setOpen(true)
    }

    const formik = useFormik({
        initialValues: {
            username: '',
            email: '',
            password: '',
            cpassword: '',
            usertype: 'jobseeker',
        },
        onSubmit: values => {
            console.log(values)
        },
        validate
    })

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
                <form onSubmit={formik.handleSubmit} action="" method="post" className="w-80 m-auto">
                    {/* Username input */}
                    {
                        formik.touched.username && formik.errors.username ? 
                        <FormErrorMessage>{formik.errors.username}</FormErrorMessage> : 
                        null
                    }
                    <div className='my-6 bg-gray-300 flex rounded-full justify-center items-center border hover:border-primary'>
                        <UserCircle size={28} color="black" weight="fill" className='mx-4'/>
                        <input 
                            type="username"
                            name="username"
                            id="username"
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
                            placeholder="Username"
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur}
                            value={formik.values.username}
                        />
                    </div>
                    {/* Email input */}
                    {
                        formik.touched.email && formik.errors.email ? 
                        <FormErrorMessage>{formik.errors.email}</FormErrorMessage> : 
                        null
                    }
                    <div className='my-6 bg-gray-300 flex rounded-full justify-center items-center border hover:border-primary'>
                        <LockSimple size={28} color="black" weight="fill" className='mx-4'/>
                        <input 
                            type="email"
                            name="email"
                            id="email"
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
                            placeholder="Email"
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur}
                            value={formik.values.email}
                        />
                    </div>
                    {/* Password input */}
                    {
                        formik.touched.password && formik.errors.password ? 
                        <FormErrorMessage>{formik.errors.password}</FormErrorMessage> : 
                        null
                    }
                    <div className='my-6 bg-gray-300 flex rounded-full justify-center items-center border hover:border-primary'>
                        <Envelope size={28} color="black" weight="fill" className='mx-4'/>
                        <input 
                            type="password"
                            name="password"
                            id="password"
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
                            placeholder="Password"
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur}
                            value={formik.values.password}
                        />
                    </div>
                    {/* Confirm password input */}
                    {
                        formik.touched.cpassword && formik.errors.cpassword ? 
                        <FormErrorMessage>{formik.errors.cpassword}</FormErrorMessage> : 
                        null
                    }
                    <div className='my-6 bg-gray-300 flex rounded-full justify-center items-center border hover:border-primary'>
                        <Repeat size={28} color="black" weight="fill" className='mx-4'/>
                        <input 
                            type="password"
                            name="cpassword"
                            id="cpassword"
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
                            placeholder="Confirm your password"
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur}
                            value={formik.values.cpassword}
                        />
                    </div>
                    {/* Select input (customized) */}
                    <input type="hidden" name="usertype" id="usertype" value={formik.values.usertype}/>
                    <div className='w-80 m-auto flex justify-between items-center rounded-full bg-gray-300 py-2 px-4 mb-6 border hover:border-primary'>
                        <div>I'm looking for: {
                            formik.values.usertype == 'jobseeker' ? 
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

// Formik validation rules
const validate = values => {
    const errors = {}
    
    if (!values.username)
        errors.username = "The username field is required"

    if (!values.email)
        errors.email = "The email field is required"

    if (!values.password)
        errors.password = "The password field is required"
    else if (values.password.length < 8)
        errors.password = "The password must have at least 8 characters"

    if (!values.cpassword) 
        errors.cpassword = "You need to confirm your password"
    else if (values.cpassword != values.password)
        errors.cpassword = "The passwords doesn't match"

    return errors
}