import hashlib


def calculate_password_hash(config, password):
    secret = config.password_secret
    module = hashlib.md5()
    string = f'{password}+{secret}'
    module.update(bytes(string, encoding='utf-8'))
    password_hash = module.hexdigest()
    return password_hash


def check_login(db, config, username, password):
    password_hash = calculate_password_hash(config, password)
    row = db.execute('SELECT count(id) from users where username=? and password=?', (username, password_hash)).fetchone()
    if row:
        return int(row[0]) > 0
    return False


def get_name_by_username(db, username):
    user = user_by_username(db, username)
    if user:
        return f'{user["lastname"]}, {user["firstname"]}'
    else:
        return None


def check_admin(db, username):
    user = user_by_username(db, username)
    if user:
        return bool(user["is_admin"])
    else:
        return False


def user_by_username(db, username):
    row = db.execute('SELECT * from users where username=?', (username,)).fetchone()
    if row:
        user = dict(row)
        user.pop('password', None)
        return user
    return None

