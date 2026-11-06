# Конфигурация проекта. Интерфейс — в gui.rpy и screens.rpy.
define config.name = _("History Stones")
define config.version = "0.1.0"
define gui.show_name = True
define gui.about = _("Минимальный каркас визуальной новеллы.")

define build.name = "HistoryStones"

# Постоянное имя каталога сохранений: не менять при обновлении версии игры.
define config.save_directory = "HistoryStonesTheGame"

# Стандартные звуковые каналы; аудиофайлы в каркасе пока отсутствуют.
define config.has_sound = True
define config.has_music = True
define config.has_voice = False

# Начальные значения; изменения игрока сохраняются средствами Ren'Py.
default preferences.text_cps = 0
default preferences.afm_time = 15

define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None
define config.window = "auto"
define config.window_show_transition = Dissolve(0.2)
define config.window_hide_transition = Dissolve(0.2)

init python:
    # Исходники инструментов и служебные файлы не включаются в дистрибутив.
    build.classify(".tools/**", None)
    build.classify(".git/**", None)
    build.classify("**/~*", None)
    build.classify("**/*.bak", None)
    build.classify("**/.DS_Store", None)
    build.classify("README.md", None)
