import React from 'react';

class connection extends React.Component {
		didMount() {
		const apiUrl = 'http://127.0.0.1:8000/sensor/';
		fetch(apiUrl).then((rsponse) => rsponse.json()).then((data) => (console.log(data)));
	}
  render(){
    return <div> Example </div>
  }
}
export default connection;