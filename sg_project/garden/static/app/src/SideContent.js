'use strict';

class SideContent extends React.Component {
  constructor(props) {
    super(props);
  }

  renderComponent() {
    switch(this.props.show) {
      case 'fields': return <Fields section="main-content" />
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
