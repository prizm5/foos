import React from 'react';
import {connect} from 'react-redux';

class Header extends React.Component{
  constructor(props){
    super(props);
  }

  render(){
    console.log(this.props);
    return <span>
      <div className="left shadowed">Fine, Nils!</div>
      <div className="right shadowed">{this.props.store.getState().time}</div></span>;
  }
}

let mapStateToProps = (state) => {
  return {time: state.time};
};

let container = connect(mapStateToProps)(Header);
export default container;
