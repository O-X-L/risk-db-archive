#!/usr/bin/env python3

from os import listdir
from pathlib import Path

FIELDS = ['time', 'ip', 'ip_an', 'cat', 'cmt', 'by', 'user', 'fp']


def main():
    base_dir = Path(__file__).parent
    dedupe_map = {}

    for f in listdir(base_dir / 'dedupe'):
        field = f.replace('field_', '').replace('.csv', '')
        if field not in dedupe_map:
            dedupe_map[field] = {}

        with open(base_dir / 'dedupe' / f, 'r', encoding='utf-8') as _f:
            init = False
            for l in _f.readlines():
                if not init:
                    init = True
                    continue

                try:
                    k, v = l.strip().split(',')
                    dedupe_map[field][k] = v

                except ValueError:
                    print(l)

    for y in listdir(base_dir):
        if not y.startswith('20'):
            continue

        for m in listdir(base_dir / y):
            for f_in in listdir(base_dir / y / m):
                if not f_in.endswith('.csv') or f_in.find('redupe') != -1:
                    continue

                f_out = f'{f_in[:-4]}_redupe.csv'
                with open(base_dir / y / m / f_in, 'r', encoding='utf-8') as fin:
                    with open(base_dir / y / m / f_out, 'w', encoding='utf-8') as fout:
                        lines = [','.join(FIELDS)]

                        init = False
                        for l in fin.readlines():
                            if not init:
                                init = True
                                continue

                            values = l.strip().split(',')
                            for field_idx, field in enumerate(FIELDS):
                                if field in dedupe_map:
                                    value = values[field_idx]
                                    if value in dedupe_map[field]:
                                        values[field_idx] = dedupe_map[field][value]

                            lines.append(','.join(values))

                        fout.write('\n'.join(lines))


if __name__ == '__main__':
    main()
