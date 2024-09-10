# from app import db, Abonnement, Utilisateur, Session, Camera

# # Créer une formule d'abonnement
# basic_plan = Abonnement(name='Basic', price=50.0, max_users=1, max_cameras_per_session=5, max_sessions_per_user=3)
# db.session.add(basic_plan)
# db.session.commit()

# # Créer un utilisateur
# user1 = Utilisateur(email='user1@example.com', password='password123', subscription_id=basic_plan.id)
# db.session.add(user1)
# db.session.commit()

# # Créer une session
# session1 = Session(user_id=user1.id, session_name='Session 1')
# db.session.add(session1)
# db.session.commit()

# # Ajouter une caméra à la session
# camera1 = Camera(session_id=session1.id, camera_name='Camera 1', camera_url='http://192.168.1.100')
# db.session.add(camera1)
# db.session.commit()

from run import db, Abonnement, Utilisateur, Session, Camera

class AdminDashboard:
    # CRUD pour les Abonnements
    @staticmethod
    def create_abonnement(name, price, max_users, max_cameras_per_session, max_sessions_per_user):
        abonnement = Abonnement(name=name, price=price, max_users=max_users, max_cameras_per_session=max_cameras_per_session, max_sessions_per_user=max_sessions_per_user)
        db.session.add(abonnement)
        db.session.commit()
        return abonnement

    @staticmethod
    def get_abonnement(abonnement_id):
        return Abonnement.query.get(abonnement_id)

    @staticmethod
    def update_abonnement(abonnement_id, name=None, price=None, max_users=None, max_cameras_per_session=None, max_sessions_per_user=None):
        abonnement = Abonnement.query.get(abonnement_id)
        if abonnement:
            if name:
                abonnement.name = name
            if price:
                abonnement.price = price
            if max_users:
                abonnement.max_users = max_users
            if max_cameras_per_session:
                abonnement.max_cameras_per_session = max_cameras_per_session
            if max_sessions_per_user:
                abonnement.max_sessions_per_user = max_sessions_per_user
            db.session.commit()
        return abonnement

    @staticmethod
    def delete_abonnement(abonnement_id):
        abonnement = Abonnement.query.get(abonnement_id)
        if abonnement:
            db.session.delete(abonnement)
            db.session.commit()
        return abonnement

    # CRUD pour les Utilisateurs
    @staticmethod
    def create_utilisateur(email, password, subscription_id):
        utilisateur = Utilisateur(email=email, password=password, subscription_id=subscription_id)
        db.session.add(utilisateur)
        db.session.commit()
        return utilisateur

    @staticmethod
    def get_utilisateur(utilisateur_id):
        return Utilisateur.query.get(utilisateur_id)

    @staticmethod
    def update_utilisateur(utilisateur_id, email=None, password=None, subscription_id=None):
        utilisateur = Utilisateur.query.get(utilisateur_id)
        if utilisateur:
            if email:
                utilisateur.email = email
            if password:
                utilisateur.password = password
            if subscription_id:
                utilisateur.subscription_id = subscription_id
            db.session.commit()
        return utilisateur

    @staticmethod
    def delete_utilisateur(utilisateur_id):
        utilisateur = Utilisateur.query.get(utilisateur_id)
        if utilisateur:
            db.session.delete(utilisateur)
            db.session.commit()
        return utilisateur

    # CRUD pour les Sessions
    @staticmethod
    def create_session(user_id, session_name):
        session = Session(user_id=user_id, session_name=session_name)
        db.session.add(session)
        db.session.commit()
        return session

    @staticmethod
    def get_session(session_id):
        return Session.query.get(session_id)

    @staticmethod
    def update_session(session_id, session_name=None):
        session = Session.query.get(session_id)
        if session:
            if session_name:
                session.session_name = session_name
            db.session.commit()
        return session

    @staticmethod
    def delete_session(session_id):
        session = Session.query.get(session_id)
        if session:
            db.session.delete(session)
            db.session.commit()
        return session

    # CRUD pour les Caméras
    @staticmethod
    def add_camera(session_id, camera_name, camera_url):
        camera = Camera(session_id=session_id, camera_name=camera_name, camera_url=camera_url)
        db.session.add(camera)
        db.session.commit()
        return camera

    @staticmethod
    def get_camera(camera_id):
        return Camera.query.get(camera_id)

    @staticmethod
    def update_camera(camera_id, camera_name=None, camera_url=None):
        camera = Camera.query.get(camera_id)
        if camera:
            if camera_name:
                camera.camera_name = camera_name
            if camera_url:
                camera.camera_url = camera_url
            db.session.commit()
        return camera

    @staticmethod
    def delete_camera(camera_id):
        camera = Camera.query.get(camera_id)
        if camera:
            db.session.delete(camera)
            db.session.commit()
        return camera
