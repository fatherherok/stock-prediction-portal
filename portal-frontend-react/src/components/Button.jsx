import React from 'react'

const Button = (props) => {
  return (
    // <div>Button</div>
    <>
         <a className={props.class} href=''>{props.text}</a>
    </>
  )
}

export default Button