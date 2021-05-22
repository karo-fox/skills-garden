'use strict';

class Fields extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      fields: [],
      section: props.section
    }
  }

    componentDidMount() {
      fetch('fields')
        .then(res => res.json())
        .then(
          (result) => {
            this.setState({
              fields: result.fields
            });
          },
          (error) => {
            this.setState({
              error
            });
          }
        )
    }
  
    render() {
      const { error, fields, section } = this.state;
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
