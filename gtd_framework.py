class TODO:
    def __init__(self, vobject_instance):
        self.name = vobject_instance.vtodo.summary.value
        self.completed_at = self._get_completion_date(vobject_instance)
        self.created_at = self._get_creation_date(vobject_instance)

    def _get_completion_date(self, vobject_instance):
        try:
            return vobject_instance.vtodo.completed.value.replace(tzinfo=None)
        except Exception:
            return None

    def _get_creation_date(self, vobject_instance):
        try:
            return vobject_instance.vtodo.created.value.replace(tzinfo=None)
        except Exception:
            # TODO: This should not happen, report this.
            return None


def _get_slug(calendar):
    return calendar.url.split("/")[-2]


def _filter_gtd_calendars(calendars):
    gtd = ['next-actions', 'waiting-for', 'projects', 'some-daymaybe', 'in']
    return filter(lambda x: _get_slug(x) in gtd, calendars)


def get_todos(calendars):
    todos = {}

    for calendar in _filter_gtd_calendars(calendars):
        todos[_get_slug(calendar)] = [TODO(todo.vobject_instance) for todo in calendar.todos(include_completed=True)]
    return todos
