'use strict';

class FieldSide extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: props.data
    }
  }
  
  render() {
    const data = this.state.data;
    return (
      <button className="field-button side-field-button">Side Field: {data.name} - {data.pk}</button>
    );
  }   
}

