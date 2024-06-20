from win10toast import ToastNotifier

toaster = ToastNotifier()


toaster.show_toast(
    "Notificação",
    "Sempre se orgulhe de seus feitos!",
    threaded=True,
    icon_path=None,
    duration=3
)
