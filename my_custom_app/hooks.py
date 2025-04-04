app_name = "my_custom_app"
app_title = "My Custom App"
app_publisher = "My Custom App"
app_description = "My Custom App"
app_email = "mycustomapp@gmail.com"
app_license = "mit"



fixtures = [
    {
        "dt": "Workflow",
        "filters": [["custom_module", "=", "my_custom_app"]]
    },

    {
        "dt": "Role",
        "filters": [["name", "in", ["Requester", "Auditor", "Projects Manager", "Special User"]]]
    },
    {
        "dt": "DocType",
        "filters": [["name", "=", "Leave Request"]]
    },

    {
    "dt": "Custom DocPerm",
    "filters": [["parent", "=", "Leave Request"]]
    }

]


