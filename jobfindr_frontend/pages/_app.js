import Head from 'next/head'

import '../styles/globals.css'

function MyApp({ Component, pageProps }) {
  return (
    <>
      <Head>
        <title>Jobfindr</title>
        <meta property="og:title" content="Jobfindr" key="title" />
        <meta httpEquiv="X-UA-Compatible" content="ie=edge" />
        <meta httpEquiv="Content-Type" content="text/html;charset=UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta name="description" content="Find jobs and talents, or both. You choose." />
        <meta name="keywords" content="job, jobs, find, find jobs, search jobs, talents, talent, recruiting, opportunities" />
      </Head>
      <Component {...pageProps} />
    </>
  )
}



export default MyApp
