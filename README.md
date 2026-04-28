# Workmate

CLI-приложение для обработки CSV-файлов с метриками YouTube-видео и генерации отчётов.

## Возможности

- принимает один или несколько CSV-файлов через `--files`
- принимает название отчёта через `--report`
- формирует единый отчёт по всем переданным файлам
- выводит результат в консоль в виде таблицы

## Поддерживаемый отчёт

### `clickbait`

Показывает видео, у которых одновременно:

- `ctr > 15`
- `retention_rate < 40`

Результат сортируется по убыванию `ctr`.

## Запуск

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[test]"
python3 main.py --files stats1.csv stats2.csv --report clickbait
```

Также можно использовать console script:

```bash
workmate --files stats1.csv stats2.csv --report clickbait
```

## Тесты

```bash
pytest
```
# workmate
