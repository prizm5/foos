import React from 'react';
import {connect} from 'react-redux';

class Header extends React.Component{
  constructor(props){
    super(props);
  }

  render(){
    return <span>
      <div className="right shadowed">{this.props.store.getState().time}</div></span>;
  }
}

let mapStateToProps = (state) => {
  return {time: state.time};
};

let container = connect(mapStateToProps)(Header);
export default container;
