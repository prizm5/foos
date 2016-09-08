import ReactDOM from 'react-dom';
import React from 'react';
import ScoreContainer from './score.jsx';
import Header from './header.jsx';
import {createStore} from 'redux';
import reducer from './foos-reducer';
import init from './game-action-creator';
import hac from './other-action-creator';
import Trains from './trains.jsx';

let store = createStore(reducer, {
  game: {
    team1: [
      {
        name: ''
      }
    ],
    team2: [
      {
        name: ''
      }
    ]
  },
  score: {
    team1: null,
    team2: null
  },
  time: 'now'
}, window.devToolsExtension && window.devToolsExtension());
init(store);
hac(store);

ReactDOM.render(
  <Header store={store}/>, document.getElementById('header'))
ReactDOM.render(
  <ScoreContainer store={store}/>, document.getElementById('score'))
ReactDOM.render(
  <Trains store={store}/>, document.getElementById('trains-container'))
