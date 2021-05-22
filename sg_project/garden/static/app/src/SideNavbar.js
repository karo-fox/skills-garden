'use strict';

class SideNavbar extends React.Component {
    constructor(props) {
      super(props);
    }
  
    render() {
      return (
        <div className="navbar-side">
          Side Navbar here
          <button onClick={this.props.handler} className="navbar-button">Fields</button>
        </div>
      );
    }
  }
