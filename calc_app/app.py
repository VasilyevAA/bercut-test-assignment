from decimal import Decimal

from flask import Flask, jsonify, request, abort
from flask_request_validator import (
    JSON,
    Param,
    Pattern,
    validate_params
)


def prepare_request(case_request):
    data = case_request.json
    return Decimal(data['arg1']), Decimal(data['arg2'])


def prepare_response(data):
    return jsonify({'result': data})


def run_app():
    app = Flask(__name__)
    default_request_validator = validate_params(
        Param('arg1', JSON, str, rules=[Pattern(r'^\d{1,}(\.?\d{1,6}$)?')]),
        Param('arg2', JSON, str, rules=[Pattern(r'^\d{1,}(\.?\d{1,6}$)?')]),
    )

    @app.route('/v1/add', methods=['POST'])
    @default_request_validator
    def addition():
        arg1, arg2 = prepare_request(request)
        return prepare_response(arg1 + arg2)

    @app.route('/v1/diff', methods=['POST'])
    @default_request_validator
    def difference():
        arg1, arg2 = prepare_request(request)
        return prepare_response(arg1 - arg2)

    @app.route('/v1/multi', methods=['POST'])
    @default_request_validator
    def multiplication():
        arg1, arg2 = prepare_request(request)
        return prepare_response(arg1 * arg2)

    @app.route('/v1/div', methods=['POST'])
    @default_request_validator
    def division():
        arg1, arg2 = prepare_request(request)
        if arg2 == 0:
            abort(400)
        return prepare_response(arg1 / arg2)

    return app


if __name__ == '__main__':
    run_app().run(host="0.0.0.0", port=8080, debug=True)
