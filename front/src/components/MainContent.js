import React from 'react';

import Fields from './Fields';

class MainContent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      show: props.show
    }
  }

  renderComponent() {
    switch(this.state.show) {
      case 'fields': return <Fields fields={this.props.fields} error={this.props.error} section="main-content" />
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

export default MainContent;