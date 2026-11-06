# Точка входа. Сценарии глав находятся в game/chapters/.
label start:
    call prologue from _call_prologue

    # При пустом стеке вызовов return возвращает в главное меню Ren'Py.
    return
