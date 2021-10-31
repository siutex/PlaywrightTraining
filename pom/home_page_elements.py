class HomePage:
    home_url = "https://siutex.pythonanywhere.com/"
    blog_layout = ":nth-match(div:has-text(\"July 3, 2016, 10:53 p.m. " \
                  "Welcome This is my first, test post. Please be patient.\"), 3)"
    main_page = "text=siutex's blog"
    login_page = "span"
    username_input = "input[name=\"username\"]"
    password_input = "input[name=\"password\"]"
    login_button = "text=Login"
