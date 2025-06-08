from flask import Blueprint, request, jsonify
from src.main.factories.calculator1_factory import calculator1_factory
from src.main.factories.calculator2_factory import calculator2_factory
from src.main.factories.calculator3_factory import calculator3_factory
from src.main.factories.calculator4_factory import calculator4_factory
from src.errors.error_controller import handle_error

calc_route_bp = Blueprint('calc_routes', __name__)

@calc_route_bp.route('/calculator/1', methods=['POST'])
def calculator_1():
    calc = calculator1_factory()

    try:
        result = calc.calculate(request)
        return jsonify(result), 200
    except Exception as e:
        return handle_error(e)

@calc_route_bp.route('/calculator/2', methods=['POST'])
def calculator_2():
    calc = calculator2_factory()

    try:
        result = calc.calculate(request)
        return jsonify(result), 200
    except Exception as e:
        return handle_error(e)

@calc_route_bp.route('/calculator/3', methods=['POST'])
def calculator_3():
    calc = calculator3_factory()

    try:
        result = calc.calculate(request)
        return jsonify(result), 200
    except Exception as e:
        return handle_error(e)

@calc_route_bp.route('/calculator/4', methods=['POST'])
def calculator_4():
    calc = calculator4_factory()

    try:
        result = calc.calculate(request)
        return jsonify(result), 200
    except Exception as e:
        return handle_error(e)