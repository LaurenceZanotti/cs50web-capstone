import { useState, useEffect } from 'react'
import Router from 'next/router'

const API_HOST = "localhost:5000"
const ROUTE = `${API_HOST}/api/user`


export default function Profile() {
    const [user, setUser] = useState(null)

    useEffect(() => {
        fetch(`http://${ROUTE}`)
            .then(res => res.json())
            .then(data => setUser(data))
    }, [])

    function handleClick() {
        fetch(`http://${API_HOST}/api/logout`)
            .then(res => {
                if (res.status == 200) Router.push('/')
                return res.json()
            })
    }

    return (
        <div>
            <h1>Profile</h1>
            <div>{JSON.stringify(user)}</div>
            <button onClick={handleClick}>Log out</button>
        </div>
    )
}

