'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var JSONResponse = function (_React$Component) {
  _inherits(JSONResponse, _React$Component);

  function JSONResponse(props) {
    _classCallCheck(this, JSONResponse);

    var _this = _possibleConstructorReturn(this, (JSONResponse.__proto__ || Object.getPrototypeOf(JSONResponse)).call(this, props));

    _this.state = {
      error: null,
      data: []
    };
    return _this;
  }

  _createClass(JSONResponse, [{
    key: 'componentDidMount',
    value: function componentDidMount() {
      var _this2 = this;

      fetch('fields').then(function (res) {
        return res.json();
      }).then(function (result) {
        _this2.setState({
          data: result.data
        });
      }, function (error) {
        _this2.setState({
          error: error
        });
      });
    }
  }, {
    key: 'render',
    value: function render() {
      var _state = this.state,
          error = _state.error,
          data = _state.data;

      if (error) {
        return React.createElement(
          'div',
          null,
          'Error: ',
          error.message
        );
      } else {
        return React.createElement(
          'ul',
          null,
          data.map(function (data) {
            return React.createElement(
              'li',
              { key: data.pk },
              data.name,
              ' - ',
              data.description
            );
          })
        );
      }
    }
  }]);

  return JSONResponse;
}(React.Component);