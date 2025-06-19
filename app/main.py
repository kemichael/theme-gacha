from flask import Flask, render_template, request, redirect, url_for
from app.database import init_db, db
from app.routes.team import bp as team_bp
from app.routes.theme1 import bp as theme1_bp
from app.routes.theme2 import bp as theme2_bp
from app.routes.draw import bp as draw_bp

def create_app():
    # Flaskアプリケーションのインスタンスを作成
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static"
    )
    # データベースの初期化
    init_db(app)

    # テンプレートの自動リロードを有効化
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    # アプリケーションコンテキスト内でDBテーブルを作成
    with app.app_context():
        db.create_all()

    # Route
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/theme1", methods=["GET", "POST"])
    def theme1():
        from app.crud import create_theme1, get_theme1s
        if request.method == "POST":
            names = request.form.get("names")
            if names:
                name_list = [n.strip() for n in names.split('\n') if n.strip()]
                for name in name_list:
                    create_theme1(name)
            return redirect(url_for("theme1"))
        themes = get_theme1s()
        return render_template("theme1.html", themes=themes)

    @app.route("/theme1/delete/<int:theme_id>")
    def delete_theme1_view(theme_id):
        from app.crud import delete_theme1
        delete_theme1(theme_id)
        return redirect(url_for("theme1"))

    @app.route("/theme2", methods=["GET", "POST"])
    def theme2():
        from app.crud import create_theme2, get_theme2s
        if request.method == "POST":
            names = request.form.get("names")
            if names:
                name_list = [n.strip() for n in names.split('\n') if n.strip()]
                for name in name_list:
                    create_theme2(name)
            return redirect(url_for("theme2"))
        themes = get_theme2s()
        return render_template("theme2.html", themes=themes)

    @app.route("/theme2/delete/<int:theme_id>")
    def delete_theme2_view(theme_id):
        from app.crud import delete_theme2
        delete_theme2(theme_id)
        return redirect(url_for("theme2"))

    @app.route("/teams", methods=["GET", "POST"])
    def teams():
        from app.crud import create_teams, get_teams
        if request.method == "POST":
            names = request.form.get("names")
            if names:
                name_list = [n.strip() for n in names.split('\n') if n.strip()]
                create_teams(name_list)
            return redirect(url_for("teams"))
        teams = get_teams()
        return render_template("teams.html", teams=teams)

    @app.route("/teams/delete/<int:team_id>")
    def delete_team_view(team_id):
        from app.crud import delete_team
        delete_team(team_id)
        return redirect(url_for("teams"))

    @app.route("/draw", methods=["GET", "POST"])
    def draw():
        from app.models import Team, Theme1, Theme2
        import random
        teams = Team.query.all()
        theme1s = Theme1.query.all()
        theme2s = Theme2.query.all()
        results = []
        if request.method == "POST":
            for team in teams:
                t1 = random.choice(theme1s)
                t2 = random.choice(theme2s)
                results.append({
                    "team": team.name,
                    "theme1": t1.name,
                    "theme2": t2.name
                })
        return render_template("draw.html", results=results)
    
    return app

# アプリケーション起動
app = create_app()
