from datetime import datetime

users = []
usersData = {}

userPost = []
postData = {}


def post(username):
    print("What's on your mind...")
    userpost = input("Enter your post : ")

    current_date = datetime.now().date()
    current_date = current_date.strftime('%D')

    postData['post'] = userpost
    postData['date'] = current_date
    postData['username'] = username

    userPost.append(postData.copy())

    login_success(username)


def view_profile(username):
    pass


def update_profile(username):
    pass


def delete_profile(username):
    pass


def logout(username):
    pass


def err_handler(**args):
    print("Wrong Choice...")


def login_success(username):
    print("Welcome", username)

    if len(userPost) > 0:
        for p in reversed(userPost):
            print("Post :", p['post'])
            print("By :", p['username'])
            print("On :", p['date'])

    print("""
    1. Post Something
    2. View Profile
    3. Update Profile
    4. Delete Profile
    5. Logout
    """)

    userChoice = input("Enter your choice : ")

    options = {
        '1': post,
        '2': view_profile,
        '3': update_profile,
        '4': delete_profile,
        '5': logout
    }

    options.get(userChoice, err_handler)(username)


def login():
    useremail = input("Enter your EmailID : ")
    userpwd = input("Enter your password : ")

    for data in users:
        if data['usermail'] == useremail and data['userpwd'] == userpwd:
            print("Login Successfull")
            # break
            login_success(data['username'])
        else:
            print("Login Failed...")

    # print("Login Now")


def register():
    # print("Register Now")
    username = input("Enter your Name : ")
    usermail = input("Enter your EmailID : ")
    userpwd = input("Enter your Password : ")
    confpwd = input("Confirm Password : ")

    usersData['username'] = username
    usersData['usermail'] = usermail
    usersData['userpwd'] = userpwd

    users.append(usersData.copy())
    print("Registered Successfully...")
    for data in users:
        print(data)


main = True
while main:
    print("""
    1. Login
    2. Register
    3. Quit
    """)

    options = {
        "1": login,
        "2": register,
    }

    userChoice = input("Enter your choice : ")
    if userChoice == "3":
        main = False
    else:
        options.get(userChoice, err_handler)()