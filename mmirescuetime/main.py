import datetime
import mothermayi.colors
import mothermayi.errors
import mothermayi.files
import requests

def plugin():
    return {
        'name'          : 'rescuetime',
        'post-commit'   : post_commit,
    }

def do_sort(filename):
    results = SortImports(filename)
    return getattr(results, 'in_lines', None) and results.in_lines != results.out_lines

def get_status(had_changes):
    return mothermayi.colors.red('unsorted') if had_changes else mothermayi.colors.green('sorted')

def post_commit(config, commit):
    api_key = config.get('rescuetime', {}).get('api_key', None)
    if not api_key:
        raise mothermayi.errors.FailHook("Cannot find recuetime api_key")

    payload = {
        'key'               : api_key,
        'highlight_date'    : datetime.date.today().isoformat(),
        'description'       : commit['Title'],
        'source'            : 'code commit',
    }
    try:
        response = requests.post('https://www.recuetime.com/anapi/highlights_post', data=payload)
    except requests.exceptions.ConnectionError as e:
        raise mothermayi.errors.FailHook(str(e))

    if not response.ok:
        failure = "{}: {}".format(response.status_code, response.text)
        raise mothermayi.errors.FailHook(failure)

    return []
