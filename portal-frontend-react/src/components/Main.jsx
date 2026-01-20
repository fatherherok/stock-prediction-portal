import React from 'react'


import Button from './Button'

const Main = () => {
  return (
    // <div className='text-light'>Main</div>
    <>
      
      <div className='container'>
          <div className='p-5 text-center bg-light-dark rounded'>
              <h1 className='text-light'>Stock Prediction Portal</h1>
              <p className='text-light lead'>I love Jesus Include every Bootstrap JavaScript plugin and dependency with one of our 
                two bundles. Both bootstrap.bundle.js and bootstrap.bundle.min.js include Popper for our tooltips and popovers.
                 For more information about what’s included in Bootstrap, please see our contents section.</p>
                
                 <Button text="Login" class="btn btn-outline-info" />
          </div>
      </div>

    </>
  )
}

export default Main