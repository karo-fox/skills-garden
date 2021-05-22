'use strict';

class App extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div id="content">
        <header>
          <MainNavbar />
          <SideNavbar />
        </header>
        <section className="main">
          <MainContent />
          <SideContent />
        </section>
        <Footer />
      </div>

    )
  }
}

let domContainer = document.querySelector('#root');
ReactDOM.render(<App />, domContainer);