import React from 'react';
import {connect} from 'react-redux';

class Trains extends React.Component {
  constructor(props) {
    super(props);
  }

  getDelayClass(delay) {
    if (parseInt(delay) > 0)
      return 'late';
    else
      return 'on-time';
    }
  getTrainViews(trains) {
    if (trains && trains.length > 0) {
      return trains.map(t => <div key={t.user.name} className="train">
        <h3 className="rider">{t.user.name}</h3>
        <span className="station">{t.orig_line}</span>
        <span className="time">{t.orig_departure_time}</span>
        <span className={"delay " + this.getDelayClass(t.orig_delay)}>{t.orig_delay}</span>
      </div>);
    }
    return '';
  }

  render() {
    return <div id="trains">
      {this.getTrainViews(this.props.trains)}
    </div>
  }
}

let mapStateToProps = (state) => {
  return {trains: state.trains};
};

let container = connect(mapStateToProps)(Trains);
export default container;
