'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var Fields = function (_React$Component) {
  _inherits(Fields, _React$Component);

  function Fields(props) {
    _classCallCheck(this, Fields);

    return _possibleConstructorReturn(this, (Fields.__proto__ || Object.getPrototypeOf(Fields)).call(this, props));
  }

  _createClass(Fields, [{
    key: "get_topics",
    value: function get_topics(id) {
      fetch("" + id).then(function (res) {
        return res.json();
      }).then(function (result) {}, function (error) {});
    }
  }, {
    key: "render",
    value: function render() {
      var _props = this.props,
          error = _props.error,
          fields = _props.fields,
          section = _props.section;

      if (error) {
        return React.createElement(
          "div",
          null,
          "Error: ",
          error.message
        );
      } else {
        return React.createElement(
          "div",
          null,
          section === "main-content" ? React.createElement(
            "div",
            { className: "field-list-main" },
            React.createElement(
              "ul",
              null,
              fields.map(function (field) {
                return React.createElement(
                  "li",
                  { key: field.pk },
                  React.createElement(FieldMain, { data: field })
                );
              })
            )
          ) : React.createElement(
            "div",
            { className: "field-list-side" },
            React.createElement(
              "ul",
              null,
              fields.map(function (field) {
                return React.createElement(
                  "li",
                  { key: field.pk },
                  React.createElement(FieldSide, { data: field })
                );
              })
            )
          )
        );
      }
    }
  }]);

  return Fields;
}(React.Component);