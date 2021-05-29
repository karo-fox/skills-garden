import React from 'react';

class SideNavbar extends React.Component {
  
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

export default SideNavbar;