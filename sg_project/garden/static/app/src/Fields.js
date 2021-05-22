'use strict';

class Fields extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      fields: []
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
      const { error, fields } = this.state;
      if (error) {
        return (
          <div>Error: {error.message}</div>
        );
      } else {
        return (
          <ul>
            {fields.map(field => (
              <li key={field.pk}>
                {field.name} - {field.description}
              </li>
            ))}
          </ul>
        );
      }
      
    }
  }
