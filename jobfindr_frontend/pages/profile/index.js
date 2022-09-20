import { useState, useEffect } from 'react'
import Router from 'next/router'
import Head from 'next/head'

export default function Profile() {
    const [user, setUser] = useState(null)

    useEffect(() => {
        fetch(`/api/user`)
            .then(res => res.json())
            .then(data => setUser(data))
    }, [])

    function handleClick() {
        fetch(`/api/logout`)
            .then(res => {
                if (res.status == 200) Router.push('/')
                return res.json()
            })
    }

    return (
        <>
        <Head>
            <title>Profile | Jobfindr</title>
        </Head>
        <div id="profile-container">
            <h1>Profile</h1>
            <div>{JSON.stringify(user)}</div>
            <button onClick={handleClick}>Log out</button>
        </div>
        </>
    )
}

