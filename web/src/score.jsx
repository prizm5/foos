import React from 'react';
import {connect} from 'react-redux';

class Score extends React.Component{
  constructor(props){
    super(props);
  }

  statusClass(team){
    let winningScore = this.props.game.mode;
    if(this.props.score[team] === winningScore){
      return 'winner';
    }
    else if(team === 'team1' && this.props.score['team2'] === winningScore){
      return 'loser';
    }else if(team === 'team2' && this.props.score['team1'] === winningScore){
      return 'loser';
    }else{
      return 'in-progress';
    }
  }

  getPlayerName(field){
    return !field ? '' : field.name;
  }

  render(){
    return (
  <div className="score-row">
    <div className={"left left-score " + (this.statusClass('team1'))}>
      <div className="black number-container">
        {this.props.score.team1}
      </div>
      <div className="names shadowed">
        <p>{this.props.game.team1[0].name}</p>
        <p>{this.getPlayerName(this.props.game.team1[1])}</p>
      </div>
    </div>
    <div className={this.statusClass('team2')}>
      <div className="number-container">
        {this.props.score.team2}
      </div>
      <div className="names shadowed">
        <p>{this.props.game.team2[0].name}</p>
        <p>{this.getPlayerName(this.props.game.team2[1])}</p>
      </div>
    </div>
  </div>
    )
  }
}

let mapStateToProps = (state) => {
    return state;
};

let scoreContainer = connect(mapStateToProps)(Score);
export default scoreContainer;
