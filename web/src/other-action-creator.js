var moment = require('moment');
var request = require('superagent');

function getTrainsForUsers(store) {
    let users = store.getState().game.team1.concat(store.getState().game.team2);
    return Promise.all(users.map(user => getTrains(user.station, user)));
}

function getTrains(station, user) {
    return new Promise((resolve, reject) => {
        request.get('http://www3.septa.org/hackathon/NextToArrive/Suburban%20Station/' + encodeURI(station) + '/1')
            .set('Accept', 'application/json')
            .end((err, succ) => {
                resolve(Object.assign(succ.body[0], {
                    user: user
                }));
            });
    });
}

function runOnTimer(fn, args, interval) {
    (function runMe() {
        fn.apply(null, args);
        setTimeout(runMe, interval);
    })()
}

export default function(store) {
    // runOnTimer(() => {
    //     store.dispatch({
    //         type: 'time_update',
    //         payload: moment().format('h:mm:ss')
    //     })
    // }, [], 1000);

    runOnTimer(() => {
        getTrainsForUsers(store)
            .then(d => store.dispatch({
                type: 'trains_loaded',
                payload: d
            }))
    }, [], 30000);
}
