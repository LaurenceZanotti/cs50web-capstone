// Libraries
import { useState, useEffect } from 'react'
import { useRouter } from 'next/router'
import Head from 'next/head'

// Components
import Header from '../../../components/protected/Header'
import Footer from '../../../components/protected/Footer'

// Libraries
import { Briefcase } from "phosphor-react"

export default function ProfileUsername() {
    // https://nextjs.org/docs/routing/dynamic-routes
    const router = useRouter()
    const {username} = router.query
    const [profile, setProfile] = useState({
        profile: null,
        is_loading: true
    })
    // TODO: Probably change this to SSG instead of CSR 
    // (else whats the point of next)
    useEffect(() => {
        if (username == undefined) return
        
        // On page load fetches profile
        fetch(`/api/pros/${username}`)
            .then(res => res.json())
            .then(data => setProfile({profile: data, is_loading: false}))
    }, [username])
    
    function handleLogout() {
        fetch(`/api/logout`)
            .then(res => {
                if (res.status == 200) router.push('/login')
            })
    }

    return (
        <>
        <Head>
            <title>{username} | Jobfindr</title>
        </Head>
        <Header>
            {/* Desktop menu options */}
            <button className='text-white flex gap-2'><Briefcase size={24} color="#f2eded" weight="fill" />Job feed</button>
        </Header>
        <div id="profile-container">
            <h1>{username}</h1>
        {
            // Profile is loading
            profile.profile == null && 
            profile.is_loading &&
            <>
            <div>...loading profile</div>
            </>
        }
        {
            // Profile is available
            profile.profile && !profile.is_loading &&
            <>
            <div>
                {JSON.stringify(profile.profile)}
            </div>
            </>
        }
            <button onClick={handleLogout}>Log out</button>
        </div>
        <Footer/>
        </>
    )
}

