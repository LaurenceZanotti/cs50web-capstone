import { useState, useEffect } from 'react'

const API_HOST = "localhost:5000"
const ROUTE = `${API_HOST}/api/user`


export default function Profile() {
    const [user, setUser] = useState(null)

    useEffect(() => {
        fetch(`http://${ROUTE}`)
            .then(res => res.json())
            .then(data => setUser(data))
    }, [])

    return (
        <div>
            <h1>Profile</h1>
            <div>{JSON.stringify(user)}</div>
        </div>
    )
}

