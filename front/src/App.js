import React from 'react';
// import logo from './logo.svg';
import './style.css';
import MainNavbar from './components/MainNavbar';
import SideNavbar from './components/SideNavbar';
import HomeView from './components/HomeView';
import FieldView from './components/FieldView';
import SideContent from './components/SideContent';
import Footer from './components/Footer';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      side: '',
      main: 'home',
      // objectList: [],
      // error: null
      item: null
    }
    this.handleSideNavFieldClick = this.handleSideNavFieldClick.bind(this);
    this.renderView = this.renderView.bind(this);
    // this.handleFieldClick = this.handleFieldClick.bind(this);
  }

  // componentDidMount() {
  //   fetch('/garden/fields')
  //     .then(res => res.json())
  //     .then(
  //       (result) => {
  //         this.setState({
  //           objectList: result.fields
  //         });
  //       },
  //       (error) => {
  //         this.setState({
  //           error: error
  //         });
  //       }
  //     )
  // }

  handleSideNavFieldClick () {
    this.setState({
      side: 'fields'
    });
  }

  // handleFieldClick(pk) {
  //   this.setState({
  //     main: 'topic',
  //   })
  // }

  renderView(parent, redirect) {
    switch(redirect) {
      case 'home': 
        console.log('render view with home was called');
        this.state = {
          main: 'home'
        }
        return <HomeView parent={null} handler={this.renderView} />
      case 'field':
        console.log('render view with field was called');
        this.state = {
          main: 'field'
        }
        return <FieldView parent={parent} handler={this.renderView} />
      // case 'topic': return <Topicview parent={parent} viewName='topic' handler={this.renderView} />
      default:
        console.log('render view with default was called');
        this.setState = ({
          main: 'home'
        });
        return <HomeView parent={null} handler={this.renderView} />
    }
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <MainNavbar />
          <SideNavbar handler={this.handleSideNavFieldClick} />
        </header>
        <section className="main">
          <div className="panel-main">
            <div className="content-main">
              {this.renderView(this.state.parent, this.state.main)}
            </div>
          </div>
          {/* <SideContent handler={this.handleFieldClick} fields={fields} error={error} show={side} fieldId={fieldId} /> */}
        </section>
        <Footer />
      </div>
    );
  }
  
}

export default App;
