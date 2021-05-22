'use strict';

class FieldMain extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      data: props.data
    }
  }
  
  render() {
    const data = this.state.data;
    return (
      <button className="field-button main-field-button">{data.name} - {data.pk}</button>
    );
  }   
}
