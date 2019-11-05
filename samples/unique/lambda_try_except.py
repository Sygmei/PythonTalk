(lambda __contextlib: (
    lambda: (lambda __ctx: [__ctx.__enter__(), __ctx.__exit__(None, None, None)])(
        (lambda exit_stack: (
            lambda exit_stack_enter: (
                [exit_stack_enter, [
                    exit_stack_enter.enter_context(ctx)
                    for ctx in [
                        type("except", (), {
                            "__enter__": lambda _s: None,
                            "__exit__": lambda _s, _exct, _exc, _tb: 
                                _exct and (issubclass(_exct, ZeroDivisionError) and [
                                    0
                                    for instruction in [
                                        print("Dividing by 0 is impossible")
                                    ]
                                ]
                            ),
                        })(),
                        type("try", (), {
                            "__enter__": lambda _s: None,
                            "__exit__": lambda _s, _exct, _exc, _tb: [
                                0
                                for instruction in [
                                    print((25 / 0))
                                ]
                            ],
                        })(),
                    ]
                ]][0]
            )
        )(exit_stack.__enter__()))(__contextlib.ExitStack())
    )
)())(__import__("contextlib"))

try: 
    print(25/0)
except ZeroDivisionError: 
    print("Dividing by 0 is impossible")