from app import db, Abonnement, Utilisateur, Session, Camera

# Créer une formule d'abonnement
basic_plan = Abonnement(name='Basic', price=50.0, max_users=1, max_cameras_per_session=5, max_sessions_per_user=3)
db.session.add(basic_plan)
db.session.commit()

# Créer un utilisateur
user1 = Utilisateur(email='user1@example.com', password='password123', subscription_id=basic_plan.id)
db.session.add(user1)
db.session.commit()

# Créer une session
session1 = Session(user_id=user1.id, session_name='Session 1')
db.session.add(session1)
db.session.commit()

# Ajouter une caméra à la session
camera1 = Camera(session_id=session1.id, camera_name='Camera 1', camera_url='http://192.168.1.100')
db.session.add(camera1)
db.session.commit()
