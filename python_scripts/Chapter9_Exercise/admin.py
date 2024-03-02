from users import User, Admin, Privileges

privilege = Privileges("can add post", "can delete post", "can ban user")

admin = Admin("Tunde", "Akingbade",privilege)
admin.rights.show_privileges()