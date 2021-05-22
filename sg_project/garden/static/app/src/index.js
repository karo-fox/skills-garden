'use strict';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      side: '',
      main: 'fields'
    }
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    this.setState({
      side: 'fields'
    });
  }

  render() {
    const {main, side} = this.state;
    return (
      <div id="content">
        <header>
          <MainNavbar />
          <SideNavbar handler={this.handleClick} />
        </header>
        <section className="main">
          <MainContent show={main} />
          <SideContent show={side} />
        </section>
        <Footer />
      </div>

    )
  }
}

let domContainer = document.querySelector('#root');
ReactDOM.render(<App />, domContainer);