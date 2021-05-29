import React from 'react';

import ButtonList from './ButtonList';

class FieldView extends React.Component {
  
  constructor(props) {
    super(props);
    this.state = {
      topics: [],
      error: null
    };
  }

  componentDidMount() {
    fetch(`/garden/${this.props.parent.pk}/`)
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
    return (
      <ButtonList objectList={this.state.topics} handler={this.props.handler} redirect="home"/>
    )
  }
}

export default FieldView;