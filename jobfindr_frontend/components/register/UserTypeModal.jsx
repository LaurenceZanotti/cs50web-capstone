/* This example requires Tailwind CSS v2.0+ */
import { Fragment, useRef, useState } from 'react'
import { Dialog, Transition } from '@headlessui/react'
import { Confetti } from 'phosphor-react'

export default function UserTypeModal(props) {
  const [open, setOpen] = useState(true)

  const cancelButtonRef = useRef(null)

  return (
    <Transition.Root show={open} as={Fragment}>
      <Dialog
        as="div"
        className="relative z-10"
        initialFocus={cancelButtonRef}
        open={open}
        static
        onClose={() => null}
      >
        {/* 
        /* Inserting static prop and a null anonymous function above avoids the
        /* user from skipping the modal step by clicking outside the modal
        /* or by pressing Esc. The solution was given by GitHub user wengtytt
        /* here: https://github.com/tailwindlabs/headlessui/issues/621
        */}
        <Transition.Child
          as={Fragment}
          enter="ease-out duration-300"
          enterFrom="opacity-0"
          enterTo="opacity-100"
          leave="ease-in duration-200"
          leaveFrom="opacity-100"
          leaveTo="opacity-0"
        >
          <div className="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
        </Transition.Child>

        <div className="fixed inset-0 z-10 overflow-y-auto">
          <div className="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
            <Transition.Child
              as={Fragment}
              enter="ease-out duration-300"
              enterFrom="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
              enterTo="opacity-100 translate-y-0 sm:scale-100"
              leave="ease-in duration-200"
              leaveFrom="opacity-100 translate-y-0 sm:scale-100"
              leaveTo="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
            >
              <Dialog.Panel className="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg">
                <div className="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                  <div className="sm:flex sm:flex-col sm:items-center">
                    <div className="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-secondary-100 sm:mx-0 sm:h-10 sm:w-10 mb-4">
                      <Confetti size={64} color="#4D6CFF" weight="duotone" />
                    </div>
                    <div className="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                      <Dialog.Title as="h3" className="text-center text-lg font-medium leading-6 text-gray-900">
                        I'm looking for...
                      </Dialog.Title>
                    </div>
                  </div>
                </div>
                <div className="bg-gray-50 px-4 py-3 mb-4 sm:flex sm:px-6">
                  <button
                    type="button"
                    className="inline-flex sm:flex-1 w-full justify-center rounded-md border border-transparent bg-primary px-4 py-2 text-base font-medium text-white shadow-sm hover:bg-primary focus:outline-none focus:ring-2 focus:ring-primary focus:ring-offset-2 sm:ml-3 sm:w-auto sm:text-sm"
                    onClick={() => {
                      props.handleUserType("jobseeker")
                      setOpen(false)
                    }}
                    ref={cancelButtonRef}
                  >
                    Job opportunities
                  </button>
                  <span className='font-medium ml-3 inline-flex items-center'>or</span>
                  <button
                    type="button"
                    className="mt-3 inline-flex sm:flex-1 w-full justify-center rounded-md border border-transparent bg-secondary-500 px-4 py-2 text-base font-medium text-white shadow-sm hover:bg-priamry focus:outline-none focus:ring-2 focus:ring-secondary-500 focus:ring-offset-2 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm"
                    onClick={() => {
                      props.handleUserType("talenthunter")
                      setOpen(false)
                    }}
                  >
                    New talents
                  </button>
                </div>
              </Dialog.Panel>
            </Transition.Child>
          </div>
        </div>
      </Dialog>
    </Transition.Root>
  )
}
