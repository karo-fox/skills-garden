import React from 'react';

import FieldView from './FieldView';
import Fields from './Fields';

class MainContent extends React.Component {

  renderComponent() {
    switch(this.props.show) {
      case 'fields': return <Fields fields={this.props.fields} error={this.props.error} handler={this.props.handler} section="main-content" />
      case 'topic': return <FieldView fieldName={this.props.fieldId}/>
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