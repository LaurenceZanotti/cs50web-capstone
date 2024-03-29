// Built in
import Head from 'next/head'
import Router from 'next/router'
import { useState } from 'react'

// Libraries
import { UserCircle, LockSimple } from 'phosphor-react'
import { useFormik } from 'formik'
import getCSRFToken from '../../utils/getCSRFToken';

// Icons
import GoogleIcon from "../../components/login/icons/GoogleIcon";
import FacebookIcon from "../../components/login/icons/FacebookIcon";
import LinkedinIcon from "../../components/login/icons/LinkedinIcon";

// Components
import AuthLayout from "../../components/login/AuthLayout";
import AuthHeader from "../../components/login/AuthHeader";
import InputSubmit from "../../components/login/InputSubmit";
import FormErrorMessage from "../../components/auth/FormErrorMessage";

export default function Login() {
    const disabled_animation = 'transition-opacity duration-200 ease-in opacity-75'

    // Form server response message state
    const [formMessage, setFormMessage] = useState({
        server_message: null,
        loading: false
    })

    const formik = useFormik({
        initialValues: {
            username: '',
            password: '',
        },
        onSubmit: values => {
            const options = {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCSRFToken() // CSRF token header as per docs(https://docs.djangoproject.com/en/3.2/ref/csrf/#ajax)
                },
                body: JSON.stringify({
                    username: values.username,
                    password: values.password,
                })
            }
            // Set form to loading state
            setFormMessage(prevState => {
                return {...prevState, loading: true}
            })
            // Send form
            fetch(`/api/login`, options)
                .then(res => {
                    // If login was successful, redirect
                    if (res.status == 200) return Router.push('/profile')
                    // else reset form message state
                    else setFormMessage(prevState => {
                        return {...prevState, loading: false}
                    })
                    // Get JSON message
                    return res.json()
                })
                .then(data => {
                    // Show messages for 10 seconds
                    setFormMessage(() => {
                        return {
                            server_message: data,
                            loading: false
                        }
                    })
                    setTimeout(() => {
                        return setFormMessage({
                            server_message: null,
                            loading: false
                        })
                    }, 10000)
                })
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
                    {
                        // Server error messages
                        (formik.touched.username || formik.touched.password) && formMessage.server_message ?
                        <FormErrorMessage>{formMessage.server_message.msg}</FormErrorMessage> :
                        null
                    }
                    {   
                        // Client error messages
                        formik.touched.username && formik.errors.username ? 
                        <FormErrorMessage>{formik.errors.username}</FormErrorMessage> : 
                        null
                    }
                    <div className={`my-6 bg-gray-300 flex rounded-full justify-center items-center border hover:border-primary ${formMessage.loading && disabled_animation}`}>
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
                            disabled={formMessage.loading}
                        />
                    </div>
                    {/* Password input */}
                    {
                    // Client error messages
                    formik.touched.password && formik.errors.password ? 
                    <FormErrorMessage>{formik.errors.password}</FormErrorMessage> : 
                    null
                    }
                    <div className={`my-6 bg-gray-300 flex rounded-full justify-center items-center border hover:border-primary ${formMessage.loading && disabled_animation}`}>
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
                            disabled={formMessage.loading}
                        />
                    </div>

                    {/* Log in input */}
                    <InputSubmit value="Log in" className="bg-primary" disabled={formMessage.loading}/>
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