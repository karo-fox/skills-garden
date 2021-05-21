'use strict';

class App extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <p>index.js start</p>
        <Navbar />
        <JSONResponse />
        <p>index.js end</p>
      </div>

    )
  }
}

let domContainer = document.querySelector('#root');
ReactDOM.render(<App />, domContainer);