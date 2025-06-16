from .models import Team, Theme1, Theme2
from .database import db

# チーム
def create_team(name):
    team = Team(name=name)
    db.session.add(team)
    db.session.commit()
    return team

def create_teams(names):
    teams = []
    for name in names:
        if name.strip():
            teams.append(create_team(name.strip()))
    return teams

def get_teams():
    return Team.query.all()

def delete_team(team_id):
    team = Team.query.get(team_id)
    if team:
        db.session.delete(team)
        db.session.commit()
        return True
    return False

# お題1
def create_theme1(name):
    theme = Theme1(name=name)
    db.session.add(theme)
    db.session.commit()
    return theme

def create_theme1s(names):
    themes = []
    for name in names:
        if name.strip():
            themes.append(create_theme1(name.strip()))
    return themes

def get_theme1s():
    return Theme1.query.all()

def delete_theme1(theme_id):
    theme = Theme1.query.get(theme_id)
    if theme:
        db.session.delete(theme)
        db.session.commit()
        return True
    return False

# お題2
def create_theme2(name):
    theme = Theme2(name=name)
    db.session.add(theme)
    db.session.commit()
    return theme

def create_theme2s(names):
    themes = []
    for name in names:
        if name.strip():
            themes.append(create_theme2(name.strip()))
    return themes

def get_theme2s():
    return Theme2.query.all()

def delete_theme2(theme_id):
    theme = Theme2.query.get(theme_id)
    if theme:
        db.session.delete(theme)
        db.session.commit()
        return True
    return False