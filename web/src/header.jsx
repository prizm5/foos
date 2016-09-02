import React from 'react';

export default class Header extends React.Component{
  constructor(props){
    super(props);
  }

  render(){
    return <span>
      <div className="left shadowed">Fine, Nils!</div>
      <div className="right shadowed">5:00</div></span>;
  }
}
