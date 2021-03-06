import json
from decimal import Decimal, Context

from flask import Flask, jsonify, Response
from flask_request_validator.exceptions import InvalidRequest
from flask_request_validator import (
    JSON,
    Param,
    Pattern,
    validate_params
)

ctx = Context(20, Emin=-999999999999999, Emax=999999999999999)


def prepare_response(data):
    return jsonify({'result': data.normalize().to_eng_string(ctx)})


def run_app():
    app = Flask(__name__)
    default_request_validator = validate_params(
        Param('arg1', JSON, str, rules=[Pattern(r'^\-?\d{1,}(\.?\d{1,6}$)?$')]),
        Param('arg2', JSON, str, rules=[Pattern(r'^\-?\d{1,}(\.?\d{1,6}$)?$')])
    )

    @app.errorhandler(InvalidRequest)
    def handle_exception(e):
        response = json.dumps({"error": e.message})
        return Response(response, mimetype='application/json'), 400

    @app.route('/v1/add', methods=['POST'])
    @default_request_validator
    def addition(arg1, arg2):
        return prepare_response(Decimal(arg1) + Decimal(arg2))

    @app.route('/v1/diff', methods=['POST'])
    @default_request_validator
    def difference(arg1, arg2):
        return prepare_response(Decimal(arg1) - Decimal(arg2))

    @app.route('/v1/multi', methods=['POST'])
    @default_request_validator
    def multiplication(arg1, arg2):
        return prepare_response(Decimal(arg1) * Decimal(arg2))

    @app.route('/v1/div', methods=['POST'])
    @default_request_validator
    def division(arg1, arg2):
        arg2 = Decimal(arg2)
        if arg2 == 0:
            raise InvalidRequest('Division by zero!')
        return prepare_response(Decimal(arg1) / arg2)

    return app


if __name__ == '__main__':
    run_app().run(host="0.0.0.0", port=23232, debug=True)
