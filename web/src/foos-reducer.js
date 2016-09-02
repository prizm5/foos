export default function(previousState, action){
  var newScore, newGame;
  switch(action.type){
    case 'score_reset':
      newScore = {team1: 0, team2: 0};
      return Object.assign({}, previousState, {score: newScore});
    case 'score_goal':
      newScore = {team1: action.payload.yellow, team2: action.payload.black};
      return Object.assign({}, previousState, {score: newScore});
    case 'set_players':
      newGame = Object.assign({}, previousState.game, {team1: action.payload.yellow, team2: action.payload.black})
      return Object.assign({}, previousState, {game: newGame});
    case 'set_game_mode':
      newGame = Object.assign({}, previousState.game, { mode: action.payload.mode})
      return Object.assign({}, previousState, {game: newGame});
    case 'time_update':
      return Object.assign({}, previousState, {time: action.payload});
    default: return previousState;
  }
}
