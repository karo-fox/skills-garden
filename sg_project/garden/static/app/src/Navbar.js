'use strict';

class Navbar extends React.Component {
    constructor(props) {
      super(props);
    }
  
    render() {
      return (
        <nav>
            <MainNavbar />
            <SidebarNavbar />
        </nav>
      );
    }
  }
