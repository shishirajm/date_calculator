default_date_format = 'DD/MM/YYYY'


def _extract_date_ddmmyyy(date):
    if date.count('/') != 2:
        raise Exception(f'"{date}" is in unsupported format, use format "{default_date_format}"')

    try:
        return list(map(lambda x: int(x), date.split('/')))
    except Exception as e:
        raise Exception(f'"{date}" is in unsupported format, use format "{default_date_format}"')


def _extract_date_fields(date_format):
    if date_format is None or date_format.lower() == default_date_format.lower():
        return _extract_date_ddmmyyy
    else:
        raise Exception(f'"{date_format}" is unsupported format, use format "{default_date_format}"')


class FormatterFactory:
    def extract(self, date, date_format):
        extractor = _extract_date_fields(date_format)
        return extractor(date)

