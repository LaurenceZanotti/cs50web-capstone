import React from 'react'
import ReactDOM from 'react-dom'
import App from './App'

if (document.querySelector('#root'))
    ReactDOM.render(<App />, document.querySelector('#root'))