import React from 'react';
import logo from './logo.svg';
import './style.css';
import MainNavbar from './components/MainNavbar';
import SideNavbar from './components/SideNavbar';
import MainContent from './components/MainContent';
import SideContent from './components/SideContent';
import Footer from './components/Footer';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      side: '',
      main: 'fields',
      fields: [],
      errors: []
    }
    this.handleClick = this.handleClick.bind(this);
  }

  componentDidMount() {
    fetch('http://127.0.0.1:8000/fields')
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            fields: result.fields
          });
        },
        (error) => {
          this.setState({
            errors: error
          });
        }
      )
  }

  handleClick () {
    this.setState({
      side: 'fields'
    });
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <MainNavbar />
          <SideNavbar handler={this.handleClick} />
        </header>
        <section className="main">
          <MainContent fields={null} error={null} show={null} />
          <SideContent fields={null} error={null} show={null} />
        </section>
        <Footer />
      </div>
    );
  }
  
}

export default App;
