import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

export default function Home({data}) {
  return (
    <div>{data.msg}</div>
  )
}

export const getStaticProps = async () => {
  const res = await fetch('http://capstone-api-1:5000/api/hello')
  const data = await res.json()
  // console.log(data);

  return {
    props: {
      data
    }
  }
}