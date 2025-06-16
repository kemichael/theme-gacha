from flask import Blueprint, request, jsonify
from ..crud import create_team, get_teams, delete_team
from ..schemas import team_schema

bp = Blueprint('team', __name__, url_prefix='/teams')

@bp.route('', methods=['GET'])
def list_teams():
    teams = get_teams()
    return jsonify([team_schema(t) for t in teams])

@bp.route('', methods=['POST'])
def add_team():
    # 複数行対応
    names = request.json.get('names')
    if names:
        # 改行で分割して複数登録
        name_list = [n.strip() for n in names.split('\n') if n.strip()]
        teams = [team_schema(t) for t in create_team(name_list)]
        return jsonify(teams), 201
    else:
        # 1件だけ
        name = request.json.get('name')
        team = create_team(name)
        return jsonify(team_schema(team)), 201

@bp.route('/<int:team_id>', methods=['DELETE'])
def remove_team(team_id):
    if delete_team(team_id):
        return jsonify({"result": "ok"})
    return jsonify({"result": "not found"}), 404