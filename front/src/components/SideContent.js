import React from 'react';

import Fields from './Fields';

class SideContent extends React.Component {

  renderComponent() {
    switch(this.props.show) {
      case 'fields': return <Fields fields={this.props.fields} error={this.props.error} section="side-content" />
      default: return <p>Default</p>
    }
  }

  render() {
    return (
      <div className="panel-side">
        <div className="content-side">
          {this.renderComponent()}
        </div>
      </div>
    );
  }
}

export default SideContent;