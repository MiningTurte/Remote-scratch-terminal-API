import scratchattach as sa3
import os
def tab(name):
    os.system('clear')
    print(name)
def login():
    os.system('clear')
    print("Login to scratch")
    username = input("Username ")
    os.system('clear||cls')
    print("Login to scratch")
    password = input("Password ")
    os.system('clear||cls')

    session = sa3.login(username, password)
    account = session.get_linked_user()
    def main():
        os.system('clear')
        print("Successfully logged in as " + str(account) + "\n\n")
        print("Information")
        # Get account information
        followers = account.follower_count()
        followingAmount = account.following_count()
        messages = account.message_count()
        projectCount = account.project_count()
        studioCount = account.studio_count()
        userID = account.id

        print("Messages: " + str(messages))
        print("Followed by " + str(followers) + " users")
        print("Following " + str(followingAmount) + " users")
        print("Projects: " + str(projectCount))
        print("Studios: " + str(studioCount))
        print("User ID: " + str(userID) + "\n\n")
        
        print("Actions")
        print("1 | Follow a user")
        print("2 | Unfollow a user")
        print("3 | Comment on your profile")
        print("4 | Toggle commenting")
        print("5 | Set about me")
        print("6 | Set wiwo")
        print("7 | Change featured project")
        print("8 | Accept studio invite")
        print("9 | Invite user to studio")
        print("A | Remove user from studio")
        print("B | Promote user from studio")
        print("C | Remove yourself from a studio")
        print("D | List all profile comments")
        print("E | Reply to a comment")
        print("F | Fetch a user's information")
        
        
        print("""\n\nTo logout say "logout" """)
        action = input("\n")
        
        if action == "logout":
            login()
        elif action == "1":
            tab('Follow')
            the_user = input("Username: ")
            user = session.connect_user(str(the_user))
            user.follow()
            print("Successfully followed user")
                    
            back = input("\nBack? (Y/N) ")
            if back == "Y":
                main()
            else:
                os.system('clear')
        elif action == "2":
            tab('Unfollow')
            the_user = input("Username: ")
            user = session.connect_user(str(the_user))
            user.unfollow()
            print("Successfully unfollowed user")
            
            back = input("\nBack? (Y/N) ")
            if back == "Y":
                main()
            else:
                os.system('clear')            
        elif action == "3":
            tab('Comment on your profile')
            comment = input("Comment: ")
            print("Sending...")
            account.post_comment(str(comment))
            print("Comment has been sent!")
            
            back = input("\nBack? (Y/N) ")
            if back == "Y":
                main()
            else:
                os.system('clear')    
        elif action == "4":
            tab('Toggle Commenting')
            account.toggle_commenting()
            print("Succesfully toggled commenting!")
            
            back = input("\nBack? (Y/N) ")
            if back == "Y":
                main()
            else:
                os.system('clear')    
        elif action == "5":
            tab('Set about me')
            bio = input("New about me: ")
            account.set_bio = str(bio)
            print("Successfully set new about me!")
            
            back = input("\nBack? (Y/N) ")
            if back == "Y":
                main()
            else:
                os.system('clear')    
        elif action == "6":
            tab('Set WIWO')
            wiwo = input("New WIWO: ")
            account.set_wiwo = str(wiwo)
            print("Successfully set new wiwo!")
            
            back = input("\nBack? (Y/N) ")
            if back == "Y":
                main()
            else:
                os.system('clear')    
        elif action == "7":
            tab('Change featured project')
            projectID = input("Project ID: ")
            account.set_featured(str(projectID), label="")
            print("Successfully changed featured project!")
            
            back = input("\nBack? (Y/N) ")
            if back == "Y":
                main()
            else:
                os.system('clear')    
        elif action == "8":
            tab('Accept studio invite')
            studioID = input("Studio ID: ")
            studio = session.connect_studio(str(studioID))
            studio.accept_invite()
            print("Successfully accepted invitation!")
            
            back = input("\nBack? (Y/N) ")
            if back == "Y":
                main()
            else:
                os.system('clear')    
        elif action == "9":
            tab('Invite user to studio')
            studioID = input("Studio ID: ")
            print("Connecting to studio...")
            studio = session.connect_studio(str(studioID))
            print("Successfully connected to studio!")
            theirUsername = input("User: ")
            studio.invite_curator(str(theirUsername))
            print("Invitation successfully sent!")
            
            back = input("\nBack? (Y/N) ")
            if back == "Y":
                main()
            else:
                os.system('clear')    
        elif action == "A":
            tab('Remove user from studio')
            studioID = input("Studio ID: ")
            print("Connecting to studio...")
            studio = session.connect_studio(str(studioID))
            print("Successfully connected to studio!")
            theirUsername = input("User: ")
            studio.remove_curator(str(theirUsername))
            print("Successfully removed user!")
            
            back = input("\nBack? (Y/N) ")
            if back == "Y":
                main()
            else:
                os.system('clear')    
        elif action == "B":
            tab('Promote user from studio')
            studioID = input("Studio ID: ")
            print("Connecting to studio...")
            studio = session.connect_studio(str(studioID))
            print("Successfully connected to studio!")
            theirUsername = input("User: ")
            studio.promote_curator(str(theirUsername))
            print("Successfully promoted user!")
            
            back = input("\nBack? (Y/N) ")
            if back == "Y":
                main()
            else:
                os.system('clear')    
        elif action == "C":
            tab('Remove yourself from a studio')
            studioID = input("Studio ID: ")
            print("Connecting to studio...")
            studio = session.connect_studio(str(studioID))
            print("Successfully connected to studio!")
            studio.leave()
            print("Successfully left studio!")
            
            back = input("\nBack? (Y/N) ")
            if back == "Y":
                main()
            else:
                os.system('clear')    
        elif action == "D":
            tab('List all of your profile comments')
            pageNum = input("Page: ")
            os.system('clear')
            print("Loading... \n\n")
            comments = account.comments(limit=None, page=pageNum)
            print(str(comments))
            print("\nSuccessfully loaded!")
            
            back = input("\nBack? (Y/N) ")
            if back == "Y":
                main()
            else:
                os.system('clear')    
        elif action == "E":
            tab('Reply to a comment on your profile')
            commentID = input("Comment ID: ")
            comentee = input("Parent comment user ID: ")
            contents = input("Comment: ")
            account.reply_comment(str(contents), parent_id=str(commentID), commentee_id=str(comentee))
            print("Successfully replied!")
            
            back = input("\nBack? (Y/N) ")
            if back == "Y":
                main()
            else:
                os.system('clear')    
        elif action == "F":
            tab("Fetch a user's information")
            usersName = input("Username: ")
            print("Fetching user...")
            user = session.connect_user(str(usersName))
            print("Connecting... \n")
            print("Join date: " + str(user.join_date))
            print("About me: " + str(user.about_me))
            print("WIWO: " + str(user.wiwo))
            print("Country: " + str(user.country))
            print("Icon URL: " + str(user.icon_url))
            print("User ID: " + str(user.id))
            print("Scratchteam? " + str(user.scratchteam))
            back = input("\nBack? (Y/N) ")
            if back == "Y":
                main()
            else:
                os.system('clear')    
    main()
login()
