from app import db, User, app

def create_admin(username, password):
    admin = User(username=username, password=password, is_admin=True)
    db.session.add(admin)
    db.session.commit()
    print(f'Admin user {username} created successfully.')

if __name__ == '__main__':
    username = input('Enter admin username: ')
    password = input('Enter admin password: ')
    with app.app_context():
        create_admin(username, password)
