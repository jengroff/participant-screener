from flask_admin.contrib.sqla import ModelView


class ScreenersAdminView(ModelView):
    column_searchable_list = (
        "prospect_name",
        "prospect_email",
        "prospect_phone",
        "prospect_id",
        "study_name",
        "study_id",
        "response_1",
        "response_2",
        "response_3",
        "response_4",
        "response_5",
    )
    column_editable_list = (
        "prospect_name",
        "prospect_email",
        "prospect_phone",
        "prospect_id",
        "study_name",
        "study_id",
        "response_1",
        "response_2",
        "response_3",
        "response_4",
        "response_5",
    )
    column_filters = (
        "prospect_name",
        "prospect_email",
        "prospect_phone",
        "prospect_id",
        "study_name",
        "study_id",
        "response_1",
        "response_2",
        "response_3",
        "response_4",
        "response_5",
    )
    column_sortable_list = (
        "prospect_name",
        "prospect_email",
        "prospect_phone",
        "prospect_id",
        "study_name",
        "study_id",
        "response_1",
        "response_2",
        "response_3",
        "response_4",
        "response_5",
    )
    column_default_sort = ("created_date", True)
