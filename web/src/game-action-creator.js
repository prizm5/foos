import Pusher from 'pusher-js';

export default function(store) {
  let pusher = new Pusher('76abfc1ad02da9810a9d', { encrypted: true });

  let channel = pusher.subscribe('foosball-out');
  channel.bind_all((name, event) => store.dispatch({ type: name, payload: event }));

  channel.bind('score_goal', g => {
    document.body.style = "background-image: url('./public/images/goal.jpg?v=" + Date.now() + ");";
  });
}
