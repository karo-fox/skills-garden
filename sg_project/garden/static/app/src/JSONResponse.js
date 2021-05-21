'use strict';

class JSONResponse extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      data: []
    }
  }

    componentDidMount() {
      fetch('fields')
        .then(res => res.json())
        .then(
          (result) => {
            this.setState({
              data: result.data
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
      const { error, data } = this.state;
      if (error) {
        return (
          <div>Error: {error.message}</div>
        );
      } else {
        return (
          <ul>
            {data.map(data => (
              <li key={data.pk}>
                {data.name} - {data.description}
              </li>
            ))}
          </ul>
        );
      }
      
    }
  }
