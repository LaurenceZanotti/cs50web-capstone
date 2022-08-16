// Libraries
import { UserCircle, LockSimple } from 'phosphor-react'

// Icons
import GoogleIcon from "../components/login/icons/GoogleIcon";
import FacebookIcon from "../components/login/icons/FacebookIcon";
import LinkedinIcon from "../components/login/icons/LinkedinIcon";

// Components
import AuthLayout from "../components/login/AuthLayout";

export default function Login() {
  return (
    <div>
        <AuthLayout>
          <div>
              Welcome to
              <h1 className="text-primary font-logo text-xl">Job<span className="text-secondary-500">findr</span></h1>
              <p>Sign up to find the best opportunities and the best talents</p>
          </div>
          <form action="">
              <div>
                  <UserCircle size={28} color="#030303" weight="fill" />
                  <input type="text" name="username" id="username" />
              </div>
              <div>
                  <LockSimple size={28} color="#030303" weight="fill" />
                  <input type="password" name="password" id="password" />
              </div>
              <div>
                  <input type="submit" value="Log in" />
              </div>
          </form>
          <div>
              <p>Forgot my <a href="" className="text-primary font-medium">password</a></p>
              <p>Don't have an account?
                  <a href="" className='text-secondary-500 font-medium'>Create one</a>
              </p>
              <p>or</p>
              <p>Continue with a social network</p>
          </div>
          <div>
              <GoogleIcon />
              <FacebookIcon />
              <LinkedinIcon />
          </div>
        </AuthLayout>
    </div>
  )
}