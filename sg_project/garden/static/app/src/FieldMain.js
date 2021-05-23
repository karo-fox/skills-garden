'use strict';

class FieldMain extends React.Component {
  constructor(props) {
    super(props);
  }
  
  render() {
    const data = this.props.data;
    return (
      <button className="field-button main-field-button">{data.name} - {data.pk}</button>
    );
  }   
}
