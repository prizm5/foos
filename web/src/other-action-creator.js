var moment = require('moment');
var $ = require('jquery');

function jsonp(start, end, cb) {
  $.ajax({
    url: 'http://www3.septa.org/hackathon/NextToArrive/',
    data: {
      req1: start,
      req2: end,
      req3: 1
    },
    dataType: 'jsonp',
    success: function(trips) {
      cb(trips);
    },
    error: function(error) {
      console.log('error: ', error);
    }
  });
}

function getTrainsForUsers(store) {
  let users = store.getState().game.team1.concat(store.getState().game.team2);
  return Promise.all(users.map(user => getTrains(user.station, user)));
}

function getTrains(station, user) {
  return new Promise((resolve, reject) => {
    let cb = data => {
      resolve(Object.assign(data[0], {
        user: user
      }));
    };
    jsonp('Suburban Station', station, cb)
  });
}

function runOnTimer(fn, args, interval) {
  (function runMe() {
    fn.apply(null, args);
    setTimeout(runMe, interval);
  })()
}

export default function(store) {
  runOnTimer(() => {
    store.dispatch({
      type: 'time_update',
      payload: moment().format('h:mm:ss')
    })
  }, [], 1000);

  runOnTimer(() => {
    getTrainsForUsers(store)
      .then(d => store.dispatch({
        type: 'trains_loaded',
        payload: d
      }))
  }, [], 30000);
}
