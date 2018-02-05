для установки python зависимостей

    pip install -r requeirements.txt

для запуска jupyter

    jupyter notebook --notebook-dir="$PWD"


Для добавления своего скрипта в scripts,
необходимо предварительно настраивать django

Для этого в начале скрипта пропишите:

    from run_with_django import setup_django
    setup_django()
