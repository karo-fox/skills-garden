import React from 'react';

class ButtonItem extends React.Component {
  
  render() {
    return (
      <button className={"button-item " + this.props.data.ItemStyle} onClick={() => this.props.data.handler(this.props.item.pk)}>{this.props.data.text}</button>
    );
  }
}

export default ButtonItem;