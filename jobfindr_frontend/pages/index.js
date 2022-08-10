// Globals
import JobfindrLogo from "../components/JobFindrLogo/JobfindrLogo"

// Page Icons
import ManWorking from "../components/index/ManWorking"
import WomanIcon from "../components/index/WomanIcon"
import MobileLogin from "../components/index/MobileLogin"
import SwipeProfile from "../components/index/SwipeProfile"
import JobOffers from "../components/index/JobOffers"

// Libraries
import { UserCircle, FacebookLogo, TwitterLogo, InstagramLogo } from "phosphor-react"

export default function Home(/*{data}*/) {
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
      {/* {data.msg} */}
      <header className="hero-section">
        <div>
          <h2 className="text-3xl font-bold underline">A <span>job</span> is looking for <span>you!</span></h2>
        </div>
        <div>
          <div>
            <WomanIcon />
          </div>
          <form action="">
            <div>
              <p>More than <span>270,000</span> jobs are in the wait. Why not have a new opportunity?</p>
            </div>
            <div>
              <div>
                <input type="text" placeholder="Search jobs"/>
                <input type="submit" value="Send" />
              </div>
              <div>or</div>
              <div>
                <a href="">Create profile</a>
              </div>
              <ManWorking />              
            </div>
          </form>
        </div>
      </header>
      <section>
        <h2>Getting your best <span>opportunity</span></h2>
        <div>
          <div>
            <h3>1. Sign in</h3>
            <div>
              <MobileLogin/>
            </div>
          </div>
          <div>
            <h3>2. Create a profile</h3>
            <div>
              <SwipeProfile/>
            </div>
          </div>
          <div>
            <h3>3. Subscribe to a position</h3>
            <div>
              <JobOffers/>
            </div>
          </div>
        </div>
      </section>
      <section>
        <h2>Are you a <span>talent hunter</span>? We are here to help!</h2>
      </section>
      <footer>

      </footer>
    </main>
    <footer>
      <div>
        <div>
          <JobfindrLogo />
          <div>
            <div className="social_icon"><FacebookLogo size={32} /></div>
            <div className="social_icon"><TwitterLogo size={32} /></div>
            <div className="social_icon"><InstagramLogo size={32} /></div>
          </div>
        </div>
        <div>
          <h2>Contact us</h2>
          <p>contact@jobfindr.com</p>
          <p>+1 111 111 1110</p>
          <p>352 Park Ave, Brooklyn, NY</p>
        </div>
        <div>
          <h2>Subscribe</h2>
          <form action="">
            <div>
              <p>Enter your email to get notified about our news and solutions!</p>
            </div>
            <div>
              <div>
                <input type="text" placeholder="Email"/>
                <input type="submit" value="Send" />
              </div>
            </div>
          </form>
        </div>
      </div>
      <hr /> {/* Remove this later */}
      <div>
        <p> © 2022 Jobfindr Inc. All rights reserved</p>
      </div>
    </footer>
    </>
  )
}

// export const getStaticProps = async () => {
//   const res = await fetch('http://host.docker.internal:5000/api/hello')
//   const data = await res.json()
//   // console.log(data);

//   return {
//     props: {
//       data
//     }
//   }
// }