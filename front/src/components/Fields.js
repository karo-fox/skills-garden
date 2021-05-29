import React from 'react';

import FieldButton from './FieldButton';

class Fields extends React.Component {
  
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
                    <FieldButton data={field} section="main" />
                  </li>
                ))}
              </ul>
            </div>
          : <div className="field-list-side">
              <ul>
                {fields.map(field => (
                  <li key={field.pk}>
                    <FieldButton data={field} section="side" />
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