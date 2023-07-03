from dataclasses import dataclass, field
from typing import Callable, List, Union
from dash.dependencies import handle_callback_args
from dash.dependencies import Input, Output, State


@dataclass
class Callback:
    func: Callable
    outputs: Union[Output, List[Output]]
    inputs: Union[Input, List[Input]]
    states: Union[State, List[State]] = field(default_factory=list)
    kwargs: dict = field(default_factory=lambda: {"prevent_initial_call": False})


class CallbackManager:
    """
    Manages all callbacks made in a dash application allowing layout and callbacks to be separated into different files.

    It is taken from S.Piechaczek answer here:
    https://stackoverflow.com/questions/62102453/how-to-define-callbacks-in-separate-files-plotly-dash
    """
    def __init__(self):
        self._callbacks = []

    def callback(self, *args, **kwargs):
        output, inputs, state, prevent_initial_call = handle_callback_args(
            args, kwargs
        )

        def wrapper(func):
            self._callbacks.append(
                Callback(
                    func,
                    output,
                    inputs,
                    state,
                    {"prevent_initial_callback": prevent_initial_call}
                )
            )

        return wrapper

    def attach_to_app(self, app):
        for callback in self._callbacks:
            app.callback(
                callback.outputs,
                callback.inputs,
                callback.states,
                **callback.kwargs
            )(callback.func)