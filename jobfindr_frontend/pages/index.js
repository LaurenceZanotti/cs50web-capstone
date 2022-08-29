// Built in
import Head from 'next/head'

// Globals
import JobfindrLogo from "../components/JobFindrLogo/JobfindrLogo"

// Page Icons
import WomanIcon from "../components/index/WomanIcon"
import MobileLogin from "../components/index/MobileLogin"
import SwipeProfile from "../components/index/SwipeProfile"
import JobOffers from "../components/index/JobOffers"
import DropdownMenu from "../components/index/DropdownMenu"
import Testimonial from "../components/index/Testimonial"

// Libraries
import { UserCircle, List, CheckCircle, FacebookLogo, TwitterLogo, InstagramLogo } from "phosphor-react"

export default function Home(/*{data}*/) {
  return (
    <>
      <Head>
        <title>Jobfindr - Your future happens now</title>
        <meta property="og:title" content="Jobfindr - Your future happens now" key="title" />
      </Head>
      <div className="bg-gradient-to-b from-primary/[.6] to-white" id="main">
      <nav className="flex justify-between items-center p-4 w-screen sm:w-[60em] m-auto bg-white">
        <div className="w-24 md:w-36">
          <h1 className='font-logo text-primary text-4xl'>
            Job
            <span className='text-secondary-500'>findr</span>
          </h1>
        </div>
        <div className='hidden sm:block'>
          <ul className="list-none text-xl">
            <a href="#home">
              <li className="inline m-4 text-secondary-500">Home</li>
            </a>
            <a href="#hero-section">
              <li className="inline m-4 text-primary">Search jobs</li>
            </a>
            <a href="#talent-hunter">
              <li className="inline m-4 text-primary">Looking for talents</li>
            </a>
            <a href="#contact">
              <li className="inline m-4 text-primary">Contact us</li>
            </a>
          </ul>
        </div>
        <div className="hidden sm:flex w-auto sm:w-36 justify-center">
          <DropdownMenu 
            icon={<UserCircle size={36} />}
            list_options={["Log in", "Sign up"]}
            list_hrefs={["login", "register"]}
          />
        </div>
        <div className="sm:hidden w-auto sm:w-36 flex justify-center">
          <DropdownMenu 
            icon={<List size={36} />}
            list_options={["Home", "I'm looking for a job", "I'm hunting talents", "Contact us", "Log in", "Sign up"]}
            list_hrefs={["#home", "#hero-section", "#talent-hunter", "#contact", "login", "register"]}
          />
        </div>
      </nav>
      <main className="bg-white w-screen sm:w-[60em] m-auto">
        {/* {data.msg} */}
        <header className="hero-section bg-hero-wave bg-no-repeat bg-bottom" id="home">
          <div className="m-auto text-center">
            <h2 className="section-title text-2xl sm:text-4xl font-bold text-darktext">A <span className="text-primary">job</span> is waiting for <span className="text-secondary-500">you!</span></h2>
          </div>
          <div className="flex flex-col-reverse sm:flex-row justify-center">
            <div className="overflow-hidden sm:overflow-visible sm:w-auto sm:m-8">
              <WomanIcon />
            </div>
            <form action="" className="m-8 bg-man-working bg-no-repeat bg-bottom">
              <div className="mt-0 mb-4">
                <p className="text-darktext font-medium text-xl text-justify">More than <span className="text-primary">270,000</span> jobs are in the wait. Why not have a new opportunity?</p>
              </div>
              <div className="flex flex-col items-center">
                <div className="flex flex-row border border-gray-300 rounded-2xl my-2">
                  <input type="text" placeholder="Search jobs" className="text-darktext bg-gray-50/[.75] py-2 px-4 rounded-l-2xl outline-none placeholder:text-gray-600 backdrop-blur-sm"/>
                  {/* <input type="submit" value="Send" className="py-2 px-4 bg-secondary-300 rounded-r-2xl"/> */}
                  <div className="p-2 bg-secondary-300 rounded-r-2xl">
                    <CheckCircle size={28} color="#3F3D56"/>
                  </div>
                </div>
                <div className="text-darktext font-medium text-xl my-2">or</div>
                <a href="register" id="hero-section-cta-button">
                  <div className="w-52 h-16 border border-none rounded-2xl bg-secondary-300 flex justify-center items-center">
                    <span className="text-primary font-bold text-lg">Create a profile</span>
                  </div>
                </a>
              </div>              
            </form>
          </div>
        </header>
        <section className="flex flex-col items-center" id="hero-section">
          <h2 className="section-title text-center text-2xl sm:text-4xl font-bold text-darktext m-8">Getting your best <span className="text-primary">opportunity</span></h2>
          <div className="flex flex-col sm:flex-row mb-8">
            <div className="border border-gray-400 rounded-2xl m-4 px-4 py-0">
              <h3 className="text-primary text-2xl text-center font-medium font-logo my-4"><span className="text-secondary-300 text-3xl inline-block relative left-0">1.</span> Sign in</h3>
              <div>
                <MobileLogin/>
              </div>
            </div>
            <div className="border border-gray-400 rounded-2xl m-4 px-4 py-0">
              <h3 className="text-primary text-2xl text-center font-medium font-logo my-4"><span className="text-secondary-300 text-3xl">2.</span> Create a profile</h3>
              <div>
                <SwipeProfile/>
              </div>
            </div>
            <div className="border border-gray-400 rounded-2xl m-4 px-4 py-0">
              <h3 className="text-primary text-2xl text-center font-medium font-logo my-4"><span className="text-secondary-300 text-3xl">3.</span> Subscribe to a position</h3>
              <div>
                <JobOffers/>
              </div>
            </div>
          </div>
        </section>
        <section className="flex flex-col items-center bg-talent-wave bg-no-repeat bg-top min-h-[25em]" id="talent-hunter">
          <h2 className="section-title text-center w-[16em] text-2xl sm:text-4xl font-bold text-darktext m-8">
            <div>Are you a <span className="text-primary">talent hunter</span>?</div>
            <div>All you need is here!</div>
          </h2>
          <div className='flex flex-col sm:flex-row'>
            <Testimonial 
              img_src={"index/testmon1.jpg"} 
              name="Isabella Brite"
              role="Copny P&C Manager"
            >
              Lorem, ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis ducimus a, officia quidem vero id excepturi recusandae neque soluta, necessitatibus est. Veritatis velit facere perferendis deleniti laudantium aut repellat nihil?
            </Testimonial>
            <Testimonial 
              img_src={"index/testmon2.jpg"} 
              name="Jose Gonzalez"
              role="Talent Hunter at Inc LTD"
            >
              Lorem, ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis ducimus a, officia quidem vero id excepturi recusandae neque soluta, necessitatibus est. Veritatis velit facere perferendis deleniti laudantium aut repellat nihil?
            </Testimonial>
            <Testimonial 
              img_src={"index/testmon3.jpg"} 
              name="Allie Mont"
              role="People & Culture Coordinator"
            >
              Lorem, ipsum dolor sit amet consectetur adipisicing elit. Perspiciatis ducimus a, officia quidem vero id excepturi recusandae neque soluta, necessitatibus est. Veritatis velit facere perferendis deleniti laudantium aut repellat nihil?
            </Testimonial>
          </div>
        </section>
      </main>
      <footer className="bg-white w-full sm:w-[60em] m-auto">
        <div className="flex flex-col sm:flex-row justify-around m-4 sm:m-auto">
          <div>
            {/* <JobfindrLogo width="139.5" height="29.25"/> */}
            <div className="w-[8rem] m-auto">
              <h1 className='font-logo text-primary text-4xl mt-4'>
                Job
                <span className='text-secondary-500'>findr</span>
              </h1>
            </div>
            <div className="flex justify-center gap-4 sm:justify-evenly mt-4">
              <div className="social_icon rounded-full bg-gradient-to-t from-secondary-300 to-secondary-100 sm:p-1"><FacebookLogo size={32} /></div>
              <div className="social_icon rounded-full bg-gradient-to-t from-secondary-300 to-secondary-100 sm:p-1"><TwitterLogo size={32} /></div>
              <div className="social_icon rounded-full bg-gradient-to-t from-secondary-300 to-secondary-100 sm:p-1"><InstagramLogo size={32} /></div>
            </div>
          </div>
          <div className="" id="contact">
            <h2 className="text-primary text-lg font-medium mt-4">Contact us</h2>
            <div className="text-xs">
              <p>contact@jobfindr.com</p>
              <p>+1 111 111 1110</p>
              <p>352 Park Ave, Brooklyn, NY</p>
            </div>
          </div>
          <div>
            <h2 className="text-primary text-lg font-medium mt-4">Subscribe</h2>
            <form action="">
              <div className="text-xs w-full sm:w-64">
                <p>Enter your email to get notified about our news and solutions!</p>
              </div>
              <div className="flex max-w-xs border border-gray-300 rounded-2xl my-2 justify-between h-10">
                <input type="text" placeholder="Email" className="text-darktext text-xs bg-gray-50/[.75] py-2 px-4 rounded-l-2xl outline-none placeholder:text-gray-600 placeholder:text-xs backdrop-blur-sm"/>
                {/* <input type="submit" value="Send" className="py-2 px-4 bg-secondary-300 rounded-r-2xl"/> */}
                <div className="p-2 bg-secondary-300 rounded-r-2xl flex justify-center items-center">
                  <CheckCircle size={20} color="#3F3D56"/>
                </div>
              </div>
            </form>
          </div>
        </div>
        <div className="w-full h-0 border border-b-secondary-500 mt-4" id="hr"/>
        <div className="text-primary text-center font-normal my-4">
          <p>© 2022 Jobfindr Inc. All rights reserved</p>
        </div>
      </footer>
      </div>
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