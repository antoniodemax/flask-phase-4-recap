from app import app
from models import *

with app.app_context():

    db.session.query(user_groups).delete()
    db.session.commit()
    
    User.query.delete()
    Group.query.delete()
    Post.query.delete()

    # db.session.delete(user_groups)

    u1 = User(username = "user1", email="user1@example.com")
    u2 = User(username = "user2", email="user2@example.com")
    u3 = User(username = "user3", email="user3@example.com")
    u4 = User(username = "user4", email="user4@example.com")
    u5 = User(username = "user5", email="user5@example.com")

    

    db.session.add_all([u1,u2, u3, u4, u5])
    db.session.commit()


    p1 = Post(title="post1", content="post1 description", user=u1)
    p2 = Post(title="post2", content="post2 description", user=u2)
    p3 = Post(title="post3", content="post3 description", user=u3)
    p4 = Post(title="post4", content="post4 description", user=u4)
    p5 = Post(title="post5", content="post5 description", user=u5)




    db.session.add_all([p1, p2, p3, p4, p5])
    db.session.commit()

    g1 = Group(name="group1")
    g2 = Group(name="group2")
    g3 = Group(name="group3")
    g4 = Group(name="group4")
    g5 = Group(name="group5")

    db.session.add_all([g1, g2, g3, g4, g5])
    db.session.commit()

    #add groups to users
    u1.groups.append(g2)
    u1.groups.append(g4)
    u2.groups.append(g1)
    u3.groups.append(g5)
    # u2.groups.append(g3)
    # u2.groups.append(g4)
    # u3.groups.append(g5)
    # u4.groups.append(g1)
    # u4.groups.append(g2)
    # u5.groups.append(g3)
    # u5.groups.append(g4)

    #add users to groups
    g5.users.append(u1)
    g1.users.append(u4)
    g4.users.append(u3)
    # g2.users.append(u4)
    # g3.users.append(u2)
    # g3.users.append(u5)
    # g4.users.append(u1)
    # g4.users.append(u2)
    # g4.users.append(u3)
    # g4.users.append(u5)
    # g5.users.append(u3)
    # g5.users.append(u4)

    #add posts to groups
    # g1.posts.append(p1)
    # g1.posts.append(p2)
    # g2.posts.append(p3)
    # g2.posts.append(p4)
    # g3.posts.append(p5)
    # g3.posts.append(

    db.session.commit()

    # print("Users, Groups, and Posts created successfully!")



