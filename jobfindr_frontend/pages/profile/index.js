import { useState, useEffect } from 'react'
import Router from 'next/router'
import Head from 'next/head'

export default function Profile() {
    const [message, setMessage] = useState({ msg: '...loading profile' })

    useEffect(() => {
        let res_status = null
        fetch(`/api/pros`)
            .then(res => {
                res_status = res.status
                return res.json()
            })
            .then(data => {
                if (res_status == 401) Router.push('/login')
                if (res_status == 302) Router.push(`/profile/${data.next}`)
                setMessage(data)    
            })
    }, [])

    return (
        <>
        <Head>
            <title>Profile | Jobfindr</title>
        </Head>
        <div id="profile-container">
            <h1>Profile</h1>
            <div>{message.msg}</div>
            {/* <button onClick={handleClick}>Log out</button> */}
        </div>
        </>
    )
}

