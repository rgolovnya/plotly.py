import _plotly_utils.basevalidators


class TickorientationValidator(
    _plotly_utils.basevalidators.EnumeratedValidator
):

    def __init__(
        self,
        plotly_name='tickorientation',
        parent_name='layout.angularaxis',
        **kwargs
    ):
        super(TickorientationValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            role='style',
            values=['horizontal', 'vertical'],
            **kwargs
        )
