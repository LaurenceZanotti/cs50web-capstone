// Globals
import JobfindrLogo from "../components/JobFindrLogo/JobfindrLogo"

// Page Icons
import ManWorking from "../components/index/ManWorking"
import WomanIcon from "../components/index/WomanIcon"
import MobileLogin from "../components/index/MobileLogin"
import SwipeProfile from "../components/index/SwipeProfile"
import JobOffers from "../components/index/JobOffers"
import SignMenu from "../components/index/SignMenu"

// Libraries
import { CheckCircle, FacebookLogo, TwitterLogo, InstagramLogo } from "phosphor-react"

export default function Home(/*{data}*/) {
  return (
    <>
    <nav className="flex justify-between items-center p-4">
      <div className="w-36">
        <h1>
          <JobfindrLogo />
        </h1>
      </div>
      <div>
        <ul className="list-none text-xl">
          <a href="#home">
            <li className="inline m-4 text-secondary-500">Home</li>
          </a>
          <a href="#hero-section">
            <li className="inline m-4 text-primary">Search talents</li>
          </a>
          <a href="#">
            <li className="inline m-4 text-primary">About</li>
          </a>
        </ul>
      </div>
      <div className="w-36 flex justify-center">
        <SignMenu/>
      </div>
    </nav>
    <main>
      {/* {data.msg} */}
      <header className="hero-section bg-hero-wave bg-no-repeat bg-bottom" id="home">
        <div className="m-auto text-center">
          <h2 className="text-4xl font-bold text-darktext">A <span className="text-primary">job</span> is waiting for <span className="text-secondary-500">you!</span></h2>
        </div>
        <div className="flex justify-center mx-96">
          <div className="m-8">
            <WomanIcon />
          </div>
          <form action="" className="m-8 w-72">
            <div className="my-4">
              <p className="text-darktext font-bold text-xl text-justify">More than <span className="text-primary">270,000</span> jobs are in the wait. Why not have a new opportunity?</p>
            </div>
            <div className="flex flex-col items-center">
              <div className="flex flex-row border border-gray-300 rounded-2xl ">
                <input type="text" placeholder="Search jobs" className="text-darktext bg-gray-50/[.75] py-2 px-4 rounded-l-2xl outline-none placeholder:text-gray-600 backdrop-blur-sm"/>
                {/* <input type="submit" value="Send" className="py-2 px-4 bg-secondary-300 rounded-r-2xl"/> */}
                <div className="p-2 bg-secondary-300 rounded-r-2xl">
                  <CheckCircle size={28} color="#3F3D56"/>
                </div>
              </div>
              <div className="text-darktext font-bold text-xl my-2">or</div>
              <a href="#">
                <div className="w-52 h-16 border border-none rounded-2xl bg-secondary-300 flex justify-center items-center">
                  <span className="text-primary font-bold text-lg">Create profile</span>
                </div>
              </a>
            </div>
            <div className="relative w-0 h-0 -z-20 bottom-44 left-14 ">
              <ManWorking />
            </div>
          </form>
        </div>
      </header>
      <section id="hero-section">
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
      <section id="">
        <h2>Are you a <span>talent hunter</span>? We are here to help!</h2>
      </section>
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