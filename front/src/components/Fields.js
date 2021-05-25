import React from 'react';

import FieldMain from './FieldMain';
import FieldSide from './FieldSide';

class Fields extends React.Component {
  constructor(props) {
    super(props);
  }

  get_topics(id) {
    fetch(`${id}`)
      .then(res => res.json())
      .then(
        (result) => {

        },
        (error) => {

        }
      )
  }
  
  render() {
    const { error, fields, section } = this.props;
    if (error) {
      return (
        <div>Error: {error.message}</div>
      );
    } else {
      return (
        <div>
          {section === "main-content"
          ? <div className="field-list-main">
              <ul>
                {fields.map(field => (
                  <li key={field.pk}>
                    <FieldMain data={field} />
                  </li>
                ))}
              </ul>
            </div>
          : <div className="field-list-side">
              <ul>
                {fields.map(field => (
                  <li key={field.pk}>
                    <FieldSide data={field}/>
                  </li>
                ))}
              </ul>
            </div>
            }
        </div>
      );
    } 
  }
}

export default Fields;