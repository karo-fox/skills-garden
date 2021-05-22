'use strict';

class MainContent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      show: props.show
    }
  }

  renderComponent() {
    switch(this.state.show) {
      case 'fields': return <Fields section="main-content" />
      default: return <p>Default</p>
    }
  }

  render() {
    return (
      <div className="panel-main">
        <div className="content-main">
          {this.renderComponent()}
        </div>
      </div>
    );
  }
}
