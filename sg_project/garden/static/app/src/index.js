'use strict';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      side: '',
      main: 'fields',
      fields: [],
      error: null
    }
    this.handleClick = this.handleClick.bind(this);
  }

  componentDidMount() {
    fetch('fields')
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            fields: result.fields
          });
        },
        (error) => {
          this.setState({
            error
          });
        }
      )
  }

  handleClick() {
    this.setState({
      side: 'fields'
    });
  }

  render() {
    const {main, side, fields, error} = this.state;
    return (
      <div id="content">
        <header>
          <MainNavbar />
          <SideNavbar handler={this.handleClick} />
        </header>
        <section className="main">
          <MainContent fields={fields} error={error} show={main} />
          <SideContent fields={fields} error={error} show={side} />
        </section>
        <Footer />
      </div>

    )
  }
}

let domContainer = document.querySelector('#root');
ReactDOM.render(<App />, domContainer);