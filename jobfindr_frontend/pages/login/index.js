// Built in
import Head from 'next/head'

// Libraries
import { UserCircle, LockSimple } from 'phosphor-react'
import { useFormik } from 'formik'

// Icons
import GoogleIcon from "../../components/login/icons/GoogleIcon";
import FacebookIcon from "../../components/login/icons/FacebookIcon";
import LinkedinIcon from "../../components/login/icons/LinkedinIcon";

// Components
import AuthLayout from "../../components/login/AuthLayout";
import AuthHeader from "../../components/login/AuthHeader";
import InputSubmit from "../../components/login/InputSubmit";

export default function Login() {

    const formik = useFormik({
        initialValues: {
            username: '',
            password: '',
        },
        onSubmit: values => {
            console.log(values)
        },
        validate
    })

    return (
        <>
        <Head>
            <title>Log in | Jobfindr</title>
        </Head>
        <div>
            <AuthLayout>
                <AuthHeader/>            
                <form onSubmit={formik.handleSubmit} action="" method="post" className="w-80 m-auto">
                    {/* Username input */}
                    <div className='my-6 bg-gray-300 flex rounded-full justify-center items-center border hover:border-primary'>
                        <UserCircle size={28} color="black" weight="fill" className='mx-4'/>
                        <input 
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
                    {
                        formik.touched.username && formik.errors.username ? 
                        <div>{formik.errors.username}</div> : 
                        null
                    }
                    {/* Password input */}
                    <div className='my-6 bg-gray-300 flex rounded-full justify-center items-center border hover:border-primary'>
                        <LockSimple size={28} color="black" weight="fill" className='mx-4'/>
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
                    {
                    formik.touched.password && formik.errors.password ? 
                    <div>{formik.errors.password}</div> : 
                    null
                    }

                    {/* Log in input */}
                    <InputSubmit value="Log in" className="bg-primary"/>
                </form>
                <div className='text-center mt-0 mb-10 leading-8'>
                    <p>I forgot my <a href="" className="text-primary font-medium">password</a></p>
                    <p>Don't have an account?
                        <a href="/register" className='text-secondary-500 font-medium ml-1'>Create one</a>
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
        </>
    )
}

// Login form validation
const validate = values => {
    const errors = {}

    if (!values.username) {
        errors.username = "Please provide your username"
    }

    if (!values.password) {
        errors.password = "Please provide your password"
    }

    return errors
}