import React from 'react';

class FieldButton extends React.Component {

  setDisplay(data) {
    if(this.props.section === "main") {
      return `${data.pk} - ${data.name} - ${data.last_reviewed}`
    } else if(this.props.section === "side") {
      return `${data.pk} - ${data.name}`
    }
  }
  
  render() {
    const data = this.props.data;
    const display = this.setDisplay(data);
    return (
      <button className="field-button" onClick={this.props.handler} >{display}</button>
    );
  }   
}

export default FieldButton;