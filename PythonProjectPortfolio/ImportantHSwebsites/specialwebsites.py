import sys
import webbrowser

def url_style_format(text):
    return text.replace(" ", "+")

if len(sys.argv) != 2:
    sys.exit()

elif sys.argv[1] == "classroom":
    webbrowser.open("https://classroom.google.com/")

elif sys.argv[1] == "classlink":
    webbrowser.open("https://launchpad.classlink.com/edison")

elif sys.argv[1] == 'gemini':
    webbrowser.open("https://gemini.google.com/app")

elif sys.argv[1] == 'gmail':
    webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
    
elif sys.argv[1] == 'gsnake':
    webbrowser.open("https://www.google.com/search?q=snake")

elif sys.argv[1] == 'search':
    try:    
        webbrowser.open("https://www.google.com/search?q=" + url_style_format(sys.argv[2]))
    except IndexError:
        webbrowser.open("https://www.google.com")

else:
    print("Enter a valid command!")
    quit()

