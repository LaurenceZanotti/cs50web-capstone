import { useState, useEffect } from 'react'

// Built in
import Head from 'next/head'

// Components
import AuthLayout from "../../components/login/AuthLayout";
import AuthHeader from "../../components/login/AuthHeader";

export default function Congratulations() {
    const [countDown, setCountDown] = useState(7)

    return (
        <>
        <Head>
            <title>Welcome! | Jobfindr</title>
        </Head>
        <div>
            <AuthLayout>
                <AuthHeader/>
                <div className='text-center mt-0 mb-10 leading-8'>
                    <p className='text-secondary-500 font-medium'>Congratulations ✨🎉</p>
                    <p>You are ready to start! Now you can <a href="/login" className='text-primary font-medium'>sign in</a></p>
                    <p>Redirecting in {countDown} seconds...</p>
                </div>            
            </AuthLayout>
        </div>
        </>
    )
}