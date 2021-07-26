from flask_admin.contrib.sqla import ModelView


class ParticipantsAdminView(ModelView):
    column_searchable_list = (
        "name",
        "email",
        "phone"
    )
    column_editable_list = (
        "name",
        "email",
        "phone",
        "created_date",
    )
    column_filters = (
        "username",
        "email",
        "phone"
    )
    column_sortable_list = (
        "username",
        "email",
        "phone",
        "created_date",
    )
    column_default_sort = ("created_date", True)
