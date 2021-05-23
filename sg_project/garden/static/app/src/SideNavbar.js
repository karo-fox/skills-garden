'use strict';

class SideNavbar extends React.Component {
    constructor(props) {
      super(props);
    }
  
    render() {
      return (
        <div className="navbar-side">
          <div className="navbar-content">
            <button onClick={this.props.handler} className="navbar-button">Fields</button>
          </div>
        </div>
      );
    }
  }
