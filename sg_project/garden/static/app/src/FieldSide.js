'use strict';

class FieldSide extends React.Component {
  constructor(props) {
    super(props);
  }
  
  render() {
    const data = this.props.data;
    return (
      <button className="field-button side-field-button">Side Field: {data.name} - {data.pk}</button>
    );
  }   
}

