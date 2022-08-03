import JobfindrLogo from "../components/JobFindrLogo/JobfindrLogo"
import { UserCircle } from "phosphor-react"

export default function Home({data}) {
  return (
    <>
    <nav>
      <div>
        <h1>
          <JobfindrLogo />
        </h1>
      </div>
      <div>
        <ul>
          <li>Home</li>
          <li>Search talents</li>
          <li>About</li>
        </ul>
      </div>
      <div>
        <UserCircle size={32} />
      </div>
    </nav>
    <main>
      {data.msg}
      <section>
        <h2>A <span>job</span> is looking for <span>you!</span></h2>
        <div>
          {/* Insert SVG icon and SVG background*/}
        </div>
        <form action="">
          <div>
            <p>More than <span>270,000</span> jobs are in the wait. Why not have a new opportunity?</p>
          </div>
          <div>
            <div>
              <input type="text" />
              <input type="submit" value="Send" />
            </div>
            <div>or</div>
            <div>
              <a href="">Create profile</a>
            </div>
          </div>
        </form>
      </section>
    </main>
    <footer></footer>
    </>
  )
}

export const getStaticProps = async () => {
  const res = await fetch('http://host.docker.internal:5000/api/hello')
  const data = await res.json()
  // console.log(data);

  return {
    props: {
      data
    }
  }
}