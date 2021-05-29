import React from 'react';

import ButtonItem from './ButtonItem';

class ButtonList extends React.Component {

  render() {
    return (
      <ul className={"object-list " + this.props.data.ListStyle}>
        {this.props.data.list.map(item => (
          <li key={item.pk}>
            <ButtonItem data={this.props.data} item={item}/>
          </li>
        ))}
      </ul>
    );
  }
}

export default ButtonList;