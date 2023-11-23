if request.method == "POST":
    # CHECK IF USERNAME ALREADY EXSISTS IN DB
    existing_user = mongo.db.users.find_one(
        {"username": request.form.get("username").lower()}
    )
    if existing_user:
        # ENSURED HASH PASSWORD MATCHES USER INPUT
        if check_password_hash(existing_user["password"], request.form.get("password")):
            session["user"] = request.form.get("username").lower()
            flash("Welcome, {}".format(request.form.get("username")))
            return redirect(url_for("profile", username=session["user"]))
        else:
            # INVALID PASSWORD
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    else:
        # USERNAME DOESN'T EXIST
        flash("Incorrect Username and/or Password")
        return redirect(url_for("login"))
