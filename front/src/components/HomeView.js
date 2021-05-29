import React from 'react';

import ButtonList from './ButtonList';

class HomeView extends React.Component {
  
  constructor(props) {
    super(props);
    this.state = {
      fields: [],
      error: null
    };
  }

  componentDidMount() {
    fetch('/garden/fields/')
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            fields: result.fields
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
      <ButtonList objectList={this.state.fields} handler={this.props.handler} redirect="field"/>
    )
  }
}

export default HomeView;