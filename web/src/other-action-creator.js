var moment = require('moment');

export default function(store){
  setInterval(()=> {
    store.dispatch({type: 'time_update', payload: moment().format('h:mm:ss')});
  }, 1000)
}