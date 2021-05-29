import React from 'react';

import ButtonList from './ButtonList';

class FieldView extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      topics: [],
      error: null
    }
  }

  componentDidMount() {
    fetch(`/garden/${this.props.fieldId}/`)
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            topics: result.topics
          });
        },
        (error) => {
          this.setState({
            error: error
          });
        }
      )
  }


  render() {
    const ButtonData = {
      ListStyle: null,
      ItemStyle: null,
      handler: null,
      text: "pk name last_reviewed",
      list: this.state.topics,
    }
    return (
      <div className="field-view">
        {this.props.fieldId}
        <ButtonList data={ButtonData} />
      </div>
    );
  }
}

export default FieldView;