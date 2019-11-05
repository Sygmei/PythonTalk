self.inputs = {
    key: NodeInput(
        self,
        key,
        value.underlying_type if is_input_flagged(value) else value,
        True if is_input_flagged(value) and (value & Hidden) else False,
        kwargs[key]
        if key in kwargs
        else {
            args[self.counter.incr()]
            if self.counter.get() < len(args)
            else None
        },
    )
    for i, (key, value) in enumerate(function.__annotations__.items())
    if key
    not in [
        "return",
        self.function_arg_spec.varargs,
        self.function_arg_spec.varkw,
    ]
}