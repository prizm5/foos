import ReactDOM from 'react-dom';
import React from 'react';
import ScoreContainer from './score.jsx';
import Header from './header.jsx';
import {createStore} from 'redux';
import reducer from './game-reducer';
import init from './game-action-creator';

let store = createStore(reducer, {
   game: { team1: [], team2:[]},
   score: {team1: null, team2: null}},
   window.devToolsExtension && window.devToolsExtension());
init(store);

ReactDOM.render(<Header />, document.getElementById('header'))
ReactDOM.render(<ScoreContainer store={store} />, document.getElementById('score'))
