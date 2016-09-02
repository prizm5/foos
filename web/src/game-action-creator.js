import Pusher from 'pusher-js';

export default function(store){
  let pusher = new Pusher('76abfc1ad02da9810a9d', {encrypted: true});

  pusher.subscribe('foosball-out')
        .bind_all((name, event)=> store.dispatch({type: name, payload: event}));
}
