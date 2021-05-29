import React from 'react';

class ButtonList extends React.Component {

  render() {
    return (
      <ul className="object-list">
        {this.props.objectList.map(item => (
          <li key={item.pk}>
            <button className='button-item' onClick={() => this.props.handler(item, this.props.redirect)}>{item.name}</button>
          </li>
        ))}
      </ul>
    );
  }
}

export default ButtonList;