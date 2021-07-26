from flask_admin.contrib.sqla import ModelView


class ScreenersAdminView(ModelView):
    column_searchable_list = (
        "name",
        "email",
        "phone",
        "study_name",
        "study_id",
        "response_1",
        "response_2",
        "response_3",
        "response_4",
        "response_5",
    )
    column_editable_list = (
        "name",
        "email",
        "phone",
        "study_name",
        "study_id",
        "response_1",
        "response_2",
        "response_3",
        "response_4",
        "response_5",
        "created_date",
    )
    column_filters = (
        "name",
        "email",
        "phone",
        "study_name",
        "study_id",
        "response_1",
        "response_2",
        "response_3",
        "response_4",
        "response_5",
    )
    column_sortable_list = (
        "name",
        "email",
        "phone",
        "study_name",
        "study_id",
        "response_1",
        "response_2",
        "response_3",
        "response_4",
        "response_5",
        "created_date",
    )
    column_default_sort = ("created_date", True)
